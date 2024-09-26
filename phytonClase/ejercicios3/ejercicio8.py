#8. Juego de la patata caliente. Si has visto el Grand Prix este verano sabrás más o menos
#de qué se trata, en caso contrario, te lo explico.

import random
import time

def juego_patata_caliente():
    tiempo_limite = random.randint(8, 15)
    numero_secreto = random.randint(1, 100)
    
    print(f"Tienes {tiempo_limite} segundos para adivinar el número entre 1 y 100.")
    
    tiempo_inicio = time.time()
    
    while True:
        try:
            adivina = int(input("Adivina el número: "))
        except ValueError:
            print("Introduce un número válido.")
            continue

        tiempo_actual = time.time()
        if tiempo_actual - tiempo_inicio > tiempo_limite:
            print(f"Se acabó el tiempo. El número era {numero_secreto}.")
            break
        
        if adivina < numero_secreto:
            print("El número es mayor.")
        elif adivina > numero_secreto:
            print("El número es menor.")
        else:
            print("¡Felicidades! Has adivinado el número.")
            break

juego_patata_caliente()
