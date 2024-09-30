#4a. Matriz de ceros: Escribe un programa que cree una matriz cuadrada de ceros de
#tamaño nxn, donde es el número de elementos de cada fila y columna y será
#especificado por el usuario (introducido por teclado).

numero = int(input("Introduce el tamaño de la matriz: "))  # Pide el tamaño de la matriz

# Creamos una matri de ceros n x n
matriz = [[0 for _ in range(numero)] for _ in range(numero)]  # Hacemos la matriz

# Mostramos la matriz fila por fila
for fila in matriz:
    print(fila)  # Imprime cada fila de la matriz