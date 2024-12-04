#9. Igual que el ejercicio 8 pero el usuario introduce los valores por teclado.
# Definir la matriz
matriz = []

for i in range(5):
    linea = []  # Crea una nueva lista para cada fila
    for j in range(5):
        numero = int(input(f"Digite el numero {i} {j}: "))
        linea.append(numero)  # Agrega el número a la fila actual
    matriz.append(linea)  # Agrega la fila completa a la matriz


# Inicializar variables para las sumas de las diagonales
suma_diagonal_principal = 0
suma_diagonal_secundaria = 0
tamaño = len(matriz)

# Calcular las sumas de las diagonales
for i in range(tamaño):
    suma_diagonal_principal += matriz[i][i]  # Elementos de la diagonal principal
    suma_diagonal_secundaria += matriz[i][tamaño - i - 1]  # Elementos de la diagonal secundaria

# Preguntar al usuario si el elemento central debe repetirse en la suma
repetir_central = input("¿Desea repetir el elemento central (13) en la suma? (sí/no): ").strip().lower()

if repetir_central == "no":
    elemento_central = matriz[tamaño // 2][tamaño // 2]  # Elemento central
    suma_total = suma_diagonal_principal + suma_diagonal_secundaria - elemento_central
else:
    suma_total = suma_diagonal_principal + suma_diagonal_secundaria

# Mostrar resultados
print(f"Suma de la diagonal principal: {suma_diagonal_principal}")
print(f"Suma de la diagonal secundaria: {suma_diagonal_secundaria}")
print(f"Suma total de las diagonales: {suma_total}")

