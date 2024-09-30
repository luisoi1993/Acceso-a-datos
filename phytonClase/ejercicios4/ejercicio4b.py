#4b. Modifica el ejemplo anterior (4a) para que en lugar de ceros, introduzca
#automáticamente (NO por teclado) los números impares que correspondan.
#Ejemplo: para la matriz cuadrada 2x2, sería:

#13
#57


numero = int(input("Introduce el tamaño de la matriz: "))  # Pide el tamaño de la matriz
impar = int(1)  # Empezamos con el primer número impar

# Creamos una matri de ceros n x n
matriz = [[0 for _ in range(numero)] for _ in range(numero)]  # Hacemos la matriz

# Llenamos la matriz con números impares
for i in range(numero):
    for j in range(numero):
        matriz[i][j] = impar  # Ponemos el número impar en la posición
        impar += 2  # Aumentamos para el siguiente impar

# Mostramos la matriz fila por fila
for fila in matriz:
    print(fila)  # Imprime cada fila de la matriz