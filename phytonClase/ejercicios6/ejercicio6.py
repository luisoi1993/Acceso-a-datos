#6- Implementa un algoritmo que lea por teclado dos valores y los añada a una tupla
#con el siguiente formato:
#mi_tupla(a,x)

#donde a es una letra y x un número.
#Imprime la tupla.

# Leer una letra desde el teclado
a = input("Introduce una letra: ")

# Leer un número desde el teclado y convertirlo a entero
x = input("Introduce un número: ")

# Verificar que 'x' es un dígito antes de convertirlo
if x.isdigit():
    x = int(x)
else:
    print("Error: el valor ingresado no es un número.")
    x = None

# Crear la tupla si el valor de 'x' es correcto
if x is not None:
    mi_tupla = (a, x)
    print("La tupla es:", mi_tupla)
