"""4c. Rellenando matrices. Amplía el ejercicio 4a de forma que el usuario no sólo decida
la dimensión de la matriz cuadrada sino que introduzca los datos (números enteros) por
teclado."""

# Solicita el tamaño de la matriz
numero = int(input("Digite el tamaño de la matriz: "))

# Inicializa una matriz vacía
matriz = []

# Llenar la matriz con números impares usando dos bucles anidados
for i in range(numero):
    fila = []  # Crea una nueva fila vacía
    for j in range(numero):
        numeros = int(input("Digite el numero para meter en el matriz "))
        fila.append(numeros)  # Agrega el número impar a la fila
    matriz.append(fila)  # Agrega la fila completa a la matriz

# Imprimir la matriz
for fila in matriz:
    print(" ".join(map(str, fila)))
