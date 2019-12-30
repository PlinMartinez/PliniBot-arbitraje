# VAMOS A IMPORTAR LA TABLA CON TRIANGULACION PARA DESPUES ENTRAR EN EXCHANGE Y CACULAR PROFIT EN CVV Y VVC
import ccxt
import claves
import numpy as np
from datetime import datetime
import time

# ABRE EL FICHERO Y LEE EL CONTENIDO
# MODIFICAR PARA CADA USO EL EXCHANGE A USAR Y EL FICHERO BASE CON LISTADO DE TRIANGULOS DE ARBITRAGE
# POR EJEMPLO BINANCE & binancemini.txt
# VAMOS A HACER PRIMERO SOLO  VCC CON STOCK DE ALGUNAS CRIPTOMONEDAS COMO LTC O SKY


# AÑADIMOS FUNCIONES DE FECHAS Y TIEMPOS PARA VER DONDE SE VA EL TIEMPO
ahora = datetime.now()
dia = ahora.strftime("%Y%m%d")

t0 = time.time()



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

mercados = exchange.load_markets(True)

monedas = exchange.currencies

simbolos = exchange.symbols

metodos = dir(exchange)

consulta=exchange.fetch_trades('SKY/ETH')
print (consulta)