# -*- coding: utf-8 -*-
"""
Created on Sun Apr 28 17:45:10 2019

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
binance= exchange_class({
	'apiKey':usuario,
	'secret':clave,
	'timeout':30000,
	'enableRateLimit:': True,
})


monedas= binance.currencies

metodos=dir(binance)

print("empezamos")

# separa los mercados por ETH

mercados=binance.load_markets(True)
mercados_ETH=[]

for key in mercados:
    print (key)
    separado=key.split("/")
    if separado[1]=='ETH':
        mercados_ETH.append(key)
        print ('ok')
        
print (mercados_ETH)
print (len(mercados_ETH))
