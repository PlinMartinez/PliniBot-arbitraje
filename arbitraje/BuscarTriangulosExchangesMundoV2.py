# -*- coding: utf-8 -*-
"""
Created on Mon May 27 22:07:25 2019

@author: MPAZ

BUSCA TODOS LOS TRIANGULOS DEL MUNDO EN TODOS LOS EXCHANGES EXCEPTO LOS LARGOS

LA FUNCION ADEMAS DEBE IMPRIMIR EL NOMBRE PARA SABER POR QUE PASO VA

¿AÑADIR CONTADOR PARA CORTAR?


"""
import pandas as pd
import numpy as np

# Tabla con exchanges y pares por exchange
# likke,255  ...

filename = 'listamundialexchanges.txt'


df = pd.read_csv(filename, sep=",", header=None)
df.columns = ["exchange", "num_pares"]


df2=df.loc[df['num_pares'] <=515]


grabar=df2.to_csv('exchangesmundopequeños2.txt', header=None, index=None, sep=',', mode='a')