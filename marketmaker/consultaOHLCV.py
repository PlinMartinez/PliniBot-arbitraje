'''ESTE PROGRAMA ES EL PASO 1 DE EXPORTAR VOLATILIDADES PARA LUEGO ANALIZAR'''



import ccxt
import claves
import pandas as pd
import matplotlib.pyplot as plt

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

symbol='ADA/ETH'
symbol2='ADX/ETH'

mercados=binance.load_markets(True)

monedas= binance.currencies

simbolos=binance.symbols

metodos=dir(binance)


def volatilidad(symbol=None):
    #print("empezamos")
    ohlcv=binance.fetch_ohlcv(symbol,'1d')
    df = pd.DataFrame(ohlcv,columns=['Fecha',
                                     'Open',
                                     'High',
                                     'Lowest',
                                     'Closing',
                                     'Volumen'])
    df['Fecha'] = pd.to_datetime(df['Fecha'], unit='ms')
    col_list=list(df)
    df['Volatilidad'] = df['High'] - df['Lowest'] 
    df['%']=df['Volatilidad'] / df['Open'] * 100
    df['%']=df['%'].round(decimals=1)
    volatilidad=df.iloc[-1,-1]
    miniserie=df['%'][-7:]
    #print (df)
    print(symbol,'tiene hoy una volatilidad de  ',volatilidad, ' %')
    return volatilidad

simbolos_mini=simbolos[10:25]
vol_pares=[]

# SACA VOLATILIDADES DE TODOS LOS MERCADOS
for i in simbolos_mini:
    suma=volatilidad(i)
    vol_pares.append(suma)

d=dict(zip(simbolos,vol_pares))
print (d)
dfichero=str(d)

#METODO 1
f = open("volatilidades.txt", "w")
f.write(dfichero)
f.close()

#METODO 2

f = open("volatilidades2.csv", "w")
f.write("Par")
f.write(",")
f.write("Volatilidad")
f.write("\n")
for (clave, valor) in d.items():
    print(clave, ",", valor)
    f.write(str(clave))
    f.write(",")
    f.write(str(valor))
    f.write("\n")

f.close()

vol_pares2=vol_pares[10:25]
plt.plot(simbolos_mini,vol_pares2)
plt.ylim(0,20)
plt.title('Volatilidad algunos cambios')
plt.axhline(3,color='r')
plt.show()


plt.figure('VOLATILIDAD DE CAMBIO ADA/ETH')
plt.title('VOLATILIDAD ADA/ETH')
plt.plot(miniserie,'g')
plt.xlabel('DIAS ULTIMA SEMANA')
plt.ylabel('%VOLATILIDAD PRECIO DIARIA')
plt.axhline(3,color='r')
#plt.ylim(0,10)
plt.axhspan(5,6,alpha=0.25,color='green')
plt.legend()
plt.show()




