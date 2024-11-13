#7- Implementa, usando un bucle for, la tupla ahora tenga el par de valores (a,b),
#de forma que:

#mi_tupla=((a,x),(b,y),(c,z))

#donde a,b,c son letras introducidas por teclado y x,y,z son números.
#El resultado al imprimir la tupla deber ser del tipo:

#el valor a vale x,
#el valor b vale y,
#el valor c vale z

#¡¡Sustituyendo cada uno de ellos por el valor introducido por teclado!!
#mi_tupla=((a,x),(b,y),(c,z))

# Inicializamos una lista para almacenar los pares temporales
pares = []

# Pedimos los valores en un bucle for
for i in range(3):
    letra = input(f"Introduce la letra {i + 1}: ")
    numero = input(f"Introduce el número {i + 1}: ")
    
    # Convertir 'numero' a entero si es un dígito
    if numero.isdigit():
        numero = int(numero)
    else:
        print("Error: el valor ingresado no es un número.")
        break
    
    # Añadir el par (letra, numero) a la lista de pares
    pares.append((letra, numero))

# Convertir la lista de pares en una tupla
mi_tupla = tuple(pares)

# Imprimir la tupla resultante
print("La tupla resultante es:", mi_tupla)
