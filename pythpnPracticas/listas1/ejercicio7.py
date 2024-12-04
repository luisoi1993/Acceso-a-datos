"""5. Suma de matrices: amplía el ejercicio 4c con un programa que sume dos matrices
cuadradas con el mismo orden. Todos los datos de la suma son números enteros.
Os recuerdo que para sumar matrices es sumar los elementos que ocupan la misma
posición en ambas matrices.
Ejemplo: Matriz 1 Matriz 2 Matriz suma
01 56 0+5 1+6 5 7
+ = =
23 78 2+7 3+8 9 15"""
# Solicita el tamaño de la matriz
numero = int(input("Digite el tamaño de la matriz: "))

# Inicializa una matriz vacía
matriz = []
matriz2 = []
matriz_final = []

# Llenar la matriz con números impares usando dos bucles anidados
for i in range(numero):
    fila = []  # Crea una nueva fila vacía
    for j in range(numero):
        numeros = int(input("Digite el numero para meter en el matriz "))
        fila.append(numeros)  # Agrega el número impar a la fila
    matriz.append(fila)  # Agrega la fila completa a la matriz

    # Llenar la matriz con números impares usando dos bucles anidados
for i in range(numero):
    fila = []  # Crea una nueva fila vacía
    for j in range(numero):
        numeros = int(input("Digite el numero para meter en el matriz "))
        fila.append(numeros)  # Agrega el número impar a la fila
    matriz2.append(fila)  # Agrega la fila completa a la matriz

# Llenar la matriz con números impares usando dos bucles anidados
for i in range(numero):
    fila = []  # Crea una nueva fila vacía
    for j in range(numero):
        numeros = matriz[i][j] + matriz2[i][j]
        fila.append(numeros)  # Agrega el número impar a la fila
    matriz_final.append(fila)  # Agrega la fila completa a la matriz

# Imprimir la matriz
for fila in matriz_final:
    print(" ".join(map(str, fila)))

"""version mejorada de chat gpt # Función para solicitar datos y llenar una matriz cuadrada
def llenar_matriz(tamano, nombre):
    print(f"\nLlenando la {nombre}:")
    matriz = []
    for i in range(tamano):
        fila = []
        for j in range(tamano):
            while True:
                try:
                    numero = int(input(f"Digite el número para la posición ({i+1}, {j+1}) de la {nombre}: "))
                    fila.append(numero)
                    break
                except ValueError:
                    print("Entrada inválida. Por favor, introduzca un número entero.")
        matriz.append(fila)
    return matriz

# Función para sumar dos matrices cuadradas
def sumar_matrices(matriz1, matriz2):
    tamano = len(matriz1)
    matriz_suma = []
    for i in range(tamano):
        fila = []
        for j in range(tamano):
            fila.append(matriz1[i][j] + matriz2[i][j])
        matriz_suma.append(fila)
    return matriz_suma

# Imprimir una matriz
def imprimir_matriz(matriz, nombre):
    print(f"\n{name}:")
    for fila in matriz:
        print(" ".join(map(str, fila)))

# Solicitar el tamaño de las matrices
while True:
    try:
        numero = int(input("Digite el tamaño de las matrices cuadradas: "))
        if numero > 0:
            break
        else:
            print("El tamaño debe ser un número mayor a 0.")
    except ValueError:
        print("Entrada inválida. Por favor, introduzca un número entero positivo.")

# Crear las matrices
matriz1 = llenar_matriz(numero, "Matriz 1")
matriz2 = llenar_matriz(numero, "Matriz 2")

# Calcular la suma de las matrices
matriz_suma = sumar_matrices(matriz1, matriz2)

# Mostrar las matrices
imprimir_matriz(matriz1, "Matriz 1")
imprimir_matriz(matriz2, "Matriz 2")
imprimir_matriz(matriz_suma, "Matriz Suma")

"""