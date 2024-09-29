#3. Patrón de números: Diseña un programa que imprima un patrón de números en forma
#de cuadrado. Por ejemplo, si el usuario introduce por teclado el número 4, el patrón
#debería ser:

numeros = int(input("Digite el número: "))

for i in range(numeros):
    for j in range(1, numeros + 1):
        print(j, end="")  # Imprime el número sin salto de línea
    print()  # Salto de línea después de cada fila


