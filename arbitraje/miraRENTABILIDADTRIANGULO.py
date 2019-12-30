import ccxt
import claves

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


casas_cambio = ccxt.exchanges

# binance=ccxt.binance()

mercados = binance.load_markets(True)

monedas = binance.currencies

simbolos = binance.symbols

metodos = dir(binance)

print("empezamos")

# MIRAMOS PRIMERO CVV >=1 Y LUEGO VCC >=1
par1 = 'ADA/BTC'  # COMPRA
par2 = 'ETH/BTC'  # VENTA
par3 = 'ADA/ETH'  # VENTA

c1 = binance.fetch_order_book(par1)['bids'][0][0]
v2 = binance.fetch_order_book(par2)['asks'][0][0]
v3 = binance.fetch_order_book(par3)['asks'][0][0]


gasto1 = 1000 * c1  # 1000 ADAS , GASTADO 0.011080 BTC
i2 = gasto1 / v2  # INGRESO 2 EN ETH GASTANDO LOS BTC DEL PASO 1
i3 = i2 / v3  # INGRESO 3 EN ADA GASTANDO LOS ETH DEL PASO 2

resultadoCVV = round((i3 - 1000), 2)
prueba = i3 - 1000
prueba2 = round(prueba, 2)


# MIRAMOS AHORA VCC >=1
par1 = 'ADA/BTC'  # VENTA
par2 = 'ETH/BTC'  # COMPRA
par3 = 'ADA/ETH'  # COMPRA

v1 = binance.fetch_order_book(par1)['asks'][0][0]
c2 = binance.fetch_order_book(par2)['bids'][0][0]
c3 = binance.fetch_order_book(par3)['bids'][0][0]


venta1 = 1000 * v1  # 1000 ADAS VENDO , INGRESO 0.01117 BTC
i2 = gasto1 / v2  # INGRESO 2 EN ETH GASTANDO LOS BTC DEL PASO 1
i3 = i2 / v3  # INGRESO 3 EN ADA GASTANDO LOS ETH DEL PASO 2

resultadoCVV = i3 - 1000
g2 = venta1 / c2
g3 = g2 / c3

resultadoVCC = round((g3 - 1000), 2)

print (resultadoVCC)
print (resultadoCVV)
