# -*- coding: utf-8 -*-
"""
Created on Wed May 22 22:24:06 2019

@author: MPAZ
"""

import ccxt
import claves

#ACCESAR A BINANCE
usuario=claves.api_key
clave=claves.secret


#instancia mediante id a Binance con claves 
exchange_id= 'binance'
exchange_class = getattr(ccxt, exchange_id)
exchange= exchange_class({
	'apiKey':usuario,
	'secret':clave,
	'timeout':30000,
	'enableRateLimit:': True,
})

casas_cambio=ccxt.exchanges
mercados=exchange.load_markets(True)
monedas= exchange.currencies
simbolos=exchange.symbols
metodos=dir(exchange)

print("empezamos")




saldob1=exchange.fetch_balance()['ETC']['free']
saldoq1=exchange.fetch_balance()['SKY']['free']


#ordenes_cerradas=exchange.fetch_closed_orders(par1) # LISTADO ORDENES CERRADAS
print("ORDEN CERRADA !!! ")

#prueba3=exchange.fetch_my_trades(par1)
