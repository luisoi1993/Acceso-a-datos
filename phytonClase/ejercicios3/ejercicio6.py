#Realiza un programa que simule el juego de "Piedra, Papel o Tijeras" contra el
#ordenador.

import random

def jugar():
    opciones = ['piedra', 'papel', 'tijeras']
    computadora = random.choice(opciones)

    jugador = input("Elige piedra, papel o tijeras: ").lower()

    print(f"Computadora eligió: {computadora}")

    if jugador == computadora:
        print("¡Es un empate!")
    elif (jugador == 'piedra' and computadora == 'tijeras') or \
         (jugador == 'papel' and computadora == 'piedra') or \
         (jugador == 'tijeras' and computadora == 'papel'):
        print("¡Ganaste!")
    else:
        print("¡Perdiste!")

jugar()