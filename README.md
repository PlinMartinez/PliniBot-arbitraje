# PliniBot
# Esto es un bot de trading para publico de habla hispana
# Las funcionalidades a tener son todas las importantes para hacer buen crypto 
# un poco de backtesting, live trading, cargar datos, analisis tecnicos, deep learning, redes neuronales, grabar registro ventas , compatibilidad con señales, C++, R y HFT

# Tiene por un lado un fichero que busca en binance los arbitrajes entre 3 pares posibles
# Por otro lado tiene un wrapper de ordenes que lo junta con pandas para analizar la info

# si alguien quiere ayudar en la creacion de red mundial de bots escribir a manuelpaz@infopyme.com


#vamos a intentar que sea el mejor del mundo

(es multiexchange y multicamino)
EL ARBITRAJE TRIANGULAR SE COMPONE DE COMPRAS EUR/DOLAR, ESOS EUROS LOS CAMBIAS POR OTRA DIVISA Y LUEGO CRUZAS CON DOLARES Y VES SI HAS GANADO O PERDIDO DINERO
PARA HACER ESTO SE DESCOMPONE EN 3 PASOS
buscatriangulos.py le metes el listado de pares que tiene cualquier exchange y te saca (con tiempo) todas las triangulaciones que existen

Despues el triangular operaciones se puede hacer de 6 formas realmente, VCC,CVV, ... (lo estudias y entenderas), entonces el arbibot3single.py revisa cada camino (ojo con los decimales y compras minimas)

finalmente ya solo queda hacer un bot continuo para buscar oportunidades y lanzar compras segun donde lo necesites implementar

para un correcto desarrollo se va a estructurar el proyecto mediante mini servicios universales para ir componiendo una red universal de seguimiento de crypto monedas

la idea base es primero monitorizar todas las operaciones de todos los exchanges, despues analizar en detalle para ver si existe correlacion, ballenas actuando y/o arbitrajes existentes así como medir los tiempos de duracion

una vez analizado actuar en consecuencia, crear valor para los compradores aportando liquidez al sistema en aquellos casos que exista oportunidad de ganancia


reactivamos el asunto

