# VAMOS A IMPORTAR LA TABLA CON TRIANGULACION PARA DESPUES ENTRAR EN EXCHANGE Y CACULAR PROFIT EN CVV Y VVC
import ccxt
import claves
import pandas as pd
import numpy as np

# ABRE EL FICHERO Y LEE EL CONTENIDO
# MODIFICAR PARA CADA USO EL EXCHANGE A USAR Y EL FICHERO BASE CON LISTADO DE TRIANGULOS DE ARBITRAGE
# POR EJEMPLO BINANCE & binancemini.txt

nombre = 'binance'

#exchange = ccxt.binance({'enableRateLimit': True, })

id = nombre
exchange_class = getattr(ccxt, id)
exchange = exchange_class({'timeout': 3000, 'enableRateLimit': True, })
mercados = exchange.load_markets(True)


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

