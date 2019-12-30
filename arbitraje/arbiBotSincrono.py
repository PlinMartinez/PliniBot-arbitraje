# -*- coding: utf-8 -*-
"""
Created on Sat May 25 14:56:15 2019

@author: MPAZ
"""

# VAMOS A IMPORTAR LA TABLA CON TRIANGULACION PARA DESPUES ENTRAR EN EXCHANGE Y CACULAR PROFIT EN CVV Y VVC
import ccxt
import claves
import numpy as np
from pprint import pprint as prety

# ABRE EL FICHERO Y LEE EL CONTENIDO
# MODIFICAR PARA CADA USO EL EXCHANGE A USAR Y EL FICHERO BASE CON LISTADO DE TRIANGULOS DE ARBITRAGE
# POR EJEMPLO BINANCE & binancemini.txt
# VAMOS A HACER PRIMERO SOLO  VCC CON STOCK DE ALGUNAS CRIPTOMONEDAS COMO LTC O SKY

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


mercados = exchange.load_markets(True)

monedas = exchange.currencies

simbolos = exchange.symbols


'''
REALIZA LAS ORDENES DE COMPRA CVV O VCC DE FORMA CONTINUADA A VER SI ALGO GANA

FUN/BTC,ETH/BTC,FUN/ETH,11.94,-15.92
REQ/BTC,ETH/BTC,REQ/ETH,12.65,-10.03
POWR/ETH,BNB/ETH,POWR/BNB,12.58,-7.09
AMB/BTC,BNB/BTC,AMB/BNB,12.68,-18.3
AMB/ETH,BNB/ETH,AMB/BNB,14.06,-18.75
BCPT/ETH,BNB/ETHCPT/BNB,10.26,-10.28
CDT/BTC,ETH/BTC,CDT/ETH,11.29,-4.54

CREAMOS CODIGO EN BASE A OPERACION VCC ENTRE
SKY/ETH = BNB/ETH x SKY/BNB

#SI PAR1 Q1 ES BTC O ETH, SI VA BIEN COMPRAR DE OTRAS TAMBIEN

'''

par1 = ('SKY/ETH')
par2 = ('BNB/ETH')
par3 = ('SKY/BNB')

libro1 = exchange.fetch_order_book(par1)
libro2 = exchange.fetch_order_book(par2)
libro3 = exchange.fetch_order_book(par3)
altobid1=libro1['bids'][0][0]
bajoask1=libro1['asks'][0][0]
altobid2=libro2['bids'][0][0]
bajoask2=libro2['asks'][0][0]
altobid3=libro3['bids'][0][0]
bajoask3=libro3['asks'][0][0]

#LANZA PAR 1 MEDIANTE CALCULOS ESPECIFICOS CALCULAR GASTAR 1,2 MIN NOTIONAL

min_notional1 = exchange.markets[par1]['info']['filters'][3]['minNotional']
notional1 = float(min_notional1)
minimovolumenventa = notional1 / altobid1
minimosubido20 = minimovolumenventa * 1.5
minimoajustado = round(minimosubido20, 8)
cantidadventa1ajustado=notional1/altobid1
cantidadventa1subido20=cantidadventa1ajustado*1.5
cantidad_venta1=round(cantidadventa1subido20,8)
valor_venta1=cantidad_venta1*altobid1

print('voy a lanzar el pedido 1')
symbol1 = par1
type1 = 'market'
side1 = 'sell'
amount1 = minimoajustado
#venta1=exchange.create_order(symbol1,type1,side1,amount1)
print('hecho el paso 1 V')

print('voy a lanzar el pedido 2')

consulta_venta1=exchange.fetch_orders(par1)[-1]
q2_por_gastar=consulta_venta1['cost']
amount2provisional=q2_por_gastar/bajoask2
amount2r=round(amount2provisional,8)
valor_compra2=amount2r*bajoask2

symbol2= par2
type2='market'
side2='buy'
amount2=amount2r
#compra2=exchange.create_order(symbol2,type2,side2,amount2)
print('hecho el paso 2 !!!')

# AHORA TOCA EL PAR3 FINALMENTE...

print('Empiezo la ultima orden numero 3 para cerrar circulo')

consulta_compra2=exchange.fetch_orders(par2)[-1]
b3_comprado=consulta_compra2['amount']
cantidad_compra3=b3_comprado/bajoask3
cantidad_compra3r=round(cantidad_compra3,8)
valor_compra3=cantidad_compra3r*bajoask3

symbol3=par3
type3='market'
side3='buy'
amount3=cantidad_compra3r
#compra3=exchange.create_order(symbol3,type3,side3,amount3)
print('ya esta por fin')

consulta_compra3=exchange.fetch_orders(par3)[-1]
