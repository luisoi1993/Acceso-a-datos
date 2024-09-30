#8. Dada la siguiente matriz:
#[1, 2, 3, 4, 5],
#[6, 7, 8, 9, 10],
#[11, 12, 13, 14, 15],
#[16, 17, 18, 19, 20],
#[21, 22, 23, 24, 25]

#implementa un algoritmo en python que realice la suma de sus diagonales, es decir,
#que sume (1+7+13+19+20)+(21+17+13+9+5). Si te fijas el 13 se repite, puedes dar la
#opción que el usuario decida si se da el resultado repitiendo el elemento central o no.
# Definimos la matriz



# Definimos la matriz
matriz = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25]
]

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
    suma_secundaria -= valor_central   # Resta el valor central de la suma secundaria

# Calcula el resultado final
resultado = suma_principal + suma_secundaria
print(f"La suma de las diagonales es: {resultado}")  # Imprime el resultado