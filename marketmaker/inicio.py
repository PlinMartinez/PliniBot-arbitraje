# -*- coding: utf-8 -*-
"""
Created on Sun May 19 17:36:27 2019

@author: MPAZ
"""

""" VAMOS A EMPEZAR SACANDO TODOS LOS METODOS AL PRINCIPIO

CONSULTA PEDIDOS ABIERTOS, CERRADOS, HORA, ...

REVISA SALDO CADA MONEDA

EXPORTA VOLATILIDADES, IMPORTA, SELECCIONA

DESPUES CREAMOS 3 PARES DE TRABAJO CON ALTA VOLATIDAD

ASIGNAMOS SALDO 10 LEYENDO CON JSON SI BAJA A 5 DEJA DE COMPRAR 
SI SUBE A 15 DEJA DE VENDER +-1%

CADA 15 MINUTOS BORRA TODOS LOS PEDIDSO Y CREA NUEVOS
"""

import ccxt
import claves
import datetime
import time
import json

#FICHA FECHA Y HORA ACTUAL Y TIEMPO DE APERTURA DE ORDENES
ahora=datetime.datetime.now()
ahorautc=datetime.datetime.utcnow()
ventana=datetime.timedelta(minutes=15)
cierre=ahora+ventana
inicio=time.time()

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

#VA SACANDO INFO GENERAL DE BINANCE

mercados=exchange.load_markets(True)

monedas= exchange.currencies

Vmonedas = exchange.currencies.keys()

simbolos=exchange.symbols

metodos=dir(exchange)

print("empezamos")

''' CARGA JSON CON MONEDAS POSICION '''

with open('MMmonedas.json') as f:
    MMmonedas = json.load(f)

''' IMPRIME POSICION NEUTRAL MONEDAS
print(MMmonedas)

for i in MMmonedas:
    print(i,MMmonedas[i])
'''


par='EDO/ETH'
moneda1='EDO'
moneda2='ETH'

ordenes_abiertas=exchange.fetch_open_orders(par)
ordenes_cerradas=exchange.fetch_closed_orders(par)
saldo_ETH = exchange.fetch_free_balance()['ETH']
saldo_ADA = exchange.fetch_free_balance()['ADA']
saldo1=exchange.fetch_balance()[moneda1]
saldo2=exchange.fetch_balance()[moneda2]

libro_ordenes=exchange.fetch_order_book(par)
ask=libro_ordenes['asks'][0][0]
bid=libro_ordenes['bids'][0][0]
spread=ask-bid
medio=(ask+bid)/2
compra=medio*0.99
venta=medio*1.01



saldob1libre=exchange.fetch_balance()[moneda1]['free']

amount_compra=0.01/compra
amount_compra2=amount_compra*1.02
amount_venta=0.01/venta
amount_compraR=round(amount_compra2,2)+1
amount_ventaR=round(amount_venta,2)+1
valor_compra=amount_compraR*compra
valor_venta=amount_ventaR*venta

contador_compras=0
contador_ventas=0


# EJEMPLO exchange.create_limit_buy_order(symbol,amount,price[,params])
print("pedido de venta")
#venta=binance.create_limit_sell_order(par,amount_ventaR,venta)
#contador_ventas=contador_ventas+1
#print("pedido de Venta GRABADO!!")

print("pedido de compra")
#compra=binance.create_limit_buy_order(par,amount_compraR,compra)
#contador_compras=contador_compras+1
#print("pedido de compra GRABADO")





ordenes_abiertas=exchange.fetch_open_orders(par)
#id_ordenes_abiertas=ordenes_abiertas[0]['info']['orderId']
#print("ORDEN ABIERTA N ", str(id_ordenes_abiertas))
ordenes_cerradas=exchange.fetch_closed_orders(par) # LISTADO ORDENES CERRADAS
#print("ORDEN CERRADA !!! ")

trades=exchange.fetch_my_trades(par)














#GUARDA JSON CON NUEVA POSICION

with open('MMmonedas.json', 'w') as f:
    json.dump(MMmonedas, f)








fin=time.time()
diferencia=round((fin-inicio),2)





print('\nESTE PROGRAMA A TARDADO {} SEGUNDOS EN TERMINAR'.format(diferencia))




