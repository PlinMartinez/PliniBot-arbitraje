# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 15:22:31 2020

se conecta a kraken y va bajando + guardando todas las ordenes de varios pares

@author: MPAZ

"""
import requests
import pandas as pd
import time
import datetime


inicio = datetime.datetime.now()
fin = inicio + datetime.timedelta(minutes=1, hours=0)


def pares():

    url_pares = 'https://api.kraken.com/0/public/AssetPairs'
    pares = requests.get(url_pares).json()['result']
    return pares


pares = pares()


par1 = 'XETHXXBT'


def operaciones_recientes(par):
    '''EXTRAE ULTIMAS OPERACIONES DE UN PAR EN KRAKEN'''
    url_operaciones = 'https://api.kraken.com/0/public/Trades?pair=' + par
    operaciones_recientes = requests.get(url_operaciones).json()['result']
    return operaciones_recientes


operaciones = operaciones_recientes(par1)[par1]


def pasar_df(operaciones):
    '''CONVIERTE EL DICCIONARIO EN DF PARA OBTENER LA INFO UTIL AGRUPADA'''
    df = pd.DataFrame(operaciones)
    df.columns = ['precio', 'cantidad',
                  'timestamp', 'compra_venta', 'tipo', '6']
    df = df.drop(columns='6')
    df['timestamp'] = pd.to_datetime(df['timestamp'], unit='s')
    return df


print('primer ciclo')
df = pasar_df(operaciones)
ultima_orden = df['timestamp'].iloc[-1]
filename = 'kraken.txt'
df.to_csv(filename, mode='a', header='column_names')
print('fichero par', par1, 'grabado con exito!')


print('a dormir un poquito')
time.sleep(10)

ahora = datetime.datetime.now()


while ahora < fin:

    print('a dormir un poquito')
    time.sleep(15)
    print('segundo ciclo continuo')
    operaciones = operaciones_recientes(par1)[par1]
    df2 = pasar_df(operaciones)
    df2 = df2[(df2['timestamp'] > ultima_orden)]
    try:
        ultima_orden = df2['timestamp'].iloc[-1]
        df2.to_csv(filename, mode='a', header='column_names')
        print('fichero par', par1, 'grabado ok en siguiente ronda')

    except:
        print('no hay + ordenes recientes para grabar')

    ahora = datetime.datetime.now()
