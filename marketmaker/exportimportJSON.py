import json
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

ASIGNAMOS SALDO 10 LEYENDO CON PICKLE SI BAJA A 5 DEJA DE COMPRAR 
SI SUBE A 15 DEJA DE VENDER +-1%

CADA 15 MINUTOS BORRA TODOS LOS PEDIDSO Y CREA NUEVOS
"""


import ccxt
import claves
import time


inicio = time.time()

# ACCESAR A BINANCE
usuario = claves.api_key
clave = claves.secret

# instancia mediante id a Binance con claves
exchange_id = 'binance'
exchange_class = getattr(ccxt, exchange_id)
binance = exchange_class({
    'apiKey': usuario,
    'secret': clave,
    'timeout': 30000,
    'enableRateLimit:': True,
})

mercados = binance.load_markets(True)

monedas = binance.currencies

Vmonedas = binance.currencies.keys()

metodos = dir(binance)

print("empezamos")


print(Vmonedas)

MMmonedas = {}

for i in Vmonedas:
    MMmonedas[i] = 10

print(MMmonedas)



with open('MMmonedas.json', 'w') as f:
    json.dump(MMmonedas, f)

'''
with open('MMmonedas.json') as f:
    data = json.load(f)

print(data)

print(data['ETH'])
'''