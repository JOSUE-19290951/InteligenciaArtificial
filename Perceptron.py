import numpy as np
from random import random

p = np.array([[0,0,1],[0,1,1],[1,0,1],[1,1,1]])   #patron de entradas que incluye el bias

SE = np.array([0,1,1,1]) #Salidad esperadas

w = np.array([random()*10,random()*10,random()*10]) #peso que incluye el bias

aprendiendo = True

tasaA = 0.3
epocas = 0
salida = 0

while aprendiendo:
    aprendiendo = False
    for i in range(len(p)):
        sumaN = 0
        for j in range(len(p[i])):
            sumaN += p[i][j] * w[j]
        if sumaN > 0:
            salida = 1
        else:
            salida = 0
        error = SE[i]-salida
        if error != 0:
            for j in range(len(w)):
                w[j]+= tasaA * error * p[i][j]
            aprendiendo = True
    print("Aprendiendo")
    epocas += 1

for i in range(len(p)):
    sumaN = 0
    for j in range(len(p[i])):
        sumaN += p[i][j] * w[j]
    if sumaN > 0:
        salida = 1
    else:
        salida = 0
    print(f'{p[i][0]}, {p[i][1]} = {SE[i]}, Perceptron = {salida}')

print("Epocas = ", epocas)
cad = ""
for i in range(len(w)):
    cad += str(w[i])+","
cad = cad[:len(cad)-1]
arch = open("pesosOr.txt", "w")
arch.write(cad)
arch.close()

