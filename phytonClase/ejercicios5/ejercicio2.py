import random
#Igual que el ejercicio 1, pero que ahora sea el ordenador quien introduzca al azar
#las coordenadas.



# Función para imprimir la matriz de forma legible usando doble for
def imprimir_matriz(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(matriz[i][j], end=" ")
        print()  # Nueva línea después de cada fila

# Crear la matriz 5x5 llena de ceros usando doble for
matriz = []
for i in range(5):
    fila = []
    for j in range(5):
        fila.append(0)
    matriz.append(fila)

# Generar dos números aleatorios entre 0 y 4 para las coordenadas
fila = random.randint(0, 4)
columna = random.randint(0, 4)

# Definir los movimientos adyacentes: arriba, abajo, izquierda, derecha y diagonales
movimientos = [
    (-1, 0), (1, 0), (0, -1), (0, 1),    # Movimientos cardinales
    (-1, -1), (-1, 1), (1, -1), (1, 1)   # Movimientos diagonales
]

# Colocar un 1 en la posición generada aleatoriamente
matriz[fila][columna] = 1

# Colocar un 1 en las posiciones adyacentes si están dentro de los límites de la matriz usando doble for
for movimiento in movimientos:
    nueva_fila = fila + movimiento[0]
    nueva_columna = columna + movimiento[1]
    
    # Comprobamos si las nuevas coordenadas están dentro de los límites de la matriz
    if 0 <= nueva_fila < len(matriz) and 0 <= nueva_columna < len(matriz[0]):
        matriz[nueva_fila][nueva_columna] = 1

# Imprimir la matriz resultante
print("\nMatriz resultante:")
imprimir_matriz(matriz)
