#1. Escribe un programa que calcule la suma de los 10 primeros números.
#Ayuda:
#En los bucles for, se puede definir un rango, el cual es una secuencia cerrada de
#números. Puedes generar un rango utilizando la función range().
#Ejemplo:
#for numero in range(1, 6): # Esto generará números del 1 al 5
#print(numero)

suma = 0

for numero in range(1, 10):
    suma = suma + numero

print(f"El resultado es : {suma}")