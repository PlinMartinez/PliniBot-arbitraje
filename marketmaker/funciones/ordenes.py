# -*- coding: utf-8 -*-
"""
Created on Sun Jun  2 15:42:00 2019

@author: MPAZ

EJECUTA ORDENES DE COMPRA VENTA PARA PLINI-BOT MARKET MAKER

"""

    
par='QSP/ETH'

import ccxt
import claves


#instancia mediante id a Binance con claves 
exchange_id= 'binance'
usuario=claves.api_key
clave=claves.secret
exchange_class = getattr(ccxt, exchange_id)
exchange= exchange_class({
	'apiKey':usuario,
	'secret':clave,
	'timeout':30000,
	'enableRateLimit:': True,
})

#mercado de pares con caracteriistcas
mercados=exchange.load_markets(True)

#listado de pares
pares_lista=list(exchange.markets.keys())

#listado de MONEDAS  
monedas=exchange.currencies

#CONSULTAR BALANCE
balances=exchange.fetch_balance()


libro_ordenes=exchange.fetch_order_book(par)
bid=libro_ordenes['bids'][0][0]
ask=libro_ordenes['asks'][0][0]
spread=ask-bid
spread_porcentaje=round(spread/bid*100,2)
medio=(ask+bid)/2
pcompra=medio*0.98
pventa=medio*1.02
#¿EN QUE POSICION ESTAS EN VENTA O EN COMPRA?

# LIMITES GESTION EN PAR
base=mercados[par]['precision']['base']
quote=mercados[par]['precision']['quote']
amount=mercados[par]['precision']['amount']
price=mercados[par]['precision']['price']


#CONSULTAR BALANCE
balances=exchange.fetch_balance()

base=par.split('/')[0]
quote=par.split('/')[1]
saldo_base=exchange.fetch_free_balance()[base]
saldo_quote=exchange.fetch_free_balance()[quote]


minimo_notional = (mercados)[par]['info']['filters'][3]['minNotional']
notional = float(minimo_notional)
qminimocompra=notional/pcompra
qminimoventa=notional/pventa
qcompra=qminimocompra*1.2
qventa=qminimoventa*1.2


try:
    
    #CREA ORDEN DE VENTA
    symbol= par
    type= 'limit'
    side_venta= 'sell'
    amount_venta= round(qventa,amount)
    price_venta=  round(pventa,price)
    
    okventa=saldo_quote-(amount_venta*price_venta)
    print('VAMOS A LANZAR VENTA DE ',symbol,side_venta,amount_venta,price_venta)
    orden_venta= exchange.create_order(symbol,type,side_venta,amount_venta,price_venta)
    print('ORDEN VENTA CREADA')

except ccxt.NetworkError as e:
    print(exchange.id, 'fetch_currencies fallo por error de red:', str(e))
except ccxt.ExchangeError as e:
    print(exchange.id, 'fetch_currencies fallo por error de exchange:', str(e))
except Exception as e:
    print(exchange.id, 'fetch_currencies fallo por:', str(e))
    print("No se ha podido hacer la venta")

try:
    
    #CREA ORDEN DE COMPRA
    symbol= par
    type= 'limit'
    side_compra= 'buy'
    amount_compra= round(qcompra,amount)
    price_compra=  round(pcompra,price)
    
    okcompra=saldo_base-amount_compra
    print('VAMOS A COMPRAR',symbol,side_compra,amount_compra,price_compra)
    orden_compra= exchange.create_order(symbol,type,side_compra,amount_compra,price_compra)
    print('ORDEN COMPRA CREADA')


except ccxt.NetworkError as e:
    print(exchange.id, 'fetch_currencies fallo por error de red:', str(e))
except ccxt.ExchangeError as e:
    print(exchange.id, 'fetch_currencies fallo por error de exchange:', str(e))
except Exception as e:
    print(exchange.id, 'fetch_currencies fallo por:', str(e))
    print("No se ha podido hacer la venta")



