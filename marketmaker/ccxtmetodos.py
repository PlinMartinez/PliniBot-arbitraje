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

''' recorrer diccionarios >> usar con SALDO SACAR PLAN ACCION, CRUZAR CON PARES
for i in currencies:
    print (currencies[i]['precision'])
    numero=currencies[i]['precision']
'''

''' listado metodos disponible por exchange
metodos=dir(ccxt.binance())
'''

''' PASAR PARAMETROS A ENDPOINTS
zaif=ccxt.zaif().public_get_ticker_pair({'pair':'btc_jpy'})
'''

''' PASAR PARAMETROS EXTRAS A ENDPOINTS
params = { ' foo' : 'bar' } 
resultado = exchange.fetch_order_book(symbol, length, params)
'''
''' AJUSTA DECIMALES AL NUMERO
numero=3.1423923
decimales=4
numeroajustado=round(numero,decimales)
'''

''' RESINCRONIZA TIEMPO EN LINEA DE COMANDOS
w32tm /resync
'''

pprint.pprint(mercados['ZRX/USDT']['precision']['amount'])

''' usa requests >> mira URL >>> convierte a JSON >>> extrae un dato en concreto
response=responde.get(url)
print(response.json())
datos['ticker']['min_ask'][0]
'''

df=pd.DataFrame(currencies)
dfT=df.T

print (dfT)


#CONSULTAR BALANCE
balance=exchange.fetch_balance()
ada=balance['ADA']['free']

#CREA DICCIONARIO DE MONEDAS SALDO >> USAR PARA PUNTUAR PARES OJO!!!!
saldo_monedas=binance.fetch_free_balance()
saldo_positivo={}
for i in saldo_monedas:
    if int(saldo_monedas[i]) > 0:
        saldo_positivo.update({i:saldo_monedas[i]})

# OPCIONES DE ORDENES
opcionesordenes=exchange.has

#ajusta precio a precision del par
a=exchange.price_to_precision(par1,0.234234234)


# ordenes hechas con ese par
#recent_trades=exchange.fetch_orders(par)


# keep last hour of history in cache
before = exchange.milliseconds () - 1 * 60 * 60 * 1000
# purge all closed and canceled orders "older" or issued "before" that time
exchange.purge_cached_orders (before)

'''CONSULTA ORDEN, FALLA BINANCE ESTE METODO REQUIERE SYMBOL ARGUMENT
if exchange.has['fetchOrder']:
    
    order = exchange.fetch_order('ADA/BNB')
    print(order)
'''

'''
import asyncio
import ccxt.async_support as ccxt
if exchange.has['fetchOrder']:
    order = asyncio.get_event_loop().run_until_complete(exchange.fetch_order(id))
    print(order)
'''




'''

# CONSULTA ORDENES ABIERTAS DE UN PAR
if (exchange.has['fetchOpenOrders']):
    symbol='ADA/BTC'
    ordenesabiertas=exchange.fetchOpenOrders (symbol)

#CONSULTA ORDENES CERRADAS DE UN PAR
if (exchange.has['fetchClosedOrders']):
    ordenescerradas=exchange.fetchClosedOrders (symbol)
symbol='VIA/ETH'
ordeneshechas=exchange.fetch_closed_orders(symbol)
#ordeneshechasbase=ordeneshechas['amount']
#ordeneshechasprecio=ordeneshechas['average']
#ordeneshechasquote=ordeneshechas['cost']


# CANCELAR ORDEN, FALTA AVERIGUAR ANTES EL NUMERO...
#exchange.cancel_order ('1234567890') # replace with your order id here (a string)

# 
# fetch_my_trades (symbol = None, since = None, limit = None, params = {})
if exchange.has['fetchMyTrades']:
    ordeneshechas=exchange.fetch_my_trades (symbol)

#calculateFee (symbol, type, side, amount, price, takerOrMaker = 'taker', params = {})
fee=exchange.markets['ETH/BTC']['taker']
fee2=exchange.markets['ETH/BTC']['maker']

# Python
orderbook = exchange.fetch_order_book (exchange.symbols[0])
bid = orderbook['bids'][0][0] if len (orderbook['bids']) > 0 else None
ask = orderbook['asks'][0][0] if len (orderbook['asks']) > 0 else None
spread = (ask - bid) if (bid and ask) else None
print (exchange.id, 'market price', { 'bid': bid, 'ask': ask, 'spread': spread })
'''

#METODOS DE TIEMPO

ahora = datetime.now()  # Obtiene fecha y hora actual
# current date and time
now = datetime.now()

timestamp = datetime.timestamp(now)
print("timestamp =", timestamp)



#GESTION DE ERRORES:
try:
    intento=exchange.fetch_currencies()
    print(intento)
except ccxt.NetworkError as e:
    print(exchange.id, 'fetch_currencies fallo por error de red:', str(e))
except ccxt.ExchangeError as e:
    print(exchange.id, 'fetch_currencies fallo por error de exchange:', str(e))
except Exception as e:
    print(exchange.id, 'fetch_currencies fallo por:', str(e))
    

''' GRABA FICHEROS .CSV CON DATOS
diccionario = {'a': 0, 'b': 3}


f = open("volatilidades2.csv", "w")
f.write("Par")
f.write(",")
f.write("Volatilidad")
f.write("\n")
for (clave, valor) in diccionario.items():
    print(clave, ",", valor)
    f.write(str(clave))
    f.write(",")
    f.write(str(valor))
    f.write("\n")

'''