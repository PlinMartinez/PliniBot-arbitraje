# -*- coding: utf-8 -*-
"""
Created on Sat May 25 22:32:13 2019

@author: MPAZ

CONECTA POR WEBSOCKES CON BINANCE Y ESTUDIA 2 TRIANGULOS
SI VE OPCION
LANZA COMPRA CON CCXT Y MIDE TIEMPOS A VER QUE PASA

"""

import time
from binance.client import Client
import claves
from binance.websockets import BinanceSocketManager
from datetime import datetime
import time


public = claves.api_key
secret = claves.secret

client = Client(api_key=public, api_secret=secret)

bm = BinanceSocketManager(client)


def handle_message(msg):

    if msg['e'] == 'error':
        print(msg['m'])

    else:
        #bitcoins_exchanged = float(msg['p']) * float([msg['q']])
        timestamp = msg['T'] / 1000
        timestamp = datetime.fromtimestamp(
            timestamp).strftime('Y-%m-%d %H:%M:%S')

    if msg['m'] == True:
        event_side = 'SELL'
    else:
        event_side = 'BUY'

    print("{} - {} - {} Price: {} - Qty: {} BTC Qty: {}".format(timestamp,
                                                               event_side,
                                                               msg['s'],
                                                               msg['p'],
                                                               msg['q'],))


conn_key = bm.start_trade_socket('ETHBTC', handle_message)


bm.start()

time.sleep(10)

bm.stop_socket(conn_key)
