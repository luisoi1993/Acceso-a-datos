"""6. Cálculo de la suma de fila y columna en una matriz: Crea una matriz en la que cada
elemento sea la suma del número de fila y columna correspondiente. El usuario indicará
por teclado la dimensión de la matriz.
Ejemplo: para una matriz 2x2

01
12

Esto es por que en una matriz, las posiciones vienen dadas como un eje de coordenadas
de arriba a abajo y de izquierda a derecha (Ejemplo de matriz 2x2):

00 01
10 11"""

numero = int(input("Digite el tamaño de la matriz: "))

matriz = []

for i in range (numero):
    fila  = []
    for j in range (numero):
        suma = i + j
        fila.append(suma)
    matriz.append(fila)


print(matriz)

for fila in matriz:
    print(" ".join(map(str,fila)))