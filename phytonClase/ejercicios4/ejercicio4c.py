#4c. Rellenando matrices. Amplía el ejercicio 4a de forma que el usuario no sólo decida
#la dimensión de la matriz cuadrada sino que introduzca los datos (números enteros) por
#teclado.

numero = int(input("Introduce el tamaño de la matriz: "))  # Pide el tamaño de la matriz

# Crear una matri de ceros n x n
matriz = [[0 for _ in range(numero)] for _ in range(numero)]  # Hacemos la matriz

# Llenamos la matriz con los números que el usuario introduce
for i in range(numero):
    for j in range(numero):
        matriz[i][j] = input(f"Digite el valor de posicion [{i}][{j}]: ")  # Pide el número para cada posición

# Mostramos la matriz fila por fila
for fila in matriz:
    print(fila)  # Imprime cada fila de la matriz