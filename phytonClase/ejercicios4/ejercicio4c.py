#4c. Rellenando matrices. Amplía el ejercicio 4a de forma que el usuario no sólo decida
#la dimensión de la matriz cuadrada sino que introduzca los datos (números enteros) por
#teclado.

numero = int(input("Introduce el tamaño de la matriz : "))


#crear una matri de 0 n x n
matriz = [[0 for _ in range(numero)] for _ in range (numero)]

for i in range(numero):
    for j in range(numero):
        matriz[i][j] = input(f"Digite el valor de posicion [{i}] + [{j}]")
    

for fila in matriz:
    print(fila)