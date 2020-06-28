
# IMPORTA FUNCIONES NECESARIAS PARA TRABAJAR
#adandio cambio junio 2020

from funciones.utilidades import instanciar
from funciones.utilidades import grabar_csv
from funciones.utilidades import grabar_txt
import pandas as pd
import shelve

exchange = instanciar()

mercados = exchange.load_markets(True)

monedas = exchange.currencies

simbolos = exchange.symbols

metodos = dir(exchange)


def volatilidad(symbol=None):
    # print("empezamos")
    ohlcv = exchange.fetch_ohlcv(symbol, '1d')
    df = pd.DataFrame(ohlcv, columns=['Fecha',
                                      'Open',
                                      'High',
                                      'Lowest',
                                      'Closing',
                                      'Volumen'])
    df['Fecha'] = pd.to_datetime(df['Fecha'], unit='ms')
    col_list = list(df)
    df['Volatilidad'] = df['High'] - df['Lowest']
    df['%'] = df['Volatilidad'] / df['Open'] * 100
    df['%'] = df['%'].round(decimals=1)
    volatilidad = df.iloc[-1, -1]
    miniserie = df['%'][-7:]
    #print (df)
    print(symbol, 'tiene hoy una volatilidad de  ', volatilidad, ' %')
    return volatilidad


# AQUI SE DEFINEN LOS SIMBOLOS A ANALIZAR LA VOLATILIDAD
symbol = 'ADA/ETH'
symbol2 = 'ADX/ETH'
simbolos_mini = simbolos[10:25]
simbolos = exchange.symbols


# SACA VOLATILIDADES DE TODOS LOS MERCADOS
vol_pares = []
for i in simbolos:
    amplitud = volatilidad(i)
    vol_pares.append(amplitud)

# CREA EL DICCIONARIO PARA EXPORTAR INFO Y SEGUIR DESDE OTROS PROGRAMAS
volatilidades = dict(zip(simbolos, vol_pares))
print(volatilidades)


dfichero = str(volatilidades)
'''
print('VAMOS A GRABAR UN FICHERO TXT CON VOLATILIDADES DEL DIA')
grabar1 = grabar_txt(volatilidades)

print('VAMOS A GRABAR OTRO FICHERO CSV CON VOLATILIDADES DEL DIA')
grabar2 = grabar_csv(volatilidades)
'''

shelfFile=shelve.open('variables')
shelfFile['volatilidades']=volatilidades
shelfFile.close()



