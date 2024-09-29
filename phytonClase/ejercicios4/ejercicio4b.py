#4b. Modifica el ejemplo anterior (4a) para que en lugar de ceros, introduzca
#automáticamente (NO por teclado) los números impares que correspondan.
#Ejemplo: para la matriz cuadrada 2x2, sería:

#13
#57

numero = int(input("Introduce el tamaño de la matriz : "))
impar = int(1)

#crear una matri de 0 n x n
matriz = [[0 for _ in range(numero)] for _ in range (numero)]

for i in range(numero):
    for j in range(numero):
        matriz[i][j] = impar
        impar += 2

for fila in matriz:
    print(fila)