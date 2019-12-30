# VAMOS A IMPORTAR LA TABLA CON TRIANGULACION PARA DESPUES ENTRAR EN EXCHANGE Y CACULAR PROFIT EN CVV Y VVC
import ccxt
import claves
import numpy as np
from datetime import datetime
import time

# ABRE EL FICHERO Y LEE EL CONTENIDO
# MODIFICAR PARA CADA USO EL EXCHANGE A USAR Y EL FICHERO BASE CON LISTADO DE TRIANGULOS DE ARBITRAGE
# POR EJEMPLO BINANCE & binancemini.txt
# VAMOS A HACER PRIMERO SOLO  VCC CON STOCK DE ALGUNAS CRIPTOMONEDAS COMO LTC O SKY


# AÑADIMOS FUNCIONES DE FECHAS Y TIEMPOS PARA VER DONDE SE VA EL TIEMPO
ahora = datetime.now()
dia = ahora.strftime("%Y%m%d")

t0 = time.time()



# ACCESAR A BINANCE
usuario = claves.api_key
clave = claves.secret

# instancia mediante id a Binance con claves
nombre = 'binance'
exchange_class = getattr(ccxt, nombre)
exchange = exchange_class({
    'apiKey': usuario,
    'secret': clave,
    'timeout': 30000,
    'enableRateLimit:': True,
})

# Tabla con arbitrajes que va a revisar solamente, quitar los que no parezcan interesantes
filename = 'binancearbitrajemini.txt'


file = open(filename, mode='r')
text = file.read()
file.close()
print(text)


# ABRE EL FICHERO Y LO TOMA COMO MATRIZ DE A x B FILAS / COLUMNAS

data = np.loadtxt(filename,
                  delimiter='-',
                  usecols=[0, 1, 2],
                  dtype=str)

print(data)
print(type(data))

print(data.shape)
print(data[1, 0])
print(data[1, 1])
print(data[1, 2])

filas = data.shape[0]
columnas = data.shape[1]

print('Tienes una matriz de ' + str(filas) + "x" + str(columnas))


casas_cambio = ccxt.exchanges

# binance=ccxt.binance()


mercados = exchange.load_markets(True)

monedas = exchange.currencies

simbolos = exchange.symbols

metodos = dir(exchange)

ganancias = []


'''
REALIZA LAS ORDENES DE COMPRA CVV O VCC DE FORMA CONTINUADA A VER SI ALGO GANA

FUN/BTC,ETH/BTC,FUN/ETH,11.94,-15.92
REQ/BTC,ETH/BTC,REQ/ETH,12.65,-10.03
POWR/ETH,BNB/ETH,POWR/BNB,12.58,-7.09
AMB/BTC,BNB/BTC,AMB/BNB,12.68,-18.3
AMB/ETH,BNB/ETH,AMB/BNB,14.06,-18.75
BCPT/ETH,BNB/ETHCPT/BNB,10.26,-10.28
CDT/BTC,ETH/BTC,CDT/ETH,11.29,-4.54

HACEMOS EJEMPLO CON PSEUDOCODIGO A COMPLETAR Y PROBAR CON SALDO REAL EN OREGON 


#SI PAR1 Q1 ES BTC O ETH, SI VA BIEN COMPRAR DE OTRAS TAMBIEN

'''

print("empezamos")

t1=time.time()-t0

ganancias=[]

contador=1

