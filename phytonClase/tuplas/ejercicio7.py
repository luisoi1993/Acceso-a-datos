"""7- Implementa, usando un bucle for, la tupla ahora tenga el par de valores (a,b),
de forma que:

mi_tupla=((a,x),(b,y),(c,z))

donde a,b,c son letras introducidas por teclado y x,y,z son números.
El resultado al imprimir la tupla deber ser del tipo:

el valor a vale x,
el valor b vale y,
el valor c vale z

¡¡Sustituyendo cada uno de ellos por el valor introducido por teclado!!"""


pares = []


for i in range(3):
    letra = input(f"Introduce la letra {i+1}: ")

    # Verificamos que sea una sola letra
    while not (letra.isalpha() and len(letra) == 1):
        letra = input("Por favor, introduce una letra válida: ")

    numero = input(f"Introduce el número {i+1} para la letra '{letra}': ")

    # Verificamos que sea un número
    while not numero.isdigit():
        numero = input("Por favor, introduce un número válido: ")

    
    numero = int(numero)

    # Añadimos el par (letra, número) a la lista
    pares.append((letra, numero))

# Convertimos la lista de pares a una tupla
mi_tupla = tuple(pares)

for letra, numero in mi_tupla:
    print(f"El valor {letra} vale {numero}.")
