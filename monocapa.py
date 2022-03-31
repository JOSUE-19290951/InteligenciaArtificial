import random as rnd
import numpy as np

neuronas = 3
entradas = 8
#pE = np.array([[1,1,1],[1,0,1],[0,1,1],[0,0,1]])
pE = np.array([[1,1,1,1,1,1,0,1],
               [0,1,1,0,0,0,0,1],
               [1,1,0,1,1,0,1,1],
               [1,1,1,1,0,0,1,1],
               [0,1,1,0,0,1,1,1],
               [1,0,1,1,0,1,1,1],
               [1,0,1,1,1,1,1,1],
               [1,1,1,0,0,0,1,1],
               [1,1,1,1,1,1,1,1],
               [1,1,1,0,0,1,1,1]])
sE = np.array([[1,0,0],
               [0,0,0],
               [1,1,0],
               [0,1,0],
               [1,0,0],
               [0,1,0],
               [1,0,1],
               [0,1,1],
               [1,0,1],
               [0,0,1]])
#sE = np.array([[0,0],[0,1],[1,0],[1,1]])

pesos = np.array([[rnd.random() * 10 for i in range(entradas)]for j in range(neuronas)])
aprendiendo = True
salida = np.zeros(neuronas)
error = np.zeros(neuronas)
epocas = 0
tasa = 0.3
while aprendiendo:
    aprendiendo = False
    i=0
    for i in range(len(pE)):
        ii = 0
        j = 0
        sumaN = np.zeros(neuronas)
        for ii in range(neuronas):
            for j in range(entradas):
                sumaN[ii] += pesos[ii][j] * pE[i][j]
        for s in range(neuronas):
            if sumaN[s] > 0:
                salida[s] = 1
            else:
                salida[s] = 0
        for s in range(neuronas):
            error[s] = sE[i][s] - salida[s]
            if error[s] != 0:
                aprendiendo = True
                print("Aprendiendo")
                for jj in range(entradas):
                    pesos[s][jj] += tasa * error[s] * pE[i][jj]
    epocas += 1

for i in range(len(pE)):
    ii = 0
    j = 0
    sumaN = np.zeros(neuronas)
    for ii in range(neuronas):
        for j in range(entradas):
            sumaN[ii] += pesos[ii][j] * pE[i][j]
    for s in range(neuronas):
        if sumaN[s] > 0:
            salida[s] = 1
        else:
            salida[s] = 0
    print(f'{pE[i][0]}, {pE[i][1]}, {sE[i][0]}, {sE[i][1]}, perceptron = {salida[0]},{salida[1]}')

print("Epocas: ", epocas)
print("Neuronas: ", neuronas)
cad = ""
for i in range(neuronas):
    for j in range(entradas):
        cad += str(pesos[i][j]) +  ","

arch = open('pesosNotG.txt', "w")
arch.write(cad[:len(cad)-1])
arch.close()

