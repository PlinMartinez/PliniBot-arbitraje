import ccxt
import claves

#ACCESAR A BINANCE
usuario=claves.api_key
clave=claves.secret


#instancia mediante id a Binance con claves 
exchange_id= 'binance'
exchange_class = getattr(ccxt, exchange_id)
binance= exchange_class({
	'apiKey':usuario,
	'secret':clave,
	'timeout':30000,
	'enableRateLimit:': True,
})


casas_cambio=ccxt.exchanges

#binance=ccxt.binance()

mercados=binance.load_markets(True)

monedas= binance.currencies

simbolos=binance.symbols

metodos=dir(binance)

print("empezamos")

libroBNBETH=binance.fetch_order_book('BNB/ETH')
ask=libroBNBETH['asks'][0][0]
bid=libroBNBETH['bids'][0][0]
spread=ask-bid
medio=(ask+bid)/2
compra=medio*0.98
venta=medio*1.02

saldo=binance.fetch_balance()['ETH']['free']

symbol='BNB/ETH'

amount=0.01/compra
amount_redondeo=round(amount,4)+0.0001
prueba=0.08
valor=amount*compra
price=compra




trades=binance.fetch_my_trades(['BNB/ETH'])

print(trades)

print("parece que todo ok")



