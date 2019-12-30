# VAMOS A IMPORTAR LA TABLA CON TRIANGULACION PARA DESPUES ENTRAR EN EXCHANGE Y CACULAR PROFIT EN CVV Y VVC
import ccxt
import claves
import pandas as pd
import numpy as np

# ABRE EL FICHERO Y LEE EL CONTENIDO
# MODIFICAR PARA CADA USO EL EXCHANGE A USAR Y EL FICHERO BASE CON LISTADO DE TRIANGULOS DE ARBITRAGE
# POR EJEMPLO BINANCE & binancemini.txt

#ACCESAR A BINANCE
usuario=claves.api_key
clave=claves.secret

#instancia mediante id a Binance con claves 
nombre = 'binance'
exchange_class = getattr(ccxt, nombre)
exchange= exchange_class({
	'apiKey':usuario,
	'secret':clave,
	'timeout':30000,
	'enableRateLimit:': True,
})


filename = 'binancearbitraje.txt'


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

print("empezamos")

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
        if resultadoCVV > 10:
            print('OJO, OPORTUNIDAD DE GANAR UN 1% CVV')
            beneficio.append(par1 + ',' + par2 + ',' + par3 +
                             ',' + str(resultadoVCC) + ',' + str(resultadoCVV2))
            print('COMPRA C VV Y CORTA EL PROGRAMA')
            break
        

        if resultadoVCC > 10:
            print('OJO, OPORTUNIDAD DE GANAR UN 1% EN MODO VCC')
            beneficio.append(par1 + ',' + par2 + ',' + par3 +
                             ',' + str(resultadoVCC) + ',' + str(resultadoCVV2))
            print('VENDE V CC Y CORTA EL PROGRAMA')
            #break

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
