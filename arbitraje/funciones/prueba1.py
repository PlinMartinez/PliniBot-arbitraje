# -*- coding: utf-8 -*-
"""
Created on Thu May 30 23:22:34 2019

@author: MPAZ
"""

# VAMOS A IMPORTAR LA TABLA CON TRIANGULACION PARA DESPUES ENTRAR EN EXCHANGE Y CACULAR PROFIT EN CVV Y VVC
import ccxt
import claves
import pandas as pd
import numpy as np
import sys

# EDICION 1.1 CAMBIO 22/5 QUE INSTANCIE EL SERVIDOR QUE TOCA
# FALTARA DEPURAR ERRORES MÁS ADELANTE Y GRABAR INFO QUE SEA UTIL

# ABRE EL FICHERO Y LEE EL CONTENIDO
# MODIFICAR PARA CADA USO EL EXCHANGE A USAR Y EL FICHERO BASE CON LISTADO DE TRIANGULOS DE ARBITRAGE
# POR EJEMPLO BINANCE & binancemini.txt

# NECESITA UNA TABLA PRIMERO DE TRIANGULOS PARA FUNCIONAR !!!




nombre = 'bitbank'

#exchange = ccxt.binance({'enableRateLimit': True, })

id = nombre
exchange_class = getattr(ccxt, id)
exchange = exchange_class({'timeout': 3000, 'enableRateLimit': True, })
mercados = exchange.load_markets(True)




filename = nombre + 'arbitraje.txt'

file = open(filename, mode='r')
text = file.read()
file.close()
print(text)

# ABRE EL FICHERO Y LO TOMA COMO MATRIZ DE A x B FILAS / COLUMNAS

data = np.loadtxt(filename,
                  delimiter='-',
                  usecols=[0, 1, 2],
                  dtype=str)

print(data)
print(type(data))

print(data.shape)
print(data[1, 0])
print(data[1, 1])
print(data[1, 2])

filas = data.shape[0]
columnas = data.shape[1]

print('Tienes una matriz de ' + str(filas) + "x" + str(columnas))

casas_cambio = ccxt.exchanges

# binance=ccxt.binance()

mercados = exchange.load_markets(True)

monedas = exchange.currencies

simbolos = exchange.symbols

metodos = dir(exchange)

beneficio = []

print("empezamos")

for i in range(0, filas):

    par1 = data[i - 1, 0]
    par2 = data[i - 1, 1]
    par3 = data[i - 1, 2]
    print(par1)
        
    mercados = exchange.load_markets(True)
  

    pc1 = exchange.fetch_order_book(par1)['asks'][0][0]
    pv1 = exchange.fetch_order_book(par2)['bids'][0][0]
    pc2 = exchange.fetch_order_book(par3)['asks'][0][0]
    pv2 = exchange.fetch_order_book(par1)['bids'][0][0]
    pc3 = exchange.fetch_order_book(par3)['asks'][0][0]
    pv3 = exchange.fetch_order_book(par3)['bids'][0][0]
    
    notional1=0.01

    r1=pc2*pc3*notional1/pv1
    beneficioVCC=notional1-r1
    beneficioVCCporcentaje=beneficioVCC/notional1
    beneficiofinalVCC=round(beneficioVCCporcentaje*100,2)
    
    notional2=notional1

    r2=pv2*pv3*notional2/pc1
    beneficioCVV=notional1-r2
    beneficioCVVporcentaje=beneficioCVV/notional2
    beneficiofinalCVV=round(beneficioCVVporcentaje*100,2)
        


    print(str(par1) + '-' + str(par2) + '-' + str(par3) +
          ' en modo VCC y CVV da sobre 1.000 unidades de base1')
    print(str(beneficiofinalVCC) + "  " + str(beneficiofinalCVV))
    if beneficioCVV > 1:
        print('OJO, OPORTUNIDAD DE GANAR UN 1% CVV')
        beneficio.append(par1 + ',' + par2 + ',' + par3 +
                         ',' + str(beneficioVCC) + ',' + str(beneficioCVV))

    if beneficioVCC > 1:
        print('OJO, OPORTUNIDAD DE GANAR UN 1% EN MODO VCC')
        beneficio.append(par1 + ',' + par2 + ',' + par3 +
                         ',' + str(beneficioVCC) + ',' + str(beneficioCVV))
