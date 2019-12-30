# -*- coding: utf-8 -*-
"""
Created on Sat May 25 14:43:05 2019

@author: MPAZ
"""

import ccxt
import claves
import numpy as np

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

mercados=exchange.load_markets(True)
