"""1. Escribe un programa que cree una matriz 5x5 llena de ceros.
El usuario deberá ingresar las coordenadas de una posición (fila, columna) por
teclado.
El programa deberá colocar un 1 en esa posición y también en todas las posiciones
adyacentes (arriba, abajo, izquierda, derecha, y diagonales), si estas posiciones
están dentro de los límites de la matriz.
Ejemplo:
Si el usuario ingresa la posición (2, 2), la matriz resultante será (los colores no
son necesarios):
[0, 0, 0, 0, 0]
[0, 1, 1, 1, 0]
[0, 1, 1, 1, 0]
[0, 1, 1, 1, 0]
[0, 0, 0, 0, 0]
2. Igual que el ejercicio 1, pero que ahora sea el ordenador quien introduzca al azar
las coordenadas.
"""
import random

# Crear una matriz 5x5 llena de ceros
matriz = [[0 for _ in range(5)] for _ in range(5)]

# Mostrar la matriz actual
def mostrar_matriz(matriz):
    for fila in matriz:
        print(fila)
    print()

# Generar coordenadas aleatorias
fila = random.randint(0, 4)
columna = random.randint(0, 4)
print(f"El ordenador seleccionó la posición: ({fila}, {columna})")

# Verificar si las coordenadas están dentro de los límites
if 0 <= fila < 5 and 0 <= columna < 5:
    # Colocar 1 en la posición seleccionada y en las adyacentes
    for i in range(fila - 1, fila + 2):  # Desde la fila anterior hasta la siguiente
        for j in range(columna - 1, columna + 2):  # Desde la columna anterior hasta la siguiente
            if 0 <= i < 5 and 0 <= j < 5:  # Comprobar límites de la matriz
                matriz[i][j] = 1
else:
    print("Coordenadas fuera de los límites. Inténtalo de nuevo.")

# Mostrar la matriz resultante
print("Matriz resultante:")
mostrar_matriz(matriz)
