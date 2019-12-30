# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 23:32:49 2019

@author: MPAZ
"""



import pandas as pd
import requests
import time
import shelve

shelfFile=shelve.open('variables')

jugores=shelfFile['jugores']
simbolos=[]

def convierte(par):
    a=par.split('/')[0]
    b=par.split('/')[1]
    c=a+b
    return c

for i in jugores:
    print (i)
    simbolo=convierte(i)
    simbolos.append(simbolo)


#pares=['ADABTC','ADAETH']

pares=simbolos[20:25]

mega={}




#par='ADABTC'


def get_order(symbol):
    url = 'https://api.binance.com/api/v1/trades?symbol={}&limit=1000'.format(
        symbol)
    data = requests.get(url).json()
    df = pd.DataFrame(data)
    return df


#df = get_order(par)


def ordenar(df):
    df['time'] = pd.to_datetime(df.time, unit="ms")
    df = df.drop(['isBestMatch', 'isBuyerMaker'], axis=1)
    df['price'] = pd.to_numeric(df['price'])
    df['qty'] = pd.to_numeric(df['qty'])
    df['quoteQty'] = pd.to_numeric(df['quoteQty'])
    return df


#df = ordenar(df)


def ordenar2(df):

    df = df.set_index('time')
    ordenes = df['id'].resample('1min').count()
    minimo = df['price'].resample('1min').min()
    maximo = df['price'].resample('1min').max()
    media = df['price'].resample('1min').mean()
    baseqty = df['qty'].resample('1min').sum()
    quoteqty = df['quoteQty'].resample('1min').sum()
    series = [pd.Series(ordenes), pd.Series(minimo), pd.Series(maximo), pd.Series(media),
              pd.Series(baseqty), pd.Series(quoteqty)]
    df2 = pd.DataFrame(series)
    df3 = df2.T
    df3.columns = ['ordenes', 'minimo', 'maximo', 'media', 'qty', 'quoteQty']
    df3['volatilidad'] = round(
        (df3['maximo'] - df3['minimo']) / df3['minimo'] * 100, 1)
    df3 = df3.reset_index()
    return df3


#df = ordenar2(df)


for par in pares:
    paso1=get_order(par)
    paso2=ordenar(paso1)
    paso3=ordenar2(paso2)
    
    mega[par]=paso3



def make_csv(df):
    
    df2 = get_order(par)
    df2 = ordenar(df2)
    df2 = ordenar2(df2)
    df3 = df.append(df2)
    df3 = df3.drop_duplicates(subset='time', keep='last')
    df3.to_csv('binance' + str(par) + '.csv')
    print('fichero' + str(par) + 'grabado')
    return df3


for i in range(1000):
    
    time.sleep(600)
    print ('ciclo numero ' + str(i))
    for par in pares:
        nuevodf=make_csv(mega[par])
        mega[par]=nuevodf







