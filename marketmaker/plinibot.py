# -*- coding: utf-8 -*-
"""
Created on Sun Jun  2 14:25:13 2019

@author: MPAZ

ROBOT DE ALGO-TRADING
COMPRA BARATO - VENDE CARO
7 PASOS PRIMERO
DESPUES , BUSCAR RUIDO PARA ENTRAR

"""

import ccxt
import claves
import pprint
import pandas as pd

# instancia mediante id a Binance con claves
exchange_id = 'binance'
usuario = claves.api_key
clave = claves.secret
exchange_class = getattr(ccxt, exchange_id)
exchange = exchange_class({
    'apiKey': usuario,
    'secret': clave,
    'timeout': 30000,
    'enableRateLimit:': True,
})

# mercado de pares con caracteriistcas
mercados = exchange.load_markets(True)

# listado de pares
pares_lista = list(exchange.markets.keys())

# listado de MONEDAS
monedas = exchange.currencies

# CONSULTAR BALANCE
balances = exchange.fetch_balance()

moneda1 = 'ADA'
moneda2 = 'ETC'
moneda3 = 'BTC'


saldos = exchange.fetch_free_balance()

# GENERA LISTA DE MONEDAS CON LIQUIDEZ

liquidez = {}

for saldo in saldos:
    if saldos[saldo] > 0:
        liquidez[saldo] = saldos[saldo]

efectivo = 'ETH'

''' RECORRE LA CARTERA CON BASURILLAS DE SALDOS A HACER x100
for efectivo in liquidez:
    print (efectivo)
'''

lista_pares_maker = []

# FUNCION QUE TOMA UNA MONEDA Y SACA LISTADO DE COINCIDENCIAS


def buscapares(moneda):
    for par in pares_lista:
        print(par)
        base = par.split('/')[0]
        quote = par.split('/')[1]
        print(base)
        print(quote)
        if liquido == base:
            lista_pares_maker.append(par)


# LLAMA A FUNCION TOMANDO LAS MONEDAS EN EFECTIVO
for liquido in liquidez:
    buscapares(liquido)


def lanza_ordenes_maker(par):

    # CONSULTAR BALANCE
    balances = exchange.fetch_balance()

    try:
        libro_ordenes = exchange.fetch_order_book(par)
        bid = libro_ordenes['bids'][0][0]
        ask = libro_ordenes['asks'][0][0]

        medio = (ask + bid) / 2
        pcompra = medio * 0.995
        pventa = medio * 1.005
        #¿EN QUE POSICION ESTAS EN VENTA O EN COMPRA?

        # LIMITES GESTION EN PAR
        base = mercados[par]['precision']['base']
        quote = mercados[par]['precision']['quote']
        amount = mercados[par]['precision']['amount']
        price = mercados[par]['precision']['price']

        base = par.split('/')[0]
        quote = par.split('/')[1]
        saldo_base = exchange.fetch_free_balance()[base]
        saldo_quote = exchange.fetch_free_balance()[quote]

        minimo_notional = (mercados)[par]['info']['filters'][3]['minNotional']
        notional = float(minimo_notional)
        qminimocompra = notional / pcompra
        qminimoventa = notional / pventa
        qcompra = qminimocompra * 1.2
        qventa = qminimoventa * 1.2

        # CREA ORDEN DE VENTA
        symbol = par
        type = 'limit'
        side_venta = 'sell'
        amount_venta = round(qventa, amount)
        price_venta = round(pventa, price)

        okventa = saldo_quote - (amount_venta * price_venta)
        print('VAMOS A LANZAR VENTA DE ', symbol,
              side_venta, amount_venta, price_venta)
        orden_venta = exchange.create_order(
            symbol, type, side_venta, amount_venta, price_venta)
        print('ORDEN VENTA CREADA')

        # CREA ORDEN DE COMPRA
        symbol = par
        type = 'limit'
        side_compra = 'buy'
        amount_compra = round(qcompra, amount)
        price_compra = round(pcompra, price)

        okcompra = saldo_base - amount_compra
        print('VAMOS A COMPRAR', symbol, side_compra,
              amount_compra, price_compra)
        orden_compra = exchange.create_order(
            symbol, type, side_compra, amount_compra, price_compra)
        print('ORDEN COMPRA CREADA')

    except ccxt.NetworkError as e:
        print(exchange.id, 'fetch_currencies fallo por error de red:', str(e))
    except ccxt.ExchangeError as e:
        print(exchange.id, 'fetch_currencies fallo por error de exchange:', str(e))
    except Exception as e:
        print(exchange.id, 'fetch_currencies fallo por:', str(e))
        print("No se ha podido hacer la venta")


# LANZA A SACO PEDIDOS DE VENTA Y DE COMPRA PARA TODOS LOS PARES


for maker in lista_pares_maker:
    lanza_ordenes_maker(maker)
