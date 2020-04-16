# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 09:39:13 2020

CONVIERTE EN FUNCIONES TODAS LAS UTILIDADES DE LA API PUBLICA KRAKEN

@author: MPAZ
"""

import requests
import pandas as pd

def hora():
    '''RETORNA LA HORA DEL SERVIDOR'''
    
    url_hora='https://api.kraken.com/0/public/Time'
    hora=requests.get(url_hora).json()['result']
    print(hora)
    return hora

hora_kraken=hora()

def guarda_tabla_activos(funcion):
    '''DECORADOR PARA EXPORTAR LISTA ACTIVOS'''
    activos=funcion()
    df=pd.DataFrame(activos).T
    df.to_csv('activos_kraken')
    print('Grabado fichero activos_kraken.csv')

@guarda_tabla_activos
def lista_activos():
    'DEVUELVE LISTA DE ACTIVOS QUE TRADEA EL EXCHANGE'''
    
    url_activo='https://api.kraken.com/0/public/Assets'
    activos=requests.get(url_activo).json()['result']
    return activos

def pares():
    '''DEVUELVE LISTA DE PARES CON SUS DETALLES DE USO'''
    
    url_pares='https://api.kraken.com/0/public/AssetPairs'
    pares=requests.get(url_pares).json()['result']
    return pares

pares=pares()

def par_uno(par):
    
    '''DEVUELVE SOLO UN LOS DATOS DE UN PAR QUE LE PASAS COMO PARAMETRO'''
    
    url_par='https://api.kraken.com/0/public/AssetPairs?pair='+par
    par=requests.get(url_par).json()['result']
    return par

par_ADAETH=par_uno('ADAETH')
    
par1='ADAETH'

def ticker(par):
    
    '''<pair_name> = nombre del par
    a = array de ofertas(<precio>, <lote completo de volumen>, <lote del volumen>),
    b = array de demandas(<precio>, <lote completo de volumen>, <lote del volumen>),
    c = array de últimas operaciones(trades) cerradas(<precio>, <lote del volumen>),
    v = array de volumen(<hoy>, <últimas 24 horas>),
    p = array del precio promedio ponderado por volumen(<hoy>, <últimas 24 horas>),
    t = array de número de operaciones(<hoy>, <últimas 24 horas>),
    l = array de mínimos(<hoy>, <últimas 24 horas>),
    h = array de máximos(<hoy>, <últimas 24 horas>),
    o = precio de apertura para hoy
    '''
    url_ticker='https://api.kraken.com/0/public/Ticker?pair='+par
    ticker=requests.get(url_ticker).json()['result']
    return ticker

ticker=ticker(par1)


def libro_ordenes(par):
    '''devuelve el libro de ordenes'''
    url_libro_ordenes='https://api.kraken.com/0/public/Depth?pair='+par
    libro_ordenes_par=requests.get(url_libro_ordenes).json()['result']
    return libro_ordenes_par

libro_ADA=libro_ordenes(par1)


def operaciones_recientes(par):
    ''' Devuelve las ultimas operaciones hechas de un par'''
    url_operaciones='https://api.kraken.com/0/public/Trades?pair='+par
    operaciones_recientes=requests.get(url_operaciones).json()['result']
    return operaciones_recientes

operaciones_ADA=operaciones_recientes(par1)


































