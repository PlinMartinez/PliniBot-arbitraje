# VAMOS A IMPORTAR LA TABLA CON TRIANGULACION PARA DESPUES ENTRAR EN EXCHANGE Y CACULAR PROFIT EN CVV Y VVC
import ccxt
import claves
import numpy as np

# ABRE EL FICHERO Y LEE EL CONTENIDO
# MODIFICAR PARA CADA USO EL EXCHANGE A USAR Y EL FICHERO BASE CON LISTADO DE TRIANGULOS DE ARBITRAGE
# POR EJEMPLO BINANCE & binancemini.txt
# VAMOS A HACER PRIMERO SOLO  VCC CON STOCK DE ALGUNAS CRIPTOMONEDAS COMO LTC O SKY

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

beneficio = []


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


def disparaVCC(par1, par2, par3):

      
    libro1 = exchange.fetch_order_book(par1)
    libro2 = exchange.fetch_order_book(par2)
    libro3 = exchange.fetch_order_book(par3)
    altobid1=libro1['bids'][0][0]
    bajoask1=libro1['asks'][0][0]
    altobid2=libro2['bids'][0][0]
    bajoask2=libro2['asks'][0][0]
    altobid3=libro3['bids'][0][0]
    bajoask3=libro3['asks'][0][0]
    
    #LANZA PAR 1 MEDIANTE CALCULOS ESPECIFICOS CALCULAR GASTAR 1,2 MIN NOTIONAL
    
    min_notional1 = exchange.markets[par1]['info']['filters'][3]['minNotional']
    notional1 = float(min_notional1)
    minimovolumenventa = notional1 / altobid1
    minimosubido20 = minimovolumenventa * 1.5
    minimoajustado = round(minimosubido20, 8)
    cantidadventa1ajustado=notional1/altobid1
    cantidadventa1subido20=cantidadventa1ajustado*1.5
    cantidad_venta1=round(cantidadventa1subido20,8)
    valor_venta1=cantidad_venta1*altobid1
    
    print('voy a lanzar el pedido 1')
    symbol1 = par1
    type1 = 'market'
    side1 = 'sell'
    amount1 = minimoajustado
    venta1=exchange.create_order(symbol1,type1,side1,amount1)
    print('hecho el paso 1 V')
    
    print('voy a lanzar el pedido 2')
    
    consulta_venta1=exchange.fetch_orders(par1)[-1]
    q2_por_gastar=consulta_venta1['cost']
    amount2provisional=q2_por_gastar/bajoask2
    amount2r=round(amount2provisional,8)
    valor_compra2=amount2r*bajoask2
    
    symbol2= par2
    type2='market'
    side2='buy'
    amount2=amount2r
    compra2=exchange.create_order(symbol2,type2,side2,amount2)
    print('hecho el paso 2 !!!')
    
    # AHORA TOCA EL PAR3 FINALMENTE...
    
    print('Empiezo la ultima orden numero 3 para cerrar circulo')
    
    consulta_compra2=exchange.fetch_orders(par2)[-1]
    b3_comprado=consulta_compra2['amount']
    cantidad_compra3=b3_comprado/bajoask3
    cantidad_compra3r=round(cantidad_compra3,8)
    valor_compra3=cantidad_compra3r*bajoask3
    
    symbol3=par3
    type3='market'
    side3='buy'
    amount3=cantidad_compra3r
    compra3=exchange.create_order(symbol3,type3,side3,amount3)
    print('ya esta por fin')
    
    consulta_compra3=exchange.fetch_orders(par3)[-1]
    cantidad_fin=consulta_compra3['amount']
    cantidad_inicio=consulta_venta1['amount']
    resultado=cantidad_fin-cantidad_inicio
    porcentaje=(resultado/cantidad_inicio)
    print('EL RESULTADO DE VCC HA SIDO ')
    print(round(resultado,8))
    q1=par1.split('/')[0]
    print(q1)
    print('El porcentaje ganado o perdido sobre la base')
    print(round(porcentaje,3))


print("empezamos")

contador=0

while contador <100:
    

    for i in range(0, filas):
    
        try:
            par1 = data[i - 1, 0]
            par2 = data[i - 1, 1]
            par3 = data[i - 1, 2]
            print(par1)
    
            c1 = exchange.fetch_order_book(par1)['bids'][0][0]
            v2 = exchange.fetch_order_book(par2)['asks'][0][0]
            v3 = exchange.fetch_order_book(par3)['asks'][0][0]
    
            gasto1 = 1000 * c1  # 1000 ADAS , GASTADO 0.011080 BTC
            i2 = gasto1 / v2  # INGRESO 2 EN ETH GASTANDO LOS BTC DEL PASO 1
            i3 = i2 / v3  # INGRESO 3 EN ADA GASTANDO LOS ETH DEL PASO 2
    
            resultadoCVV = round((i3 - 1000), 2)
            prueba = i3 - 1000
            prueba2 = round(prueba, 2)
            resultadoCVV2 = prueba2
    
            v1 = exchange.fetch_order_book(par1)['asks'][0][0]
            c2 = exchange.fetch_order_book(par2)['bids'][0][0]
            c3 = exchange.fetch_order_book(par3)['bids'][0][0]
    
            venta1 = 1000 * v1  # 1000 ADAS VENDO , INGRESO 0.01117 BTC
            i2 = gasto1 / v2  # INGRESO 2 EN ETH GASTANDO LOS BTC DEL PASO 1
            i3 = i2 / v3  # INGRESO 3 EN ADA GASTANDO LOS ETH DEL PASO 2
    
            resultadoCVV = i3 - 1000
            g2 = venta1 / c2
            g3 = g2 / c3
    
            resultadoVCC = round((g3 - 1000), 2)
    
            print(str(par1) + '-' + str(par2) + '-' + str(par3) +
                  ' en modo VCC y CVV da sobre 1.000 unidades de base1')
            print(str(resultadoVCC) + "  " + str(resultadoCVV2))
            if resultadoCVV > 15:
                print('OJO, OPORTUNIDAD DE GANAR UN 1% CVV')
                beneficio.append(par1 + ',' + par2 + ',' + par3 +
                                 ',' + str(resultadoVCC) + ',' + str(resultadoCVV2))
                print('COMPRA C VV Y CORTA EL PROGRAMA')
    
            if resultadoVCC > 15:
                print('OJO, OPORTUNIDAD DE GANAR UN 1% EN MODO VCC')
                beneficio.append(par1 + ',' + par2 + ',' + par3 +
                                 ',' + str(resultadoVCC) + ',' + str(resultadoCVV2))
                par1string = str(par1)
                par2string = str(par2)
                par3string = str(par3)
                disparaVCC(par1string, par2string, par3string)
                print('VENDIDO V CC Y CORTADO EL PROGRAMA')
                break
            contador=contador+1
            
    
        except:
            print('algo ha fallado en un triangulo raro')

fichero = nombre + 'beneficio.txt'

contador = 0
with open(fichero, 'w') as f:
    for i in beneficio:
        f.write(beneficio[contador])
        f.write('\n')
        contador = contador + 1
        print("linea grabada")
print("ok, grabado!!")
