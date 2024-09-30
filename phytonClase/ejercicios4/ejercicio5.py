#5. Suma de matrices: amplía el ejercicio 4c con un programa que sume dos matrices
#cuadradas con el mismo orden. Todos los datos de la suma son números enteros.
#Os recuerdo que para sumar matrices es sumar los elementos que ocupan la misma
#posición en ambas matrices.
#Ejemplo: Matriz 1 Matriz 2 Matriz suma
#01 56 0+5 1+6 5 7
#+ = =
#23 78 2+7 3+8 9 15


numero = int(input("Introduce el tamaño de las matrices: "))  # Pide el tamaño de las matrices

# Crear las matrices con los valores que pone el usuario
matriz1 = [[int(input(f"Introduce el valor para la posición [{i}][{j}] de la Matriz 1: ")) for j in range(numero)] for i in range(numero)]  # Matriz 1
matriz2 = [[int(input(f"Introduce el valor para la posición [{i}][{j}] de la Matriz 2: ")) for j in range(numero)] for i in range(numero)]  # Matriz 2

# Crear una matri de ceros para la suma
matriz_suma = [[0 for _ in range(numero)] for _ in range(numero)]  # Matriz de suma

# Sumar las dos matrices
for i in range(numero):
    for j in range(numero):
        matriz_suma[i][j] = matriz1[i][j] + matriz2[i][j]  # Sumar cada posición

print("\nMatriz suma:")  # Imprime el resultado de la suma
for fila in matriz_suma:
    print(fila)  # Muestra cada fila de la matriz suma