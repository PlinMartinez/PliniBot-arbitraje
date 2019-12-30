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

# Tabla con arbitrajes que va a revisar solamente, quitar los que no parezcan interesantes
filename = 'binancearbitraje.txt'


file = open(filename, mode='r')
text = file.read()
file.close()
print(text)


# ABRE EL FICHERO Y LO TOMA COMO MATRIZ DE A x B FILAS / COLUMNAS

data = np.loadtxt(filename,
                  delimiter='-',
                  usecols=[0, 1, 2],
                  dtype=str)

print(data)
print(type(data))

print(data.shape)
print(data[1, 0])
print(data[1, 1])
print(data[1, 2])

filas = data.shape[0]
columnas = data.shape[1]

print('Tienes una matriz de ' + str(filas) + "x" + str(columnas))


casas_cambio = ccxt.exchanges

mercados = exchange.load_markets(True)

monedas = exchange.currencies

simbolos = exchange.symbols

metodos = dir(exchange)

ganancias = []


'''
REALIZA LAS ORDENES DE COMPRA CVV O VCC DE FORMA CONTINUADA A VER SI ALGO GANA

FUN/BTC,ETH/BTC,FUN/ETH,11.94,-15.92
REQ/BTC,ETH/BTC,REQ/ETH,12.65,-10.03
POWR/ETH,BNB/ETH,POWR/BNB,12.58,-7.09
AMB/BTC,BNB/BTC,AMB/BNB,12.68,-18.3
AMB/ETH,BNB/ETH,AMB/BNB,14.06,-18.75
BCPT/ETH,BNB/ETHCPT/BNB,10.26,-10.28
CDT/BTC,ETH/BTC,CDT/ETH,11.29,-4.54

'''

print("empezamos")

t1=time.time()-t0



par1 = 'HOT/BTC'
par2 = 'BNB/BTC'
par3 = 'HOT/BNB'
par1str = str(par1)
par2str = str(par2)
par3str = str(par3)
triangulo=[par1str,'-',par2str,'-',par3str]
print(triangulo)

t2=time.time()-t0

libro_ordenes1 = exchange.fetch_order_book(par1)
libro_ordenes2 = exchange.fetch_order_book(par2)
libro_ordenes3 = exchange.fetch_order_book(par3)

t3=time.time()-t0

pc1 = libro_ordenes1['asks'][0][0]
pv1 = libro_ordenes1['bids'][0][0]
pc2 = libro_ordenes2['asks'][0][0]
pv2 = libro_ordenes2['bids'][0][0]
pc3 = libro_ordenes3['asks'][0][0]
pv3 = libro_ordenes3['bids'][0][0]

#CALCULA VCC >> V1 / C2 x C3

paso1VCC=pv1/(pc2*pc3)
paso2VCC=1000-(paso1VCC*1000)
resultadoVCC=round(paso2VCC,1)

print('RESULTADOVCC ',str(resultadoVCC))
      


#CALCULA CVV >> C1 / V2 x V3
paso1CVV=pc1/(pv2*pv3)
paso2CVV=1000-(paso1CVV*1000)
resultadoCVV=round(paso2CVV,1)

print('RESULTADOCVV ',str(resultadoCVV))

# SACA Q MIN COMPRAS
minimo_notional1 = (mercados)[
    par1]['info']['filters'][3]['minNotional']
notional1 = float(minimo_notional1)
minimo_notional2 = (mercados)[
    par2]['info']['filters'][3]['minNotional']
notional2 = float(minimo_notional2)
minimo_notional3 = (mercados)[
    par3]['info']['filters'][3]['minNotional']
notional3 = float(minimo_notional3)

'''
qc1 = notional1 / pc1
qc1a =round(qc1*1.2,6)
qv1 = notional1 / pv1 
qv1a= round(qv1*1.2,6)
qv2 = notional2 / pv2
qv2a= round(qv2*1.2,6)
qc2 = notional2 / pc2
qc2a= round(qc2*1.2,6)
qv3 = notional3 / pv3
qv3a= round(qv3*1.2,6)
qc3 = notional3 / pc3
qc3a= round(qc3*1.2,6)
'''


#AJUSTE DE CANTIDADES POR CAMINANTE METODO CVV  qq2 == qq1 comparar(1,3,2)
qq1=notional1*1.2
qb1=qq1/pc1 #CUANTO qbase1 gano
qq1=qb1*pc1           #CUANTO qquote gasto   
qb3=qb1
qq3=qb3*pv3
qb2=qq3
qq2=qb2*pv3
rsegcvv1=qb1-qb3
rsegcvv2=qq2-qq1     #RESULTADO REAL OPERACION CVV +qq2 fin - qq1 inicio
rsegcvv2p=rsegcvv2/qq2  # tiene que ser mayor > 0.01
rsegcvv3=qq3-qb2
qb1f=round(qb1,6)
qb2f=round(qb2,6)
qb3f=round(qb3,6)
finalCVV=rsegcvv2p

#CALCULOS PARA CAMINO VCC    qb3==qb1 (1,2,3)
qqx1=notional1*1.2 
qbx1=qqx1/pv1
qqx2=qqx1
qbx2=qqx2/pc2
qqx3=qbx2
qbx3=qqx3/pc3
#rsegvcc1=qbx3f-qbx1f  # RESULTADO REAL OPERACION VCC +qb3 fin -qb1 inicio 
rsegvcc2=qqx1-qqx2
rsegvcc3=qbx2-qqx3
qbx1f=round(qbx1,6)
qbx2f=round(qbx2,6)
qbx3f=round(qbx3,6)

rsegvcc1=qbx3f-qbx1f  # RESULTADO REAL OPERACION VCC +qb3 fin -qb1 inicio 
rsegvcc1p=rsegvcc1/qbx3f

finalVCC=rsegvcc1p



