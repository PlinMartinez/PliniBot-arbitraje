# -*- coding: utf-8 -*-
"""
Created on Thu May 23 00:32:37 2019

@author: MPAZ

VENDE SKY/BTC
COMPRA BNB/BTC
COMPRA SKY/BNB


"""

# VAMOS A IMPORTAR LA TABLA CON TRIANGULACION PARA DESPUES ENTRAR EN EXCHANGE Y CACULAR PROFIT EN CVV Y VVC
import ccxt
import claves
import pandas as pd
import numpy as np

# ABRE EL FICHERO Y LEE EL CONTENIDO
# MODIFICAR PARA CADA USO EL EXCHANGE A USAR Y EL FICHERO BASE CON LISTADO DE TRIANGULOS DE ARBITRAGE
# POR EJEMPLO BINANCE & binancemini.txt
# VAMOS A HACER SOLO VCC CON STOCK DE 

#ACCESAR A BINANCE
usuario=claves.api_key
clave=claves.secret

#instancia mediante id a Binance con claves 
nombre = 'binance'
exchange_class = getattr(ccxt, nombre)
exchange= exchange_class({
	'apiKey':usuario,
	'secret':clave,
	'timeout':30000,
	'enableRateLimit:': True,
})



casas_cambio = ccxt.exchanges

# binance=ccxt.binance()


mercados = exchange.load_markets(True)

monedas = exchange.currencies

simbolos = exchange.symbols

metodos = dir(exchange)


print('EMPIEZA A DISPARAR')

par1='SKY/ETH'
par2='BNB/ETH'
par3='SKY/BNB'

b1 = par1.split('/')[0]
print('b1 es ' + str(b1))
q1 = par1.split('/')[1]
print('q1 es ' + str(q1))
b2 = par2.split('/')[0]
print('b2 es ' + str(b2))
q2 = par2.split('/')[1]
print('q2 es ' + str(q2))
b3 = par3.split('/')[0]
print('b3 es ' + str(b3))
q3 = par3.split('/')[1]
print('q3 es ' + str(q3))
    

 #LANZA PAR 3
    
libro3=exchange.fetch_order_book(par3)
ask3=libro3['asks'][0][0]
bid3=libro3['bids'][0][0]
medio3=(ask3+bid3)/2
compra3=medio3*0.98
                  
amount_compra3=0.01/compra3
amount_compra32=amount_compra3*1.02

symbol=str(par3)
type='market'
side='buy'
saldoq3=exchange.fetch_balance()[b2]['free']
amount=saldoq3/ask3  # COMPRA gastando el q1 al completo
venta1=exchange.create_order(symbol,type,side,amount)
print('hecho el paso 3 V')