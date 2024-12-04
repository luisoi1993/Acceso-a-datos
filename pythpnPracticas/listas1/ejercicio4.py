"""4a. Matriz de ceros: Escribe un programa que cree una matriz cuadrada de ceros de
tamaño nxn, donde es el número de elementos de cada fila y columna y será
especificado por el usuario (introducido por teclado).
Ejemplo: Si el usuario escribe un 2, la matriz 2x2 sería:

00
00"""

# Solicita el tamaño de la matriz
numero = int(input("Digite el tamaño de la matriz de ceros: "))

# Inicializa una matriz vacía
matriz = []

# Llenar la matriz con ceros usando dos bucles anidados
for i in range(numero):
    fila = []  # Crea una nueva fila vacía
    for j in range(numero):
        fila.append(0)  # Agrega un 0 a la fila
    matriz.append(fila)  # Agrega la fila completa a la matriz

# Imprimir la matriz
for fila in matriz:
    print(" ".join(map(str, fila)))
