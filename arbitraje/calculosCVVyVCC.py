# -*- coding: utf-8 -*-
"""
Created on Mon May 27 23:46:12 2019

@author: MPAZ
"""

# VAMOS A IMPORTAR LA TABLA CON TRIANGULACION PARA DESPUES ENTRAR EN EXCHANGE Y CACULAR PROFIT EN CVV Y VVC
import ccxt
import claves
import numpy as np
from datetime import datetime
import time

# ABRE EL FICHERO Y LEE EL CONTENIDO
# MODIFICAR PARA CADA USO EL EXCHANGE A USAR Y EL FICHERO BASE CON LISTADO DE TRIANGULOS DE ARBITRAGE
# POR EJEMPLO BINANCE & binancemini.txt
# VAMOS A HACER PRIMERO SOLO  VCC CON STOCK DE ALGUNAS CRIPTOMONEDAS COMO LTC O SKY


# AÑADIMOS FUNCIONES DE FECHAS Y TIEMPOS PARA VER DONDE SE VA EL TIEMPO
ahora = datetime.now()
dia = ahora.strftime("%Y%m%d")

t0 = time.time()



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


casas_cambio = ccxt.exchanges

# binance=ccxt.binance()


mercados = exchange.load_markets(True)

monedas = exchange.currencies

simbolos = exchange.symbols

metodos = dir(exchange)

ganancias = []


'''
REALIZA LAS ORDENES DE COMPRA CVV O VCC DE FORMA CONTINUADA A VER SI ALGO GANA

FUN/BTC,ETH/BTC,FUN/ETH,11.94,-15.92
REQ/BTC,ETH/BTC,REQ/ETH,12.65,-10.03
POWR/ETH,BNB/ETH,POWR/BNB,12.58,-7.09
AMB/BTC,BNB/BTC,AMB/BNB,12.68,-18.3
AMB/ETH,BNB/ETH,AMB/BNB,14.06,-18.75
BCPT/ETH,BNB/ETHCPT/BNB,10.26,-10.28
CDT/BTC,ETH/BTC,CDT/ETH,11.29,-4.54

HACEMOS EJEMPLO CON PSEUDOCODIGO A COMPLETAR Y PROBAR CON SALDO REAL EN OREGON 


#SI PAR1 Q1 ES BTC O ETH, SI VA BIEN COMPRAR DE OTRAS TAMBIEN

'''

print("empezamos")


par1='SKY/BTC'
par2='BNB/BTC'
par3='SKY/BNB'

libro_ordenes1 = exchange.fetch_order_book(par1)
libro_ordenes2 = exchange.fetch_order_book(par2)
libro_ordenes3 = exchange.fetch_order_book(par3)

#PRIMERO CAMINO VCC

v1 = libro_ordenes1['bids'][0][0]
c2 = libro_ordenes2['asks'][0][0]
c3 = libro_ordenes3['asks'][0][0]

minimo_notional1 = (mercados)[
                par1]['info']['filters'][3]['minNotional']
notional1 = float(minimo_notional1) # CALCULA EL MINIMO NOTIONAL PARA CUADRAR Q
qmin1=notional1/v1   # CANTIDAD MINIMA COMPRA
qmin1aumentado=round(qmin1*1.2,8) #AUMENTA UN 20% DE SEGURIDAD
vv1=round(v1*qmin1aumentado,8) # REDONDEA A 8 DECIMALES

q2=round(vv1/c2,8) #CANTIDAD2
vc2=round(q2*c2,8) #VOLUMEN2

q3=round(q2/c3,8) #CANTIDAD3
vc3= round(c3*q3,8) #VOLUMEN3

resultadoVCCbruto=v1/(c2*c3)
resultadoVCC=round(resultadoVCCbruto*1000,2)
diferenciacirculoVCC=round(q3-qmin1aumentado,8)
porcentaVCC=round(diferenciacirculo/qmin1aumentado,4)

#SEGUNDO CAMINO CVV

c1 = libro_ordenes1['asks'][0][0]
v2 = libro_ordenes2['bids'][0][0]
v3 = libro_ordenes3['bids'][0][0]

qcmin1=notional1/c1
qcmin1aumentado=round(qcmin1*1.2,8)
vc1=round(c1*qcmin1aumentado,8)

qq3=round(qcmin1aumentado/v3,8)

qq2=round(qq3*v2,8)

diferenciacirculoCVV=round(qq2-qcmin1aumentado,4)
porcentajeCVV=round(diferenciacirculoCVV/qcmin1aumentado,4)

