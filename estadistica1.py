import statistics as stats

edades = [22, 23, 26, 26, 34, 34, 38, 40, 41]

print(stats.pvariance(edades))

listado=[1,2,3,4,5,6,5,4,3,4,7,12,11,3,1,5]

print (len(listado))

maximos=[]
minimos=[]

for i in range(10):

	
	a=listado[i]
	b=listado[i+1]
	c=listado[i+2]
	print (a,b,c)

	if b > a and b > c:
		print('tocado maximo')
		maximos.append(b)
	if b < a and b < c:
		print('tocado minimo')
		minimos.append(b)

print('lista final')
print (maximos)
print(minimos)






