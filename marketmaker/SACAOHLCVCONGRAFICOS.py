import ccxt  # MODULO CCXT
import claves  # CLAVES EN MISMA CARPETA EJECUTA SCRIPT
import pandas as pd  # DATAFRAMES
import matplotlib.pyplot as plt  # GRAFICAR CON PYPLOT

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

symbol = 'ADA/ETH'
symbol2 = 'ADX/ETH'

mercados = binance.load_markets(True)  # CARGA Y RECARGA MERCADOS

monedas = binance.currencies  # DICCIONARIO MONEDAS CON ESPECIFICACIONES

simbolos = binance.symbols  # LISTADO PARES INTERCAMBIO

metodos = dir(binance)  # LISTADO METODOS

print("empezamos")

ohlcv = binance.fetch_ohlcv(symbol, '1d')  # SACA OHLCV DE UN MERCADO COMPLETO

# GENERA LA TABLA
df = pd.DataFrame(ohlcv, columns=['Fecha',
                                  'Open',
                                  'High',
                                  'Lowest',
                                  'Closing',
                                  'Volumen'])


df['Fecha'] = pd.to_datetime(df['Fecha'], unit='ms')  # CAMBIA LOS MS EN FECHA

# col_list.remove('Closing')
# print(col_list)
# df['e']=df[col_list].sum(axis=1)

df['Volatilidad'] = df['High'] - df['Lowest']  # CREA COLUMNA VOL = HIGH - LOW
df['%'] = df['Volatilidad'] / df['Open'] * 100  # % = VOL / OPEN
df['%'] = df['%'].round(decimals=1)  # REDONDEA A UN DECIMAL
df2 = df.iloc[-1, -1]  # SACA ULTIMA FILA ULTIMA COLUMNA SI >3 % OK
miniserie = df['%'][-7:]  # ULTIMOS 7 DIAS PARA GRAFICAR
col_list = list(df)  # LISTADO DE COLUMNAS
print(df)


def dibuja(symbol=None):
    print('generando dibujo')
    ohlcv = binance.fetch_ohlcv(i, '1d')  # SACA OHLCV DE UN MERCADO COMPLETO
    # GENERA LA TABLA
    df = pd.DataFrame(ohlcv, columns=['Fecha',
                                      'Open',
                                      'High',
                                      'Lowest',
                                      'Closing',
                                      'Volumen'])
    df['Fecha'] = pd.to_datetime(
        df['Fecha'], unit='ms')  # CAMBIA LOS MS EN FECHA
    # CREA COLUMNA VOL = HIGH - LOW
    df['Volatilidad'] = df['High'] - df['Lowest']
    df['%'] = df['Volatilidad'] / df['Open'] * 100  # % = VOL / OPEN
    df['%'] = df['%'].round(decimals=1)  # REDONDEA A UN DECIMAL
    df2 = df.iloc[-1, -1]  # SACA ULTIMA FILA ULTIMA COLUMNA SI >3 % OK
    miniserie = df['%'][-7:]  # ULTIMOS 7 DIAS PARA GRAFICAR
    col_list = list(df)  # LISTADO DE COLUMNAS
    plt.figure()
    plt.title(i)  # TITULO GRAFICO
    plt.plot(miniserie, 'g')  # GRAFICA EN COLOR VERDE
    plt.xlabel('DIAS ULTIMA SEMANA')  # TITULO EJE X
    plt.ylabel('%VOLATILIDAD PRECIO DIARIA')  # TITULO EJE J
    plt.axhline(3, color='r')  # LINEA ROJA EN 3, NO ENTRAR MERCADO BAJO
    plt.ylim(0, 10)
    plt.text
    plt.axhspan(5, 6, alpha=0.25, color='green')  # BANDA ENTRE 5 Y 6
    plt.legend()  # CAJITA CON LEYENDA
    plt.show()  # ENSEÑA EL GRAFICO


a = ['ADA/ETH', 'ADX/ETH']
simbolos_prueba = simbolos[0:10]
for i in simbolos_prueba:
    dibuja(i)
