"""5- Implementa en Python un algoritmo que reciba tres valores por teclado y los añade
a la tupla:

mi_tupla(x,y,z)
Imprime la tupla por pantalla."""


mi_tupla = (1, 2, 3, "cuatro", "cinco")


x = input("Introduce el primer valor: ")
y = input("Introduce el segundo valor: ")
z = input("Introduce el tercer valor: ")

# Creamos una nueva tupla añadiendo los valores ingresados
mi_tupla = mi_tupla + (x, y, z)


print("La tupla actualizada es:", mi_tupla)
