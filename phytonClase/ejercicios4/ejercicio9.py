#9. Igual que el ejercicio 8 pero el usuario introduce los valores por teclado.

# Pide al usuario el tamaño de la matriz
numero = int(input("Introduce el tamaño de la matriz (n para n x n): "))

# Crear la matriz vacía
matriz = []

# Llenar la matriz con valores que ingresa el usuario
for i in range(numero):
    fila = []  # Fila vacía
    for j in range(numero):
        valor = int(input(f"Introduce el valor para la posición [{i}][{j}]: "))  # Valor de la posición
        fila.append(valor)  # Agrega el valor a la fila
    matriz.append(fila)  # Agrega la fila a la matriz

n = len(matriz)  # Tamaño de la matriz
suma_principal = 0  # Suma de la diagonal principal
suma_secundaria = 0  # Suma de la diagonal secundaria

# Bucle para sumar las diagonales
for i in range(n):
    suma_principal += matriz[i][i]  # Suma diagonal principal
    suma_secundaria += matriz[i][n - 1 - i]  # Suma diagonal secundaria

# Pregunta si se incluye el valor del centro
opcion = input("¿Deseas incluir el valor central dos veces en la suma? (sí/no): ").strip().lower()

# Si no se quiere incluir y la matriz es impar, quita el valor central
if opcion == "no" and n % 2 != 0:
    valor_central = matriz[n // 2][n // 2]  # Valor central de la matriz
    suma_secundaria -= valor_central  # Resta el valor central de la suma secundaria

# Calcula el resultado final
resultado = suma_principal + suma_secundaria
print(f"La suma de las diagonales es: {resultado}")  # Imprime el resultado