"""6- Implementa un algoritmo que lea por teclado dos valores y los añada a una tupla
con el siguiente formato:
mi_tupla(a,x)

donde a es una letra y x un número.
Imprime la tupla."""


a = input("Introduce una letra: ")

# Verificamos que el usuario haya ingresado una sola letra
while not (a.isalpha() and len(a) == 1):
    a = input("Por favor, introduce una letra válida: ")


x = input("Introduce un número: ")

# Verificamos que el valor ingresado sea un número
while not x.isdigit():
    x = input("Por favor, introduce un número válido: ")

# Convertimos el número a un entero
x = int(x)

# Creamos la tupla
mi_tupla = (a, x)

# Mostramos la tupla
print("La tupla creada es:", mi_tupla)
