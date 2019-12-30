'''

REALIZA LAS ORDENES DE COMPRA CVV O VCC DE FORMA CONTINUADA A VER SI ALGO GANA

FUN/BTC,ETH/BTC,FUN/ETH,11.94,-15.92
REQ/BTC,ETH/BTC,REQ/ETH,12.65,-10.03
POWR/ETH,BNB/ETH,POWR/BNB,12.58,-7.09
AMB/BTC,BNB/BTC,AMB/BNB,12.68,-18.3
AMB/ETH,BNB/ETH,AMB/BNB,14.06,-18.75
BCPT/ETH,BNB/ETHCPT/BNB,10.26,-10.28
CDT/BTC,ETH/BTC,CDT/ETH,11.29,-4.54

HACEMOS EJEMPLO CON PSEUDOCODIGO A COMPLETAR Y PROBAR CON SALDO REAL EN OREGON 

'''

#SI PAR1 Q1 ES BTC O ETH, SI VA BIEN COMPRAR DE OTRAS TAMBIEN
def disparaVCC(par1, par2, par3):
    
    #par1 = 'FUN/BTC'
    #par2 = 'ETH/BTC'
    #par3 = 'FUN/ETH'

    b1 = par1.split('/')[0]
    print('b1 es ' + str(b1))
    q1 = par1.split('/')[1]
    print('q1 es ' + str(q1))
    b2 = par2.split('/')[0]
    print('b2 es ' + str(b2))
    q2 = par2.split('/')[1]
    print('q2 es ' + str(q2))
    b3 = par3.split('/')[0]
    print('b3 es ' + str(b3))
    q3 = par3.split('/')[1]
    print('q3 es ' + str(q3))


    #HACE LA PRIMERA ORDEN DE COMPRA A PRECIO DE MERCADO

    symbol1=par1
    type1='market'
    side1='buy'
    amount1=0	# ver como poner 30€ aprox
    # price = a precio de mercado
    # params = { 'type':'stoplimit', ... ....  }

    orden1=exchange.create_order(symbol1,type1,side1,amount1,price1,params1)

    #verifica orden hecha y saca saldo de b1
    #con el saldo de b1 vende par3 >>> -b3 +q3

    symbol2=par3
    type2='market'
    side2='sell'
    amount2=b1saldo	# ver como poner 30€ aprox
    # price = a precio de mercado
    # params = { 'type':'stoplimit', ... ....  }

    orden2=exchange.create_order(symbol2,type2,side2,amount2,price2,params2)

    #con el q3 obtenido vendelo TODO en b2 a ver cuanto q2 has conseguido


    symbol3=par2
    type2='market'
    side2='sell'
    amount2=q3saldo	# ver como poner 30€ aprox
    # price = a precio de mercado
    # params = { 'type':'stoplimit', ... ....  }

    orden3=exchange.create_order(symbol3,type3,side3,amount3,price3,params3)





    #si q2 > q1 >>> BIEN ERES COJONUDO
    #si q2 < q1 >>> MAL, ERES UN PARDILLO LENTORRO



   

if __name__ == '__main__':
	disparaCVV('FUN/BTC','ETH/BTC','FUN/ETH')
