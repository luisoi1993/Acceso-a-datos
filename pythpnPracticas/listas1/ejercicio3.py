"""3. Patrón de números: Diseña un programa que imprima un patrón de números en forma
de cuadrado. Por ejemplo, si el usuario introduce por teclado el número 4, el patrón
debería ser:
1234
1234
1234
1234
Si se ingresa el 2, sería:
12
12"""

# Solicitar el número al usuario
numero = int(input("Introduce un número: "))

# Bucle para las filas
for i in range(numero):
    # Crear y mostrar cada fila con los números del 1 al número ingresado
    for j in range(1, numero + 1):
        print(j, end="")  # Imprimir números en la misma línea
    print()  # Nueva línea después de cada fila
