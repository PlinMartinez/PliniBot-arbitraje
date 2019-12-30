echo off
echo HOLA, VAMOS A HACER VARIAS OPERACIONES
echo PRIMERO VEMOS VOLATILIDAD CON FICHERO consultaOHLCV.py
echo DESPUES REVISAMOS CON ANALISIS_PANDAS.py
echo FINALMENTE EJECUTAMOS INICIO.py para empezar a trabajar con el que tenga >5 <20 volatilidad y 1 par solo
cd\
cd python
cd rmb
cd marketmaker
python saluda.py
echo ESTO PRIMERO MIDE LA VOLATILIDAD DE TODOS LOS PARES
python consultaOHLCV.py
echo ESTO DESPUES FILTRA LOS QUE TIENE MUCHA 
python analisis_PANDAS.py

