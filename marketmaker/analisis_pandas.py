# -*- coding: utf-8 -*-
"""
Created on Sun May  5 21:12:35 2019

@author: MPAZ
"""

import pandas as pd 
 
df=pd.read_csv("volatilidades2.csv")
#print (df)
print (df.dtypes)

print (df.sort_values(by=['Volatilidad'],ascending=[False]))

df2=df.sort_values(by=['Volatilidad'],ascending=[False])

df3 = df2[df2['Volatilidad'] > 5]

df4= df3[df3['Volatilidad']<20]


print(df4)