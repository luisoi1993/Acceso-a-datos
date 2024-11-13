#Igual que anterior pero ahora, el usuario decide el número de unos que coloca y si
#en horizontal o vertical a partir de las coordenadas que de forma aleatoria
#selecciona el ordenador. Aquí hay una restricción, ya que el algoritmo tendrá que
#ir buscando posiciones de forma aleatoria hasta que el número de unos indicado
#por el usuario entre.
#Ejemplo:
#Si aleatoriamente salen las coordenadas (3,3) y el usuario quiere introducir 4 unos,
#no es viable, ya que harían falta más de 5 filas o columnas para representarlo.

import random

def imprimir_matriz(matriz):
    for i in range(len(matriz)):  # Reemplazo de for predefinido para recorrer la matriz
        for j in range(len(matriz[i])):
            print(matriz[i][j], end=" ")
        print()

# Crear la matriz 5x5 llena de ceros usando doble for
matriz = []
for i in range(5):
    fila = []
    for j in range(5):
        fila.append(0)
    matriz.append(fila)

# Solicitar al usuario el número de unos que desea colocar
num_unos = int(input("¿Cuántos unos deseas colocar? (Entre 1 y 5): "))
while num_unos < 1 or num_unos > 5:
    num_unos = int(input("Por favor, elige un número entre 1 y 5: "))

# Solicitar al usuario la dirección (horizontal o vertical)
direccion = input("¿Quieres colocarlos en horizontal o vertical? (h/v): ").lower()
while direccion not in ["h", "v"]:
    direccion = input("Dirección no válida. Por favor, elige 'h' para horizontal o 'v' para vertical: ").lower()

# Función para verificar si es posible colocar los unos
def es_posible_colocar(fila, columna, direccion, num_unos):
    if direccion == "h":
        # Verificar si hay espacio en la fila hacia la derecha
        return columna + num_unos <= 5
    elif direccion == "v":
        # Verificar si hay espacio en la columna hacia abajo
        return fila + num_unos <= 5
    return False

# Buscar coordenadas aleatorias hasta que sea posible colocar los unos
fila, columna = random.randint(0, 4), random.randint(0, 4)
while not es_posible_colocar(fila, columna, direccion, num_unos):
    fila, columna = random.randint(0, 4), random.randint(0, 4)

# Colocar los unos en la matriz usando doble for
if direccion == "h":
    for i in range(num_unos):
        for j in range(len(matriz[fila])):  # Recorre la fila seleccionada
            if j == columna + i:
                matriz[fila][j] = 1
elif direccion == "v":
    for i in range(num_unos):
        for j in range(len(matriz)):  # Recorre la columna seleccionada
            if j == fila + i:
                matriz[j][columna] = 1

# Imprimir la matriz resultante
print("\nMatriz resultante:")
imprimir_matriz(matriz)