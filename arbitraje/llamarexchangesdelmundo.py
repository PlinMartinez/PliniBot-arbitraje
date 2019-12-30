'''
llamarexchangesdelmundo.py
Ed 2.0 2019/5/27
implementa un filtro previo de numero de pares para poder terminar pronto
añade nombre de exchange a listado para ver proceso por donde va

'''


import ccxt

from funciones import BUSCATRIANGULOS
print(ccxt.exchanges)

lista = ccxt.exchanges

lista_filtro=[]
lista_fallos=[]

for id in lista:
    try:
        exchange_class=getattr(ccxt,id)
        exchange = exchange_class({'timeout':3000,'enableRateLimit':True,})
        mercados=exchange.load_markets()
        print(mercados.keys())
        numero_pares=len(mercados.keys())
        if int(numero_pares) < 515:
            lista_filtro.append(id)
            
    except:
        print('algo fallo')
        lista_fallos.append(id)
        


for i in lista_filtro:

    try:
        BUSCATRIANGULOS.buscatriangulos(i)
    except:
        pass
