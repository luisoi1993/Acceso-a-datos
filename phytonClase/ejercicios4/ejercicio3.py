#3. Patrón de números: Diseña un programa que imprima un patrón de números en forma
#de cuadrado. Por ejemplo, si el usuario introduce por teclado el número 4, el patrón
#debería ser:


numeros = int(input("Digite el número: "))  # pedimos un número al usuario

# Empezamos el primer ciclo para las filas
for i in range(numeros):
    # Empezamos otro ciclo para los números de cada fila
    for j in range(1, numeros + 1):
        print(j, end="")  # Imprime el número sin saltar a la siguiente línea
    print()  # Hace un salto de línea después de cada fila