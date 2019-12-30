
import ccxt
import claves

par1='YOYOW/BTC'
par2='BNB/BTC'
par3='YOYOW/BNB'

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

print('Hola mundo V1.0')
print(par1)
mercados=exchange.load_markets(True)
libro_ordenes1 = exchange.fetch_order_book(par1,5)
libro_ordenes2 = exchange.fetch_order_book(par2,5)
libro_ordenes3 = exchange.fetch_order_book(par3,5)

pc1 = libro_ordenes1['asks'][0][0]
pv1 = libro_ordenes1['bids'][0][0]
pc2 = libro_ordenes2['asks'][0][0]
pv2 = libro_ordenes2['bids'][0][0]
pc3 = libro_ordenes3['asks'][0][0]
pv3 = libro_ordenes3['bids'][0][0]

minimo_notional1 = (mercados)[
            par1]['info']['filters'][3]['minNotional']
notional1 = float(minimo_notional1)
minimo_notional2 = (mercados)[
            par2]['info']['filters'][3]['minNotional']
notional2 = float(minimo_notional1)
minimo_notional3 = (mercados)[
            par3]['info']['filters'][3]['minNotional']
notional3 = float(minimo_notional1) 

#MODO CVV

bc1=notional1/pc1
qc1=notional1
bv2=notional1*pv3/pc1
qv2=notional1*pv3*pv2/pc1
bv3=notional1/pc1
qv3=notional1*pv3/pc1

b_CVV=qv2-notional1
b_porcentaje_CVV=round(b_CVV/qc1*100,2)
par1cfinal=bv3-bc1
par2vfinal=qv2-qc1
par3vfinal=qv3-bv2



#MODO VCC

bv1=notional1/pv1
qv1=notional1
bc2=notional1*pc3/pv1
qc2=notional1*pc3*pc2/pv1
bc3=notional1/pv1
qc3=bc2

b_VCC=qc2-notional1
b_porcentaje_VCC=round(b_VCC/qv1*100,2)
par1vfinal=bc3-bv1
par2cfinal=qc2-qv1
par3cfinal=qc3-bc2

venta1=bv1*pv1
compra2=bc2*pc2
compra3=bc3*pc3



base1=par1.split('/')[0]
quote1=par1.split('/')[1]
base2=par2.split('/')[0]
quote2=par2.split('/')[1]
base3=par3.split('/')[0]
quote3=par3.split('/')[1]

balance=exchange.fetch_balance()

saldob1=balance[base1]['free']
saldoq1=balance[quote1]['free']
saldob2=balance[base2]['free']
saldoq2=balance[quote2]['free']
saldob3=balance[base3]['free']
saldoq3=balance[quote3]['free']

saldoINICIOmoneda1=balance[base1]['free']
saldoINICIOmoneda2=balance[quote1]['free']
saldoINICIOmoneda3=balance[base2]['free']




if b_porcentaje_VCC>1:
    
    print('oportunidad de ganar +1% modo VCC')
    
    saldo_inicio=exchange.fetch_balance()[quote1]['free']
    
    print('Orden1 VENTA')
    symbol1= par1
    type= 'limit'
    side1v= 'sell'
    amount1v= round(bv1*1.2,6)
    price1v=  pv1
    orden1v= exchange.create_order(symbol1,type,side1v,amount1v,price1v)
    amount1ve=exchange.fetch_closed_orders(symbol1)[-1]['amount']
    average1ve=exchange.fetch_closed_orders(symbol1)[-1]['average']
    cost1ve=exchange.fetch_closed_orders(symbol1)[-1]['cost']
    
    print('Orden2 COMPRA')
    symbol2= par2
    type= 'limit'
    side2c= 'buy'
    amount2cpaso1=cost1ve/pc2
    amount2c= round(amount2cpaso1,6)-0.000001
    price2c=  pc2
    orden2c= exchange.create_order(symbol2,type,side2c,amount2c,price2c)
    amount2ce=exchange.fetch_closed_orders(symbol2)[-1]['amount']
    average2ce=exchange.fetch_closed_orders(symbol2)[-1]['average']
    cost2ce=exchange.fetch_closed_orders(symbol2)[-1]['cost']
        
    
    print('Orden3 COMPRA')
    symbol3= par3
    type= 'limit'
    side3c= 'buy'
    amount3cpaso1= amount2ce/pc3
    amount3c= round(amount3cpaso1,6)-0.000001
    price3c=  pc3
    orden3c= exchange.create_order(symbol3,type,side3c,amount3c,price3c)
    amount3ce=exchange.fetch_closed_orders(symbol3)[-1]['amount']
    average3ce=exchange.fetch_closed_orders(symbol3)[-1]['average']
    cost3ce=exchange.fetch_closed_orders(symbol3)[-1]['cost']
    
    saldo_fin= exchange.fetch_balance()[quote1]['free']
    
    balance=exchange.fetch_balance()
    
    saldoFINmoneda1=balance[base1]['free']
    saldoFINmoneda2=balance[quote1]['free']
    saldoFINmoneda3=balance[base2]['free']
    
    
        
    print('has ganado',b_VCC,par1)
    



