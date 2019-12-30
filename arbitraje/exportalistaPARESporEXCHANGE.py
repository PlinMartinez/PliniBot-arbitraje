import ccxt

print('LOS EXCHANGES DISPONIBLES SON ESTOS')
print(ccxt.exchanges)


# ids = ['binance','bigone', 'bitbank']

# TOMA TODOS LOS EXCHANGES EN LISTA PARA IR ACTUANDO SOBRE TODOS
ids = ccxt.exchanges

listabuenos = []
listafallo = []

for id in ids:

    try:
        exchange_class = getattr(ccxt, id)
        exchange = exchange_class({'timeout': 3000, 'enableRateLimit': True, })
        mercados = exchange.load_markets()
        print(mercados.keys())
        numero_pares = len(mercados.keys())
        print('El número de pares que tiene este exchange ' +
              id + ' ' + str(numero_pares))
        listabuenos.append(id + ',' + str(numero_pares))

    except:
        print('Ha fallado')
        print(id)
        listafallo.append(id)


fichero = 'listamundialexchanges.txt'

contador = 0
with open(fichero, 'w') as f:
    for i in listabuenos:
        f.write(listabuenos[contador])
        f.write('\n')

        contador = contador + 1
        print("linea grabada")
print("ok, grabado!!")

fichero = 'listafallo.txt'

contador = 0
with open(fichero, 'w') as f:
    for i in listafallo:
        f.write(listafallo[contador])
        f.write('\n')

        contador = contador + 1
        print("linea de fallos grabado")
print("ok, grabado los malos!!")