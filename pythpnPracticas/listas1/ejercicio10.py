"""8. Dada la siguiente matriz:
[1, 2, 3, 4, 5],
[6, 7, 8, 9, 10],
[11, 12, 13, 14, 15],
[16, 17, 18, 19, 20],
[21, 22, 23, 24, 25]

implementa un algoritmo en python que realice la suma de sus diagonales, es decir,
que sume (1+7+13+19+20)+(21+17+13+9+5). Si te fijas el 13 se repite, puedes dar la
opción que el usuario decida si se da el resultado repitiendo el elemento central o no."""

# Definir la matriz
matriz = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25]
]

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

