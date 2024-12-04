#6. Crea un programa que simule un juego de adivinanza, donde el usuario debe
#adivinar un número aleatorio generado por la computadora.
#Input: número por teclado
#Output: Indicar si el número introducido es mayor o menor que el aleatorio.
#Import random #investiga sobre el funcionamiento de esta librería.

import random 

numero_aleatorio = random.randint(1, 100)

print("¡Bienvenido al juego de adivinanza!")
print("He pensado un número entre 1 y 100. ¿Puedes adivinar cual es?")

adivinado = False

while not adivinado:
    try:
        numero_usuario = int(input("Introduce un numero: "))
        if numero_usuario < numero_aleatorio:
            print("El numero que buscas es mayor.")
        elif numero_usuario > numero_aleatorio:
            print("El numero que buscas es menor")
        else:
            print(f"¡Felicidades! Has adivinado el numero: {numero_aleatorio}")
            adivinado = True
    except ValueError:
            print("Por favor, introduce un número válido.")
