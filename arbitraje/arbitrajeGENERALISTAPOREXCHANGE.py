import ccxt

print(ccxt.exchanges)

nombre = 'bitfinex'
exchange = ccxt.bitfinex()

mercados = exchange.load_markets(True)

print(mercados)


lista1 = (list(exchange.markets.keys()))

print(lista1)

# lista1=lista2=lista3=['ADA/ETH','EUR/USD','ETH/BTC','ZEC/USDT','ADA/BTC']

lista2 = lista3 = lista1

lista_arbitraje = []

'''
par1='ADA/BTC'
par2='ETH/BTC'
par3='ADA/ETH'

base1=par1.split('/')[0]
quote1=par1.split('/')[1]
base2=par2.split('/')[0]
quote2=par2.split('/')[1]
base3=par3.split('/')[0]
quote3=par3.split('/')[1]

if base1 == base3 and quote1 == quote2 and base2 == quote3:
	print (base1, '/',quote1, '=', base2,'/',quote2, 'x',base3,'/',quote3)

'''

p1 = 0
p2 = 0
p3 = 0

largo = len(lista1)

print(lista1)
print(len(lista1))

for a in range(0, largo):
    for b in range(0, largo):
        for c in range(0, largo):
            print(lista1[a], lista2[b], lista3[c])

            par1 = lista1[a]
            par2 = lista2[b]
            par3 = lista3[c]

            base1 = par1.split('/')[0]
            quote1 = par1.split('/')[1]
            base2 = par2.split('/')[0]
            quote2 = par2.split('/')[1]
            base3 = par3.split('/')[0]
            quote3 = par3.split('/')[1]

            if base1 == base3 and quote1 == quote2 and base2 == quote3:
                print(base1, '/', quote1, '=', base2, '/',
                      quote2, 'x', base3, '/', quote3)
                lista_arbitraje.append(par1 + '-' + par2 + '-' + par3)

fichero = nombre + 'arbitraje.txt'

contador = 0
with open(fichero, 'w') as f:
    for i in lista_arbitraje:
        f.write(lista_arbitraje[contador])
        f.write('\n')

        contador = contador + 1
        print("linea grabada")
print("ok, grabado!!")

import json

filename = nombre + 'arbitraje.json'
with open(filename, 'w') as f_obj:
    json.dump(lista_arbitraje, f_obj)

print("json generado")
