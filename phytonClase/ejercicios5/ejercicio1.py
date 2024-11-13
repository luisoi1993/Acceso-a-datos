#Escribe un programa que cree una matriz 5x5 llena de ceros.
#El usuario deberá ingresar las coordenadas de una posición (fila, columna) por
#teclado.
#El programa deberá colocar un 1 en esa posición y también en todas las posiciones
#adyacentes (arriba, abajo, izquierda, derecha, y diagonales), si estas posiciones
#están dentro de los límites de la matriz.


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

# Solicitar al usuario las coordenadas de la posición
fila = int(input("Ingresa la fila (0-4): "))
columna = int(input("Ingresa la columna (0-4): "))

# Definir los movimientos adyacentes: arriba, abajo, izquierda, derecha y diagonales
movimientos = [
    (-1, 0), (1, 0), (0, -1), (0, 1),    # Movimientos cardinales
    (-1, -1), (-1, 1), (1, -1), (1, 1)   # Movimientos diagonales
]

# Colocar un 1 en la posición ingresada por el usuario
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
