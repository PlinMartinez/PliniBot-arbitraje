'''
from datetime import datetime

now = datetime.now()

current_time = now.strftime("%H:%M:%S")
print("Current Time =", current_time)



import time

t = time.localtime()
current_time = time.strftime("%H:%M:%S", t)
print(current_time)


'''

from datetime import datetime
import pytz




fecha=datetime.now()
print(fecha.strftime("%Y-%m-%d"))

solucion=fecha.strftime("%Y-%m-%d")

print (solucion)
print (type(solucion))