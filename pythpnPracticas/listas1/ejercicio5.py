"""4b. Modifica el ejemplo anterior (4a) para que en lugar de ceros, introduzca
automáticamente (NO por teclado) los números impares que correspondan."""

# Solicita el tamaño de la matriz
numero = int(input("Digite el tamaño de la matriz: "))
impares = 1  # Primer número impar

# Inicializa una matriz vacía
matriz = []

# Llenar la matriz con números impares usando dos bucles anidados
for i in range(numero):
    fila = []  # Crea una nueva fila vacía
    for j in range(numero):
        fila.append(impares)  # Agrega el número impar a la fila
        impares += 2  # Incrementa al siguiente número impar
    matriz.append(fila)  # Agrega la fila completa a la matriz

# Imprimir la matriz
for fila in matriz:
    print(" ".join(map(str, fila)))