while contador <2:

    print('CICLO DE TRABAJO NUMERO ' + str(contador))

    for i in range(0, filas):
        try:
            par1 = data[i - 1, 0]  # TOMA LOS 3 PARES DE LA MATRIZ
            par2 = data[i - 1, 1]
            par3 = data[i - 1, 2]
            par1str = str(par1)
            par2str = str(par2)
            par3str = str(par3)
            
            t2=time.time()-t0

            libro_ordenes1 = exchange.fetch_order_book(par1)
            libro_ordenes2 = exchange.fetch_order_book(par2)
            libro_ordenes3 = exchange.fetch_order_book(par3)
            

            # MIRA LOS VALORES ACTUALES DE MERCADO A VER SI VE OPORTUNIDAD
            v1 = libro_ordenes1['bids'][0][0]
            c2 = libro_ordenes2['asks'][0][0]
            c3 = libro_ordenes3['asks'][0][0]
            t3=time.time()-t0
            altobid1 = venta1 = v1
            bajoask2 = compra2 = c2
            bajoask3 = compra3 = c3

            # SACA Q MIN COMPRAS
            minimo_notional1 = (mercados)[
                par1]['info']['filters'][3]['minNotional']
            notional1 = float(minimo_notional1)
            #altobid1 = libro_ordenes1['bids'][0][0]
            qminimo1 = notional1 / altobid1
            qmin1 = round((qminimo1 * 1.5), 8)
            

            minimo_notional2 = (mercados)[
                par2]['info']['filters'][3]['minNotional']
            notional2 = float(minimo_notional2)
            #bajoask2 = libro_ordenes2['asks'][0][0]
            qminimo2 = notional2 / bajoask2
            qmin2 = round((qminimo2 * 1.5), 8)

            minimo_notional3 = (mercados)[
                par3]['info']['filters'][3]['minNotional']
            notional3 = float(minimo_notional3)
            #bajoask3 = libro_ordenes3['asks'][0][0]
            qminimo3 = notional3 / bajoask3
            qmin3 = round((qminimo3 * 1.5), 8)

            print(par1str, '-', par2str, '-', par3str)
            resultadoVCC=((compra2*compra3)/venta1)*1000
            resultadoVCCredondeo=round(resultadoVCC,2)
            print (resultadoVCCredondeo)
            beneficioVCC=resultadoVCC-1000
            print(round(beneficioVCC,2))
            if beneficioVCC>10:
                print('HAY OPORTUNIDAD DE GANAR >1%, EJECUTA COMPRA')
                
                symbol1 = par1
                type1 = 'limit'
                side1 = 'sell'
                amount1 = qmin1
                symbol2 = par2
                type2 = 'limit'
                side2 = 'buy'
                amount2 = qmin2
                symbol3 = par3
                type3 = 'limit'
                side3 = 'buy'
                amount3 = qmin3
                
                ganancias.append('T,'+symbol1+','+side1+','+str(altobid1)+','+
                                 str(qmin1)+','+symbol2+','+side2+','+str(bajoask2)+','+
                                 str(qmin2)+','+symbol3+','+side3+','+str(bajoask3)+','+
                                 str(qmin3)+',')
                
                tic = time.time()
                print('VAMOS A EJECUTAR ORDEN 1 : '+symbol1+'-'+type1+'-'+side1+'-'+str(amount1))
                #exchange.create_order(symbol1,type1,side1,amount1,v1)
                print('VAMOS A EJECUTAR ORDEN 2 : '+symbol2+'-'+type2+'-'+side2+'-'+str(amount2))
                #exchange.create_order(symbol2,type2,side2,amount2,c2)
                print('VAMOS A EJECUTAR ORDEN 3 : '+symbol3+'-'+type3+'-'+side3+'-'+str(amount3))
                #exchange.create_order(symbol3,type3,side3,amount3,c3)
                print("TRIANGULO CERRADO")
                #AQUI HABRA QUE GRABAR EL RESULTADO FINAL
                

                print("Tiempo consumido: ", time.time() - tic)
               






        except Exception as e:
            print(exchange.id, 'fetch_order_book failed with:', str(e))

        except:
            print('Ha pasado algun fallo en este proceso, depurar')
            # AÑADIR ERRORES MAS INFO

    contador = contador + 1

fichero = 'ganancias' + 'binance' + dia + '.txt'

contador_lineas = 0

print(t0)
print(t1)
print(t2)
print(t3)

'''
contador_tiempos=0

tiempos=[t0,t1,t2,t3]

with open(tiempos, 'w') as f:

    for i in tiempos:
        f.write(ganancias[contador_tiempos])
        f.write('\n')

        contador_tiempos = contador_tiempos + 1
        print("tiempo registrado")
    print("ok, DATA LOG GRABADO !!")

'''

with open(fichero, 'w') as f:

    for i in ganancias:
        f.write(ganancias[contador_lineas])
        f.write('\n')

        contador_lineas = contador_lineas + 1
        print("linea grabada")
    print("ok, grabado!!")
