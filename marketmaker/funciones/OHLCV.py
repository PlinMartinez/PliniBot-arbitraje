# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 23:41:20 2019

@author: MPAZ

toma OHLCV de un par y busca info de interes
mide el mercado su fuerza antes de ver a cual zumbarle y sacarle beneficio

O:open
H:high
L:low
C:close
V:Volumen

en 7 días ¿variacion de precio? buscar poca variacion, 
si sube comprar barato
si baja vender caro
si centro mucho market maker al 1%

volatilidad: marca el entrar en market maker o si es oceano en calma no entrar

velocidad mercado: a que velocidad se mueven los segundos??

volumen mercado: ¿estamos entre peces o hay ballenas en medio?

humanos o maquinas: ¿maker o buy market?

numero de picos al día: +/-1% cuantas veces en 24 horas >>> grabar un fichero
par.fecha: hora:minuto: >>> 60 minutos x 24 horas >>> ADA/ETH20190602.csv
fichero/par >>> genera estrategia dia siguiente>>>
numero de picos, media, mediana , momento entrar, momento salir 

"""

import ccxt
import claves
import pprint
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

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



#mercado de pares con caracteriistcas
mercados=exchange.load_markets(True)

#listado de pares
pares_lista=list(exchange.markets.keys())

#listado de MONEDAS  
monedas=exchange.currencies

#CONSULTAR BALANCE
balances=exchange.fetch_balance()

moneda1='ADA'
moneda2='ETC'
moneda3='BTC'

par1='ADA/ETH'
par2='ETH/BTC'

simbolos = exchange.symbols
simbolos_mini=simbolos[10:25]
vol_pares=[]


saldos=exchange.fetch_free_balance()

'''
def volatilidad(symbol=None):
    #print("empezamos")
    ohlcv=exchange.fetch_ohlcv(symbol,'1d')
    df = pd.DataFrame(ohlcv,columns=['Fecha',
                                     'Open',
                                     'High',
                                     'Lowest',
                                     'Closing',
                                     'Volumen'])
    df['Fecha'] = pd.to_datetime(df['Fecha'], unit='ms')
    col_list=list(df)
    df['Volatilidad'] = df['High'] - df['Lowest'] 
    df['%']=df['Volatilidad'] / df['Open'] * 100
    df['%']=df['%'].round(decimals=1)
    volatilidad=df.iloc[-1,-1]
    miniserie=df['%'][-7:]
    #print (df)
    print(symbol,'tiene hoy una volatilidad de  ',volatilidad, ' %')
    resultado=volatilidad
    return resultado

volatilidad=volatilidad(par1)
'''

par='ETH/BTC'
symbol='ADA/BTC'
#print("empezamos")
ohlcv=exchange.fetch_ohlcv(par,'1d')
df = pd.DataFrame(ohlcv,columns=['Fecha',
                                 'Open',
                                 'High',
                                 'Lowest',
                                 'Closing',
                                 'Volumen'])
df['Fecha'] = pd.to_datetime(df['Fecha'], unit='ms')
col_list=list(df)
df['Volatilidad'] = df['High'] - df['Lowest'] 
df['%']=df['Volatilidad'] / df['Open'] * 100
df['%']=df['%'].round(decimals=1)
volatilidad=df.iloc[-1,-1]
miniserie=df['%'][-7:]
#print (df)

print('\n')
print(par,'tiene hoy una volatilidad de  ',volatilidad, ' %')

titulo='VOLATILIDAD ULTIMA SEMANA  ' +str(par)
plt.title(titulo)
plt.plot(miniserie,'g')
plt.xlabel('DIAS ULTIMA SEMANA')
plt.ylabel('%VOLATILIDAD PRECIO DIARIA')
plt.axhline(3,color='r') # POR DEBAJO DE AQUI MERCADO EN CALMA
#plt.ylim(0,10)
plt.axhspan(5,6,alpha=0.25,color='green')
plt.legend()
plt.show()

open=df.iloc[-7,1]
cierre=df.iloc[-1,-4]
variacion_semanal_precio=round((cierre-open)/open*100,2)

'''


# SACA VOLATILIDADES DE TODOS LOS MERCADOS
for i in simbolos_mini:
    suma=volatilidad(i)
    vol_pares.append(suma)

d=dict(zip(simbolos_mini,vol_pares))
print (d)
dfichero=str(d)

#METODO 1
f = open("volatilidades.txt", "w")
f.write(dfichero)
f.close()

#METODO 2

f = open("volatilidades2.csv", "w")
f.write("Par")
f.write(",")
f.write("Volatilidad")
f.write("\n")
for (clave, valor) in d.items():
    print(clave, ",", valor)
    f.write(str(clave))
    f.write(",")
    f.write(str(valor))
    f.write("\n")

f.close()

vol_pares2=vol_pares[10:25]
plt.plot(simbolos_mini,vol_pares2)
plt.ylim(0,20)
plt.title('Volatilidad algunos cambios')
plt.axhline(3,color='r')
plt.show()


plt.figure('VOLATILIDAD DE CAMBIO ADA/ETH')
plt.title('VOLATILIDAD ADA/ETH')
plt.plot(miniserie,'g')
plt.xlabel('DIAS ULTIMA SEMANA')
plt.ylabel('%VOLATILIDAD PRECIO DIARIA')
plt.axhline(3,color='r')
#plt.ylim(0,10)
plt.axhspan(5,6,alpha=0.25,color='green')
plt.legend()
plt.show()
'''


ordenes_cerradas=exchange.fetch_closed_orders(par,25,50)
numero_ordenes_cerradas_par1=len(ordenes_cerradas)
ordenes_abiertas=exchange.fetch_open_orders(par)
numero_ordenes_abiertas=len(ordenes_abiertas)
libro_ordenes=exchange.fetch_order_book(par)
registro_ordenes=exchange.fetch_my_trades(par)
ohlcv=exchange.fetch_ohlcv(par,'1d')

prueba=exchange.fetch_ticker(par)


recent_trades=exchange.






