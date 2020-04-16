

# -*- coding: utf-8 -*-
"""
Created on Mon Dec 16 23:14:53 2019

@author: MPAZ

PASO 2

SE CONECTA A BINANCE, TOMA LAS ORDENES DE LOS PARES SELECCIONADOS EN PASO 1
 Y LO EXPORTA CADA 5 MINUTOS EN UN CSV

(DESPUES VENDRA LA LOGICA DE ACCION)

"""

import requests
import pandas as pd
from datetime import date
from datetime import datetime
import time
import shelve



def ordenes_binance(par):
    ''' EXTRAE DE BINANCE LAS ULTIMAS 1000 ORDENES DE 1 PAR'''
    url_binance = 'https://api.binance.com/api/v1/'
    url = url_binance + 'trades?symbol={}&limit=1000'.format(par)
    datos = requests.get(url).json()
    df = pd.DataFrame(datos)
    return df

def ordenar_df1(df):
    ''' TOMA LAS ORDENES DE BINANCE Y LAS AGRUPA ORDENADAMENTE'''
    df.drop(['isBuyerMaker', 'isBestMatch'],
            axis='columns', inplace=True)  # BORRA COLUMNAS
    df.columns = ['id', 'precio', 'cant',
                  'coste', 'timestamp']  # ORDENA COLUMNAS
    df['fecha'] = pd.to_datetime(df['timestamp'], unit='ms')
    columnas2 = ['timestamp', 'fecha', 'id', 'precio', 'cant', 'coste']
    df = df[columnas2]
    df['precio'] = df['precio'].astype(float)  # ASIGNA FORMATOS A COLUMNAS
    df['cant'] = df['cant'].astype(float)
    df['coste'] = df['coste'].astype(float)
    return df



db = shelve.open('tablas')

pares2 = db['pares_vivos']

db.close()



pares = []

for par in pares2:
    duo = par.split('/')
    union = duo[0] + duo[1]
    pares.append(union)


# pares=['ADAUSDT','ATOMBTC']

mega = {}


for par in pares:

    try:

        # df=mega[par]  ¿no seria al reves y al final?

        df = ordenes_binance(par)
        df = ordenar_df1(df)

        hoy = date.today()
        año, mes, dia = hoy.year, hoy.month, hoy.day
        nombre = str(año) + '-' + str(mes) + '-' + \
            str(dia) + '_' + par + '.csv'
        # ruta='C:\RMB_v2\\ficheros\\'+nombre
        ruta = nombre
        df.to_csv(ruta)
        print('Grabado fichero ' + ruta)

        mega[par] = df

    except:
        print('fallo en par' + par)


while True:

    for par in pares:

        try:

            print('A dormir 30 segundos')
            time.sleep(30)
            print('Al ataque!!!')
            df = mega[par]
            ultima_orden = df['id'].iloc[-1]

            # MIRA A VER QUE MOMENTO ES PARA QUITAR LO QUE TENGA MAS DE 24 HORAS
            now = datetime.now()
            timestamp = datetime.timestamp(now)
            timestamp2 = round(timestamp * 1000, 0)
            dia = 1000 * 60 * 60 * 24
            solucion = timestamp2 - dia

            df2 = ordenes_binance(par)
            df2 = ordenar_df1(df2)

            df2 = df2[(df2['timestamp'] > solucion)]
            df2 = df2[(df2['id'] > ultima_orden)]
            df = df.append(df2)

            hoy = date.today()
            año, mes, dia = hoy.year, hoy.month, hoy.day

            nombre = str(año) + '-' + str(mes) + '-' + \
            str(dia) + '_' + par + '.csv'

            # ruta='C:\RMB_v2\\ficheros\\'+nombre
            ruta = nombre

            df.to_csv(ruta)
            print(datetime.now())
            print('Grabado fichero par' + par + ruta)

        except:
            print('Fallo en el par ' + par)
