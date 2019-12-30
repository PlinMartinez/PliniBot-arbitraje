# -*- coding: utf-8 -*-
"""
Created on Sun Apr 28 17:45:10 2019

@author: MPAZ
"""
import ccxt
import claves
from datetime import datetime
import time





#ACCESAR A BINANCE
usuario=claves.api_key
clave=claves.secret


#instancia mediante id a Binance con claves 
exchange_id= 'binance'
exchange_class = getattr(ccxt, exchange_id)
binance= exchange_class({
	'apiKey':usuario,
	'secret':clave,
	'timeout':30000,
	'enableRateLimit:': True,
})

mercados=binance.load_markets(True)

monedas= binance.currencies

metodos=dir(binance)

print("empezamos")


par='DENT/ETH' # EMPEZAMOS CON ESTA

#SACA INFORMACION DE PEDIDOS ABIERTOS , DE MOMENTO TRABAJAMOS CON SOLO 1
try:
    
    pedidos_abiertos=binance.fetch_open_orders(par)# OJO AÑADIR SIMBOLO
    pedido_fecha=pedidos_abiertos[0]['datetime']
    pedido_id=pedidos_abiertos[0]['id']
    pedido_lado=pedidos_abiertos[0]['side']
    pedido_par=pedidos_abiertos[0]['symbol']
    pedido_precio=pedidos_abiertos[0]['price']
    pedido_timestamp=pedidos_abiertos[0]['timestamp']
    pedido_timestamp2=float(pedido_timestamp)
    pedido_timestamp3=pedido_timestamp/1000
#GRABA A FICHERO LOS PEDIDOS ABIERTOS, REALMENTE ESTO ES UTIL CON LOS CERRADOS
except:
    print('esta parte fallo')

f = open("pedidosabiertos.csv", "w")
f.write("Fecha")
f.write(",")
f.write("id")
f.write(",")
f.write("lado")
f.write(",")
f.write("par")
f.write("\n")

'''
f.write(pedido_fecha)
f.write(",")
f.write(pedido_lado)

f.close()
'''

#MIDE POSICION CON RESPECTO A LIBO DE ORDENES

libro_ordenes=binance.fetch_order_book(par)
posicion=libro_ordenes['bids']
cantidad_delante_mio=0

'''
for orden in posicion:
    
    if orden[0]>pedido_precio:
        print (orden[0]) # PRECIO
        print (orden[1]) # CANTIDAD
        cantidad_delante_mio +=orden[1]
 '''   
    

print ("Tu posicion va detras de :")
print(cantidad_delante_mio)

print("parece que todo ok")


#GESTIONAR TIEMPOS, SI LA HORA ES DISTINTA CANCELAR ORDENES Y VOLVER A EMPEZAR

ahora = datetime.now()  # Obtiene fecha y hora actual

print("Hora:", ahora.hour)  # Muestra hora




# current date and time
now = datetime.now()

timestamp = datetime.timestamp(now)
print("timestamp =", timestamp)






