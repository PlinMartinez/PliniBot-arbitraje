# -*- coding: utf-8 -*-

import asyncio
import ccxt
import ccxt.async_support as ccxta  # noqa: E402
import time
import os
import sys
import claves
import numpy as np

inicio = round(time.time() * 1000)


# CLAVES A BINANCE
usuario = claves.api_key
clave = claves.secret

# instancia mediante id a Binance con claves

nombre = 'binance'
exchange_class = getattr(ccxt, nombre)
exchange = exchange_class({
    'api_key': usuario,
    'secret': clave,
    'timeout': 30000,
    'enableRateLimit:': True,
})

mercados = exchange.load_markets(True)
monedas = exchange.currencies
simbolos = exchange.symbols
metodos = dir(exchange)
mercados = exchange.markets


# FUNCIONES ASYNCRONAS DE COMPRA >> CON ESTE COMANDO SE LLAMA A EJECUTAR LOS 3
# a = asyncio.get_event_loop().run_until_complete(
# multi_ordenes(symbol1, type1, side1, amount1, symbol2,
# type2, side2, amount2, symbol3, type3, side3, amount3))


async def async_ejecutar_orden(symbol, type, side, amount):

    client = getattr(ccxta, 'binance')({
        'apiKey': usuario,
        'secret': clave,
        'timeout': 30000,
        'enableRateLimit:': True,
    })
    orden = await client.create_order(symbol, type, side, amount)
    await client.close()
    return orden


async def multi_ordenes(symbol1, type1, side1, amount, symbol2, type2, side2, amount2, symbol3, type3, side3, amount3):
    input_ordenes = [async_ejecutar_orden(symbol1, type1, side1, amount1),
                     async_ejecutar_orden(symbol2, type2, side2, amount2),
                     async_ejecutar_orden(symbol3, type3, side3, amount3)]
    ordenes = await asyncio.gather(*input_ordenes, return_exceptions=True)
    return ordenes


# TABLA CON FICHERO TXT DE ARBITRAJES

filename = 'binancearbitrajemini.txt'
file = open(filename, mode='r')
text = file.read()
file.close()
print(text)

# GENERA UNA MATRIZ DE N FILAS PARA IR MIRANDO SI ENCUENTRA BENEFICIO EN ALGUN TRIANGULO
data = np.loadtxt(filename,
                  delimiter='-',
                  usecols=[0, 1, 2],
                  dtype=str)
print(data)
print(data.shape)
print(data[0, 0])
print(data[0, 1])
print(data[0, 2])
filas = data.shape[0]
columnas = data.shape[1]
print('Tienes una matriz de ' + str(filas) +
      " filas x " + str(columnas) + " columnas")

print('EMPEZAMOS A BUSCAR TRIANGULOS CON BENEFICIO')
contador = 1


while contador < 2:

    print('CICLO DE TRABAJO NUMERO ' + str(contador))

    for i in range(0, filas):
        try:
            par1 = data[i - 1, 0]  # TOMA LOS 3 PARES DE LA MATRIZ
            par2 = data[i - 1, 1]
            par3 = data[i - 1, 2]
            par1str = str(par1)
            par2str = str(par2)
            par3str = str(par3)

            recarga_mercados = exchange.load_markets(
                True)  # ESTA LINEA HACE FALTA???
            libro_ordenes1 = exchange.fetch_order_book(
                par1)  # TOMA LOS LIBROS DE ORDENES
            libro_ordenes2 = exchange.fetch_order_book(par2)
            libro_ordenes3 = exchange.fetch_order_book(par3)

            # MIRA LOS VALORES ACTUALES DE MERCADO A VER SI VE OPORTUNIDAD
            v1 = libro_ordenes1['bids'][0][0]
            c2 = libro_ordenes2['asks'][0][0]
            c3 = libro_ordenes3['asks'][0][0]
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
                tic = time.time()

                symbol1 = par1
                type1 = 'market'
                side1 = 'sell'
                amount1 = qmin1
                symbol2 = par2
                type2 = 'market'
                side2 = 'buy'
                amount2 = qmin2
                symbol3 = par3
                type3 = 'market'
                side3 = 'buy'
                amount3 = qmin3

                

                a = asyncio.get_event_loop().run_until_complete(multi_ordenes(symbol1, type1, side1, amount1, symbol2, type2, side2, amount2, symbol3, type3, side3, amount3))
                print("async call spend:", time.time() - tic)






        except Exception as e:
            print(exchange.id, 'fetch_order_book failed with:', str(e))

        except:
            print('Ha pasado algun fallo en este proceso, depurar')
            # AÑADIR ERRORES MAS INFO

    contador = contador + 1


'''

if __name__ == '__main__':

    # Consider review request rate limit in the methods you call
    symbol1 = par1
    type1 = 'market'
    side1 = 'sell'
    amount1 = qmin1
    symbol2 = par2
    type2 = 'market'
    side2 = 'buy'
    amount2 = qmin2
    symbol3 = par3
    type3 = 'market'
    side3 = 'buy'
    amount3 = qmin3

    tic = time.time()
    a = asyncio.get_event_loop().run_until_complete(multi_ordenes(symbol1, type1, side1, amount1, symbol2, type2, side2, amount2, symbol3, type3, side3, amount3))
    print("async call spend:", time.time() - tic)
'''
