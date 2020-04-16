# -*- coding: utf-8 -*-
"""
Created on Sun Dec 29 21:29:19 2019

@author: MPAZ

MIRA TODOS LOS PARES DE UN EXCHANGE Y CLASIFICA

SI LAS ULTIMAS 500 ORDENES HECHAS > 24 HORAS EL MERCADO ESTA MUERTO
SI LAS ULTIMAS 500 ORDENES HECHAS < 1 DIA EL MERCADO ESTA VIVO Y SE PUEDE NAVEGAR

Pasa a Shelve estos 2 listados para futuros trabajos
pares_vivos_velocidad
pares_muertos_velocidad
SACA LOS OHLCV de cada par y agrupa
si volatilidad <1% >> mercado mueto
si volatlidad >3% >> mercado jugoso

"""

import ccxt
import time
import shelve
import pandas as pd

binance = ccxt.binance()   # INSTANCIA BINANCE

mercados = binance.load_markets()  # CARGA MERCADOS

pares = binance.symbols  # SACA LISTA PARES


''' ESTA PARTE ES DE DEBUGGING UNITARIO'''

# ZONA DE DEPURACION, DESPUES cambiar mini_pares por pares

mini_pares = pares[0:3]
# SACA TIEMPO DE VENTA 500 ORDENES DESDE LIBRO DE ORDENES DE UN PAR
ordenes = binance.fetch_trades(mini_pares[1])
primero = ordenes[0]['timestamp']  # TIEMPO PRIMERA ORDEN
ultimo = ordenes[-1]['timestamp']  # TIEMPO ULTIMA ORDEN
delay = ultimo - primero  # DIFERENCIA EN ms
retraso = round(delay / (1000 * 60 * 60), 1)  # CONVIERTE A DIAS


ohlcv = binance.fetch_ohlcv(mini_pares[1], '1d')
df = pd.DataFrame(ohlcv)
df.columns = ['time', 'open', 'high', 'low', 'close', 'volume']
df['time'] = pd.to_datetime(df['time'], unit='ms')
df = df.set_index('time')
df['volatilidad'] = round((df['high'] - df['low']) / df['low'] * 100, 1)
ayer = df['volatilidad'][-2]

velocidad_pares = {}

for par in pares:
    ''' METE EN DICCIONARIO EL NUMERO DIAS / PAR ULTIMAS 500 ORDENES
          {'ADA/BNB': 1.6, 'ADA/BTC': 0.4, 'ADA/BUSD': 13.0}'''
    try:
        print('Revisamos la velodidad del par ' + par)
        ordenes = binance.fetch_trades(par)
        primero = ordenes[0]['timestamp']
        ultimo = ordenes[-1]['timestamp']
        delay = ultimo - primero
        retraso = round(delay / (1000 * 60 * 60), 1)
        velocidad_pares[par] = retraso
        print('La velocidad del par ' + par + 'es de ' + retraso)
        time.sleep(1)
    except:
        print('el par este ha salido chungo' + str(par))


''' GENERA LISTAS PARES VIVOS Y MUERTOS '''
pares_vivos_velocidad = []
pares_muertos_velocidad = []

for clave, valor in velocidad_pares.items():
    if valor <= 1:
        pares_vivos_velocidad.append(clave)
    if valor > 1:
        pares_muertos_velocidad.append(clave)

''' GUARDA EN SHELVE LOS RESULTADOS PARA SIGUIENTES SCRIPTS'''
obj = shelve.open('tablas')
obj['velocidad_pares'] = velocidad_pares
obj['pares_vivos_velocidad'] = pares_vivos_velocidad
obj['pares_muertos_velocidad'] = pares_muertos_velocidad
# obj.close


volatilidad = {}

for par in pares:

    ''' SACA VOLATILIDAD DIARIA DESDE CCXT
    {'ADA/BNB': 15.1, 'ADA/BTC': 15.1, 'ADA/BUSD': 15.3}'''

    try:

        print('Empezamos a mirar OHLCV con el par ' + par)
        ohlcv = binance.fetch_ohlcv(par, '1d')
        df = pd.DataFrame(ohlcv)
        df.columns = ['time', 'open', 'high', 'low', 'close', 'volume']
        df['time'] = pd.to_datetime(df['time'], unit='ms')
        df = df.set_index('time')
        df['volatilidad'] = round(
            (df['high'] - df['low']) / df['low'] * 100, 1)
        ayer = df['volatilidad'][-2]
        volatilidad[par] = ayer
        time.sleep(1)
    except:

        print('el par ' + par + 'ha fallado')


pares_vivos_amplitud = []
pares_muertos_amplitud = []

for clave, valor in volatilidad.items():
    if valor < 1:
        pares_muertos_amplitud.append(clave)
    if valor > 3:
        pares_vivos_amplitud.append(clave)


#obj = shelve.open('tablas')
obj['pares_vivos_amplitud'] = pares_vivos_amplitud
obj['pares_muertos_amplitud'] = pares_muertos_amplitud
# obj.close


pares_vivos = []

for item in pares_vivos_velocidad:
    print(item)
    if item in pares_vivos_amplitud:
        pares_vivos.append(item)

#obj = shelve.open('tablas')
obj['pares_vivos'] = pares_vivos
obj.close

print('La lista de pares vivos es la siguiente ' + str(len(pares_vivos)))
print(pares_vivos)
