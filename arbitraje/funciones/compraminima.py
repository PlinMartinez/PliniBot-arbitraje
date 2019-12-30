# -*- coding: utf-8 -*-
"""
Created on Sat Jun  1 09:43:29 2019

@author: MPAZ

TOMA UN PAR >> REVISA LIBRO DE ORDENES >> COMPRA LO MINIMO >> ASI VCC OK

"""




import ccxt
import claves



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


par='YOYOW/BTC'

print(' V1.0', par)

mercados=exchange.load_markets(True)

libro_ordenes = exchange.fetch_order_book(par,5)


pc = libro_ordenes['asks'][0][0]
pv = libro_ordenes['bids'][0][0]


minimo_notional1 = (mercados)[
            par]['info']['filters'][3]['minNotional']
notional1 = float(minimo_notional1)*2


minima_compra=notional1/pc

print('Orden de compra minima')
symbol= par
type= 'limit'
side= 'buy'
amount= round(minima_compra,6)
price=  round(pc,8)
orden= exchange.create_order(symbol,type,side,amount,price)
print('Orden ejecutada correctamente')












