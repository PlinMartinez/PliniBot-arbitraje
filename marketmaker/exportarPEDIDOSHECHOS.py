import ccxt
import pandas as pd 


#ACCESAR A BINANCE
usuario='fXmen1YY4cSmOrCy6b2DcS3XhQJlsHxYtRTfjXrTx44uStvicVM9LM5Zpsiess0B'
clave='KooOFFONa1JzJIPiFtvAgVAdhUYWSxBR1Y1VFCRMDhdcwGdy4jt6fuYNKgT7rgaV'


#instancia mediante id a Binance con claves 
exchange_id= 'binance'
exchange_class = getattr(ccxt, exchange_id)
binance= exchange_class({
	'apiKey':usuario,
	'secret':clave,
	'timeout':30000,
	'enableRateLimit:': True,
})



symbol='ETH/PAX'

metodos=dir(binance)

print("empezamos")


trades=binance.fetch_my_trades(symbol)

print("parece que todo ok")

#orden=(trades)[0]['order']
#print("tu numero de orden lanzada es", str(orden))

pedidos_cerrados=binance.fetch_closed_orders(symbol)

pedidos_abiertas=binance.fetch_open_orders(symbol)

prueba1=binance.fetch_my_trades(symbol)

since= binance.milliseconds()  
all_orders = []
while since < binance.milliseconds():
    limit=5
    orders = binance.fetch_orders(simbol, since, limit)
    if len(orders):
        since= orders[len(orders)-1]
        all_orders += orders
    else:
        break


df=pd.DataFrame(pedidos_cerrados)

file_name='C:\python\Spyder\exportar\ordeneshechas.csv'
#grabado=df.to_csv(file_name, sep='\t', encoding='utf-8')

with open('test.csv', 'a+') as f:        
    df.to_csv(f, header=False)    

print(df)









