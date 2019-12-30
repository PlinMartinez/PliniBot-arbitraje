# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 22:44:29 2019

@author: MPAZ

SACA COMPRAS Y VENTAS AL MINUTO DE LISTA ORDENES HECHAS PARA VER QUIEN SE LLEVA LA PASTA...


"""

import requests        # for making http requests to binance
import json            # for parsing what binance sends back to us
import pandas as pd    # for storing and manipulating the data we get back
import numpy as np     # numerical python, i usually need this somewhere
# and so i import by habit nowadays

import matplotlib.pyplot as plt  # for charts and such

import datetime as dt  # for dealing with times


root_url = 'https://api.binance.com'
api_end_point='/api/v1/trades'
par='ADABTC'
url = root_url + api_end_point+ '?symbol=' + par 
data = json.loads(requests.get(url).text)

df = pd.DataFrame(data)
df.columns = ['id','isBestMatch','isBuyerMaker',
              'price', 'qty', 'quoteQty', 'time']

df2=pd.DataFrame(data,columns=['time','price',
                               'qty', 'quoteQty', 
                               'isBuyerMaker'])

df2['time'] = pd.to_datetime(df2['time'], unit='ms')
formato_hora = "%H:%M"

df2['año']=df2.time.dt.year
df2['mes']=df2.time.dt.month
df2['dia']=df2.time.dt.day
df2['hora']=df2.time.dt.hour
df2['minuto']=df2.time.dt.minute
df2['segundo']=df2.time.dt.second
df2[['price','qty']]=df2[['price','qty']].astype(float)
df3=df2.groupby(['minuto'])[['qty']].sum()

#df.index = [dt.datetime.fromtimestamp(x/1000.0) for x in df.time]

#print (df)

print(df.head())

print(df.tail())

print(df2)
print(df2.info())
print(df2.describe())
print('final')
print(df3)


