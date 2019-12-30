# -*- coding: utf-8 -*-

import asyncio
import os
import sys
import claves
import time

inicio = round(time.time() * 1000)      # INICIO EN ms

root = os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))))
sys.path.append(root + '/python')

import ccxt.async_support as ccxt  # noqa: E402

# CLAVES A BINANCE
usuario = claves.api_key
clave = claves.secret

exchange = ccxt.binance({
    'apiKey': usuario,
    'secret': clave,
    'enableRateLimit': True,  # this is required, as documented in the Manual!
})


async def test():

    response = None

    try:

        await exchange.load_markets('ADA/ETH')
        await exchange.load_markets('ETH/BTC')  # force-preload markets first

        exchange.verbose = True  # this is for debugging

        symbol = 'ADA/BTC'  # change for your symbol
        amount = 1.0        # change the amount
        price = 0.000001     # change the price

        try:

            response = await exchange.create_limit_buy_order(symbol, amount, price)

        except Exception as e:
            print('Failed to create order with',
                  exchange.id, type(e).__name__, str(e))

    except Exception as e:
        print('Failed to load markets from',
              exchange.id, type(e).__name__, str(e))

    await exchange.close()
    return response

fin = round(time.time() * 1000)      # INICIO EN ms
duracion = fin - inicio
print('el tiempo de ejecucion del programa esta en {} milisegundos'.format(duracion))


if __name__ == '__main__':
    print(asyncio.get_event_loop().run_until_complete(test()))
