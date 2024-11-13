#5- Implementa en Python un algoritmo que reciba tres valores por teclado y los añade
#a la tupla:

#mi_tupla(x,y,z)
#Imprime la tupla por pantalla.

# Tupla original
mi_tupla = (1, 2, 3, "cuatro", "cinco")

# Leer tres valores desde el teclado
valor1 = input("Introduce el primer valor: ")
valor2 = input("Introduce el segundo valor: ")
valor3 = input("Introduce el tercer valor: ")

# Crear una nueva tupla con los valores añadidos
mi_tupla = mi_tupla + (valor1, valor2, valor3)

# Imprimir la nueva tupla
print("La nueva tupla es:", mi_tupla)
