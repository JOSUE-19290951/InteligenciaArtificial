arch = open("pesosOr.txt","r")
pp = arch.read()
arch.close()

pesos = pp.split(",")
print(pesos)
x1 = int(input("Entrada 1: "))
x2 = int(input("Entrada 2: "))

sumaN = x1 * float(pesos[0]) +  x2 * float(pesos[1]) + float(pesos[2])

if sumaN > 0:
    salida = 1
else:
    salida = 0

print(f'{x1} , {x2} = {salida}')