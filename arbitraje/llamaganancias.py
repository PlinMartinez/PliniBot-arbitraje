import ccxt
from funciones import ganancias


lista = ccxt.exchanges

for i in lista:
    nombre= i
   
    try:
        ganancias.ganancias(nombre)
    except:
        print("se ha liado parda en algun exchange que no tengo lista")
