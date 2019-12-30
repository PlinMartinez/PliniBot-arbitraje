import ccxt
import claves
import pprint

# ACCESAR A BINANCE
usuario = claves.api_key
clave = claves.secret


# instancia mediante id a Binance con claves
exchange_id = 'binance'
exchange_class = getattr(ccxt, exchange_id)
binance = exchange_class({
    'apiKey': usuario,
    'secret': clave,
    'timeout': 30000,
    'enableRateLimit:': True,
})
# ccasas_cambio=ccxt.exchanges
# binance=ccxt.binance()
# LISTADO MERCADOS
mercados = binance.load_markets(True)
# LISTADO MONEDAS
monedas = binance.currencies
# LISTADO SIMBOLOS
simbolos = binance.symbols
# METODOS DEL EXCHANGE
metodos = dir(binance)

print("empezamos")

symbol = 'ADA/ETH'
moneda = 'ETH'

saldo = binance.fetch_balance()

trades = binance.fetch_my_trades(symbol)

print("parece que todo ok")

orden = (trades)[0]['order']
print("tu numero de orden lanzada es", str(orden))

pedidos_cerrados = binance.fetch_closed_orders(symbol)
pedidos_abiertas = binance.fetch_open_orders(symbol)
saldo_moneda = binance.fetch_free_balance()[moneda]

saldo_ADA = binance.fetch_free_balance()['ADA']
saldo_ETH = binance.fetch_free_balance()['ETH']
