# -*- coding: utf-8 -*-
"""
Created on Fri May 31 21:18:05 2019

@author: MPAZ
"""

import ccxt
import claves
import pprint
import pandas as pd

''' ACTIVA EL DEPURADOR
import logging
logging.basicConfig(level=logging.DEBUG)
'''

''' PROBAR PARA NO EXCEDER VELOCIDAD
# Python
exchange = ccxt.binance ({
    'rateLimit': 10000,  # unified exchange property
    'options': {
        'adjustForTimeDifference': True,  # exchange-specific option
    }
})
exchange.options['adjustForTimeDifference'] = False
'''

print ("hola")

#LISTA EXCHANGES
casas=ccxt.exchanges

#INSTANCIAR EXCHANGE BINANCE CON LIMITACION VELOCIDAD LLAMADAS
exchange = ccxt.binance( { 'enableRateLimit' : True , })

#INSTANCIAR KRAKEN 
kraken = ccxt.kraken()

#instanciar exchange metodo getattr
gdax = getattr(ccxt,'gdax')()


#cargar mercados
mgdax=gdax.load_markets()

#modificar condiciones exchange
exchange.enableRateLimit = True


#instancia mediante id a Binance con claves 
exchange_id= 'binance'
usuario=claves.api_key
clave=claves.secret
exchange_class = getattr(ccxt, exchange_id)
exchange= exchange_class({
	'apiKey':usuario,
	'secret':clave,
	'timeout':30000,
	'enableRateLimit:': True,
})

''' CARGAR E IMPRIMIR MERCADOS
okcoin=ccxt.okcoinusd()
markets=okcoin.load_markets()
print(okcoin.id, markets)
'''
mercados=exchange.load_markets()

#IMPRIME LISTADO PARES   >>> UTIL PARA BUSCAR PAREJA SOBRE MONEDA...
monedas=list(exchange.markets.keys())
#LISTADO DE PARES >>> MUY UTIL PARA CRUZAR CON SALDOS Y HACER MARKET MAKER
symbols=exchange.symbols

#listado de MONEDAS  
currencies=exchange.currencies

symbol='VIA/ETH'

ordenescerradas=exchange.fetchClosedOrders (symbol)

