# -*- coding: utf-8 -*-
"""
Created on Fri May 24 23:12:28 2019

@author: MPAZ

VERSION MEJORADA DE ARBITRAJE ENTRE 3 PARES EN BINANCE


"""
import ccxt
import asyncio
import ccxt.async_support as ccxta
import claves
import numpy as np
import time

import os
import sys

root = os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))))
sys.path.append(root + '/python')

inicio=round(time.time()*1000)      # INICIO EN ms

# CLAVES A BINANCE
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

filas = data.shape[0]
columnas = data.shape[1]

print('Tienes una matriz de ' + str(filas) + " x " + str(columnas))

#VA GRABANDO VALORES QUE PUEDEN SER UTILES DEL EXCHANGE

casas_cambio = ccxt.exchanges
exchange=ccxt.binance()
mercados=exchange.load_markets(True)
monedas = exchange.currencies
simbolos = exchange.symbols
metodos = dir(exchange)


#EMPIEZA A EJECUTARSE EL NUCLEO DURO DEL SISTEMA
medio=round(time.time()*1000)

# ESTO HAY QUE ADAPTARLO A HACER 3 ORDENES DE FORMA CONCURRENTE


'''
def sync_client(exchange):
    client = getattr(ccxt, exchange)()
    tickers = client.fetch_tickers()
    return tickers
'''


''''
async def async_client(exchange):
    client = getattr(ccxta, exchange)()
    tickers = await client.fetch_tickers()
    await client.close()
    return tickers
'''

'''
async def multi_tickers(exchanges):
    input_coroutines = [async_client(exchange) for exchange in exchanges]
    tickers = await asyncio.gather(*input_coroutines, return_exceptions=True)
    return tickers
'''






fin=round(time.time()*1000)      # INICIO EN ms
duracion=fin-inicio
print('el tiempo de ejecucion del programa esta en {} milisegundos'.format(duracion))

'''
if __name__ == '__main__':

    # Consider review request rate limit in the methods you call
    exchanges = ["coinex", "binance", "bitfinex" ]

    tic = time.time()
    a = asyncio.get_event_loop().run_until_complete(multi_tickers(exchanges))
    print("async call spend:", time.time() - tic)

    time.sleep(1)

    tic = time.time()
    a = [sync_client(exchange) for exchange in exchanges]
    print("sync call spend:", time.time() - tic)
'''
