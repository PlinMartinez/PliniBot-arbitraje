# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 22:05:39 2019

@author: MPAZ

BOT DE ARBITRAJE. TOMA 3 PARES Y REVISA CAMINOS CVV Y VCC 6 POSIBILIDADES
SEGUN DECIMALES PUEDE O NO REALIZAR TRIANGULACION
MIRA SI DA DINERO O SE PIERDE
EXPORTA UNA TABLA CON TODAS LAS OPCIONES REALES

"""
import ccxt
import claves

# ACCESAR A BINANCE
usuario = claves.api_key
clave = claves.secret

# instancia mediante id a Binance con claves
nombre = 'binance'
exchange_class = getattr(ccxt, nombre)
exchange = exchange_class({
    'apiKey': usuario,
    'secret': clave,
    'timeout': 30000,
    'enableRateLimit:': True,
})

#INSTANCIA METODOS QUE PUEDEN SER UTILES
mercados = exchange.load_markets(True)
monedas = exchange.currencies
simbolos = exchange.symbols
metodos = dir(exchange)

#CARGA LIBRO DE ORDENES DE LOS 3 PARES PARA PODER COMPARAR

par1='LTC/BTC'
par2='BNB/BTC'
par3='LTC/BNB'
libro_ordenes1 = exchange.fetch_order_book(par1)
libro_ordenes2 = exchange.fetch_order_book(par2)
libro_ordenes3 = exchange.fetch_order_book(par3)

pc1 = libro_ordenes1['asks'][0][0]
pv1 = libro_ordenes1['bids'][0][0]
pc2 = libro_ordenes2['asks'][0][0]
pv2 = libro_ordenes2['bids'][0][0]
pc3 = libro_ordenes3['asks'][0][0]
pv3 = libro_ordenes3['bids'][0][0]

# LIMITES GESTION EN PAR
base1decimales = mercados[par1]['precision']['base']
base2decimales = mercados[par2]['precision']['base']
base3decimales = mercados[par3]['precision']['base']
quote1decimales = mercados[par1]['precision']['quote']
quote2decimales = mercados[par2]['precision']['quote']
quote3decimales = mercados[par3]['precision']['quote']
amount1decimales = mercados[par1]['precision']['amount']
amount2decimales = mercados[par2]['precision']['amount']
amount3decimales = mercados[par3]['precision']['amount']
price1decimales = mercados[par1]['precision']['price']
price2decimales = mercados[par2]['precision']['price']
price3decimales = mercados[par3]['precision']['price']

# SACA Q MIN COMPRAS
minimo_notional1 = (mercados)[par1]['info']['filters'][3]['minNotional']
notional1 = float(minimo_notional1)
minimo_notional2 = (mercados)[par2]['info']['filters'][3]['minNotional']
notional2 = float(minimo_notional2)
minimo_notional3 = (mercados)[par3]['info']['filters'][3]['minNotional']
notional3 = float(minimo_notional3)
minimoqbasepar1=round((notional1/pv1)*1.2,amount1decimales)
minimoqbasepar2=round((notional2/pv2)*1.2,amount2decimales)
minimoqbasepar3=round((notional3/pv3)*1.2,amount3decimales)

#SEPARA BASE DE QUOTE EN CADA PAR
base1 = par1.split('/')[0]
base2 = par2.split('/')[0]
base3 = par3.split('/')[0]
quote1 = par1.split('/')[1]
quote2 = par2.split('/')[1]
quote3 = par3.split('/')[1]
saldo_base1 = exchange.fetch_free_balance()[base1]
saldo_base2 = exchange.fetch_free_balance()[base2]
saldo_base3 = exchange.fetch_free_balance()[base3]
saldo_quote1 = exchange.fetch_free_balance()[quote1]
saldo_quote2 = exchange.fetch_free_balance()[quote2]
saldo_quote3 = exchange.fetch_free_balance()[quote3]

'''
CAMINO 1: VCC par1 par2 par3   b3-b1
CAMINO 2: CCV par2 par3 par1   q1-q2
CAMINO 3: CVC par3 par1 par2   b2-q3
CAMINO 4: CVV par1 par3 par2   q2-q1
CAMINO 5: VCV par2 par1 par3   q3-b2
CAMINO 6: VVC par3 par2 par1   b1-b3
'''

camino1paso1quote1=round(minimoqbasepar1*pv1,quote1decimales)
camino1paso2base2=round(camino1paso1quote1/pc2,base2decimales)
camino1paso3base3=round(camino1paso2base2/pc3,base3decimales)
camino1paso4resultado=camino1paso3base3-minimoqbasepar1
beneficiocamino1moneda1=camino1paso4resultado/minimoqbasepar1

camino2paso1quote2=round(minimoqbasepar2*pc2,quote2decimales)
camino2paso2base3=round(camino2paso1quote2/pc3,base3decimales)
camino2paso3quote1=round(camino2paso2base3*pv1,quote1decimales)
camino2paso4resultado=camino2paso3quote1-camino2paso1quote2
beneficiocamino1moneda2=camino2paso4resultado/camino2paso1quote2

camino3paso1quote3=round(minimoqbasepar3*pc3,quote3decimales)
camino3paso2quote1=round(camino3paso1quote3*pv1,quote1decimales)
camino3paso3base1=round(camino3paso2quote1/pc2,base2decimales)
camino3paso4resultado=minimoqbasepar2-camino3paso1quote3
beneficiocamino3moneda3=camino3paso4resultado/camino3paso1quote3

camino4paso1quote1=round(minimoqbasepar1*pc1,quote1decimales)
camino4paso2quote3=round(camino4paso1quote1*pv3,quote3decimales)
camino4paso3quote2=round(camino4paso2quote3*pv2,base2decimales)
camino4paso4resultado=camino4paso3quote2-camino4paso1quote1
beneficiocamino4moneda2=camino4paso4resultado/camino4paso1quote1

camino5paso1quote2=round(minimoqbasepar2*pv2,quote2decimales)
camino5paso2base1=round(camino5paso1quote2/pc2,base1decimales)
camino5paso3quote3=round(camino5paso2base1*pv3,quote3decimales)
camino5resultadomoneda3=camino5paso3quote3-minimoqbasepar2
beneficiocamino5moneda3=camino5resultadomoneda3/minimoqbasepar2

camino6paso1quote3=round(minimoqbasepar3*pv3,quote3decimales)
camino6paso2quote2=round(camino6paso1quote3*pv2,quote2decimales)
camino6paso3base1=round(camino6paso2quote2/pc1,base1decimales)
camino6paso4resultadomoneda1=camino6paso3base1-minimoqbasepar3
beneficiocamino6moneda1=camino6paso4resultadomoneda1/minimoqbasepar3

#CAMINO5 ORDENES

symbol1 = par2
type1 = 'limit'
side1 = 'sell'
amount1 = minimoqbasepar2
price1=pv2

symbol2 = par1
type2 = 'limit'
side2 = 'buy'
amount2 = camino5paso2base1
price2=pc1

symbol3 = par3
type3 = 'limit'
side3 = 'sell'
amount3 = camino5paso2base1
price3=pv3


'''

print('EJECUTAMOS ORDEN')
exchange.create_order(symbol1,type1,side1,amount1,price1)
exchange.create_order(symbol2,type2,side2,amount2,price2)
exchange.create_order(symbol3,type3,side3,amount3,price3)
print('ORDEN EJECUTADA!!')

'''




            
            
            
            
            
            
            
            
            