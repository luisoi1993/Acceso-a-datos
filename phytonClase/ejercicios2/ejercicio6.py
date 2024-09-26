#6. Crea un programa que simule un juego de adivinanza, donde el usuario debe
#adivinar un número aleatorio generado por la computadora.
#Input: número por teclado
#Output: Indicar si el número introducido es mayor o menor que el aleatorio.
#Import random #investiga sobre el funcionamiento de esta librería.

import random
numeroMaximo = int(input("Digite el numero maximo: "))
numeroAleatorio = random.randint(1, numeroMaximo)
print("El numero aleatorio es: ",numeroAleatorio)