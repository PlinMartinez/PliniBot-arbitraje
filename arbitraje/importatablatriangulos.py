BU# VAMOS A IMPORTAR LA TABLA CON TRIANGULACION PARA DESPUES ENTRAR EN EXCHANGE Y CACULAR PROFIT EN CVV Y VVC
import ccxt
import claves
import pandas as pd
import numpy as np

# ABRE EL FICHERO Y LEE EL CONTENIDO

filename = 'bitbankarbitraje.txt'
file = open(filename, mode='r')
text = file.read()
file.close()
print(text)


# ABRE EL FICHERO Y LO TOMA COMO ARRAY DE A x B FILAS / COLUMNAS

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

par1 = data[1, 0]
par2 = data[1, 1]
par3 = data[1, 2]


''' ACCESAR A BINANACE
usuario = claves.api_key
clave = claves.secret
'''


''' instancia mediante id a Binance con claves
exchange_id = 'binance'
exchange_class = getattr(ccxt, exchange_id)
binance = exchange_class({
    'apiKey': usuario,
    'secret': clave,
    'timeout': 30000,
    'enableRateLimit:': True,
})
'''


casas_cambio = ccxt.exchanges

# binance=ccxt.binance()

exchange_trabajo = 'bitbank'

exchange = ccxt.bitbank()


mercados = exchange.load_markets(True)

monedas = exchange.currencies

simbolos = exchange.symbols

metodos = dir(exchange)

print("empezamos")

''' MIRAMOS PRIMERO CVV >=1 Y LUEGO VCC >=1  YA VIENE EN LA IMPORTACION DEL FICHERO
par1 = 'ADA/BTC'  # COMPRA
par2 = 'ETH/BTC'  # VENTA
par3 = 'ADA/ETH'  # VENTA
'''

c1 = exchange.fetch_order_book(par1)['bids'][0][0]
v2 = exchange.fetch_order_book(par2)['asks'][0][0]
v3 = exchange.fetch_order_book(par3)['asks'][0][0]


gasto1 = 1000 * c1  # 1000 ADAS , GASTADO 0.011080 BTC
i2 = gasto1 / v2  # INGRESO 2 EN ETH GASTANDO LOS BTC DEL PASO 1
i3 = i2 / v3  # INGRESO 3 EN ADA GASTANDO LOS ETH DEL PASO 2

resultadoCVV = round((i3 - 1000), 2)
prueba = i3 - 1000
prueba2 = round(prueba, 2)


''' MIRAMOS AHORA VCC >=1 YA VIENE EN LA IMPORTACION DEL FICHERO
par1 = 'ADA/BTC'  # VENTA
par2 = 'ETH/BTC'  # COMPRA
par3 = 'ADA/ETH'  # COMPRA
'''

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

print(resultadoVCC)
print(resultadoCVV)
