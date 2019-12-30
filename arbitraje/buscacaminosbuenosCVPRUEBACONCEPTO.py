
# TOMA 3 PARES

par1 = 'ADA/BTC'
par2 = 'ETH/BTC'
par3 = 'ADA/ETH'

# SEPARA LA BASE DEL QUOTE

separa1 = par1.split('/')
separa2 = par2.split('/')
separa3 = par3.split('/')

b1 = separa1[0]
q1 = separa1[1]
b2 = separa1[0]
q2 = separa1[1]
b3 = separa1[0]
q3 = separa1[1]

# ANALIZA LAS OPCIONES CCC, CCV, ..., CVV

# opcion1 compra par1 , compra par 2, compra par 3

b1 = b2 = b3 = q1 = q2 = q3 = 0

print(b1)


b1 = +1
q1 = -1
b2 = +1
q2 = -1
b3 = +1
q3 = -1  # CCC

r1 = (b1 + b3)
r2 = (q1 + q2)
r3 = (b2 + q3)

print(r1)
print(r2)
print(r3)

if r1 == 0 and r2 == 0 and r3 == 0:

    print("va bien 1")


b1 = b2 = b3 = q1 = q2 = q3 = 0
b1 = +1
q1 = -1
b2 = +1
q2 = -1
b3 = -1
q3 = +1  # CCV
r1 = (b1 + b3)
r2 = (q1 + q2)
r3 = (b2 + q3)

print(r1)
print(r2)
print(r3)

if r1 == 0 and r2 == 0 and r3 == 0:

    print("va bien 2")

b1 = b2 = b3 = q1 = q2 = q3 = 0
b1 = +1
q1 = -1
b2 = -1
q2 = +1
b3 = +1
q3 = -1  # CVC
r1 = (b1 + b3)
r2 = (q1 + q2)
r3 = (b2 + q3)

print(r1)
print(r2)
print(r3)

if r1 == 0 and r2 == 0 and r3 == 0:

    print("va bien 3")
b1 = b2 = b3 = q1 = q2 = q3 = 0
b1 = +1
q1 = -1
b2 = -1
q2 = +1
b3 = -1
q3 = +1  # CVV
r1 = (b1 + b3)
r2 = (q1 + q2)
r3 = (b2 + q3)

print(r1)
print(r2)
print(r3)

if r1 == 0 and r2 == 0 and r3 == 0:

    print("va bien 4")
b1 = b2 = b3 = q1 = q2 = q3 = 0
b1 = -1
q1 = +1
b2 = +1
q2 = -1
b3 = +1
q3 = -1  # VCC
r1 = (b1 + b3)
r2 = (q1 + q2)
r3 = (b2 + q3)

print(r1)
print(r2)
print(r3)

if r1 == 0 and r2 == 0 and r3 == 0:

    print("va bien 5")
b1 = b2 = b3 = q1 = q2 = q3 = 0
b1 = -1
q1 = +1
b2 = +1
q2 = -1
b3 = -1
q3 = +1  # VCV
r1 = (b1 + b3)
r2 = (q1 + q2)
r3 = (b2 + q3)

print(r1)
print(r2)
print(r3)

if r1 == 0 and r2 == 0 and r3 == 0:

    print("va bien 6")
b1 = b2 = b3 = q1 = q2 = q3 = 0
b1 = -1
q1 = +1
b2 = -1
q2 = +1
b3 = +1
q3 = -1  # VVC
r1 = (b1 + b3)
r2 = (q1 + q2)
r3 = (b2 + q3)

print(r1)
print(r2)
print(r3)

if r1 == 0 and r2 == 0 and r3 == 0:

    print("va bien 7")
b1 = b2 = b3 = q1 = q2 = q3 = 0
b1 = -1
q1 = +1
b2 = -1
q2 = +1
b3 = -1
q3 = +1  # VVV
r1 = (b1 + b3)
r2 = (q1 + q2)
r3 = (b2 + q3)

print(r1)
print(r2)
print(r3)

if r1 == 0 and r2 == 0 and r3 == 0:

    print("va bien 8")

# RESULTADO CVV O VCC VALEN
