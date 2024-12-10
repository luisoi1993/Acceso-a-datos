"""Para entender la recursividad, vamos a comprender las siguientes funciones matemáticas:
1- Calcula el factorial de un número
La formula para el calculo del factorial de un numero es N! = N * (N-1) .... 2 * 1.
La representación recursiva es:

Se puede mejorar desde el punto de vista de la programación si tenemos en cuenta
que el caso base también puede ser si x=1=0, pero entonces el caso recursivo le
tenemos que aumentar a x>1"""
def factorial(x):
    # Caso base
    if x == 0 or x == 1:
        return 1
    # Caso recursivo
    else:
        return x * factorial(x - 1)


numero = 5
print(f"El factorial de {numero} es: {factorial(numero)}")

