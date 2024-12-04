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


Igual que anterior pero ahora, el usuario decide el número de unos que coloca y si
en horizontal o vertical a partir de las coordenadas que de forma aleatoria
selecciona el ordenador. Aquí hay una restricción, ya que el algoritmo tendrá que
ir buscando posiciones de forma aleatoria hasta que el número de unos indicado
por el usuario entre.
Ejemplo:
Si aleatoriamente salen las coordenadas (3,3) y el usuario quiere introducir 4 unos,
no es viable, ya que harían falta más de 5 filas o columnas para representarlo."""

import random

# Crear una matriz 5x5 llena de ceros
matriz = [[0 for _ in range(5)] for _ in range(5)]

# Mostrar la matriz actual
def mostrar_matriz(matriz):
    for fila in matriz:
        print(fila)
    print()

# Mostrar la matriz inicial
print("Matriz inicial:")
mostrar_matriz(matriz)

# Pedir al usuario el número de unos y la orientación
num_unos = int(input("Introduce el número de unos que quieres colocar: "))
orientacion = input("Introduce la orientación (horizontal/vertical): ").strip().lower()

# Validar orientación
if orientacion not in ["horizontal", "vertical"]:
    print("Orientación no válida. Intenta de nuevo.")
else:
    # Buscar una posición válida aleatoriamente
    while True:
        fila = random.randint(0, 4)
        columna = random.randint(0, 4)

        # Verificar si el número de unos cabe en la orientación seleccionada
        if orientacion == "horizontal" and columna + num_unos <= 5:
            for i in range(num_unos):
                matriz[fila][columna + i] = 1
            break
        elif orientacion == "vertical" and fila + num_unos <= 5:
            for i in range(num_unos):
                matriz[fila + i][columna] = 1
            break

# Mostrar la matriz resultante
print("Matriz resultante:")
mostrar_matriz(matriz)
