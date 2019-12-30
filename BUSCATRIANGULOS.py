import ccxt
import sys


#USAR bitbank PARA PROBAR ya que se hace rapido
#EL PASO PRIMERO ES ESTE , BUSCA EN CADA EXCHANGE TODOS LOS TRIANGULOS POSIBLES
#LUEGO TOCA VERIFICAR GANANCIAS, BUSCAR COLOCACION CERCANA A CADA EXCHANGE
#FINALMENTE TOCA EJECUTAR SIN TEMOR A "FUEGO" LAS COMPRAS


def buscatriangulos(nombre):

    print(ccxt.exchanges)

    id = nombre
    exchange_class = getattr(ccxt, id)
    exchange = exchange_class({'timeout': 3000, 'enableRateLimit': True, })
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
                print(id,'-',lista1[a],'-', lista2[b],'-', lista3[c])

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


#POR EJEMPLO python buscatriangulos.py binance
if __name__ == '__main__':
    buscatriangulos(sys.argv[1])