if b_porcentaje_CVV>1:
    
    print('oportunidad de ganar +1% modo CVV')
    
    saldo_inicio=exchange.fetch_balance()[quote1]['free']
    
    print('Orden1 COMPRA')
    symbol1= par1
    type= 'limit'
    side1c= 'buy'
    amount1c= round(bc1*2,6)
    price1c=  pc1
    orden1c= exchange.create_order(symbol1,type,side1c,amount1c,price1c)
    amount1ce=exchange.fetch_closed_orders(symbol1)[-1]['amount']
    average1ce=exchange.fetch_closed_orders(symbol1)[-1]['average']
    cost1ce=exchange.fetch_closed_orders(symbol1)[-1]['cost']
    
    print('Orden3 VENTA')
    symbol3= par3
    type= 'limit'
    side3v= 'sell'
    amount3v= amount1ce
    price3v=  pv3
    orden3v= exchange.create_order(symbol3,type,side3v,amount3v,price3v)
    amount3ve=exchange.fetch_closed_orders(symbol3)[-1]['amount']
    average3ve=exchange.fetch_closed_orders(symbol3)[-1]['average']
    cost3ve=exchange.fetch_closed_orders(symbol3)[-1]['cost']
    
    print('Orden2 VENTA')
    symbol2= par2
    type= 'limit'
    side2v= 'sell'
    amount2v= cost3ve
    price2v=  pv2
    orden2= exchange.create_order(symbol2,type,side2v,amount2v,price2v)
    amount2ve=exchange.fetch_closed_orders(symbol2)[-1]['amount']
    average2ve=exchange.fetch_closed_orders(symbol2)[-1]['average']
    cost2ve=exchange.fetch_closed_orders(symbol2)[-1]['cost']
        
    saldo_fin= exchange.fetch_balance()[quote1]['free']
      
    print('inicias con', str(saldo_inicio))
    print('terminas con', str(saldo_fin))
    resultadofinalCVV=saldo_fin-saldo_inicio
    print ('TACHAN  ---->>>>> ' ,str(resultadofinalCVV))



contador = 0
datos=[]
datos.append('VCC CAMINO')
datos.append(str(saldob1))
datos.append(str(saldoq1))
datos.append(par1)
datos.append(str(bv1))
datos.append(str(pv1))
datos.append(str(qv1))
datos.append('----')

datos.append(str(saldob1))
datos.append(str(saldoq1))
datos.append(par2)
datos.append(str(bc2))
datos.append(str(pc2))
datos.append(str(qc2))
datos.append('----')

datos.append(str(saldob1))
datos.append(str(saldoq1))
datos.append(par3)
datos.append(str(bc3))
datos.append(str(pc3))
datos.append(str(qc3))


fichero='arbitraje.csv'
with open(fichero, 'w') as f:
    for i in datos:
        f.write(datos[contador])
        f.write('\n')

        contador = contador + 1
        print("linea grabada")
print("ok, grabado!!")

