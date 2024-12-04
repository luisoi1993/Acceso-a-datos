"""import random
import time

# Generar el tiempo límite entre 8 y 15 segundos
tiempo_limite = random.randint(8, 15)

# Generar el número aleatorio entre 1 y 100
numero_secreto = random.randint(1, 100)

# Mostrar mensaje inicial
print(f"Tienes {tiempo_limite} segundos para adivinar el número entre 1 y 100.")

# Guardar el tiempo de inicio
inicio_tiempo = time.time()

# Bucle para que el jugador intente adivinar el número
while True:
    # Verificar si el tiempo se ha acabado
    tiempo_actual = time.time()
    if tiempo_actual - inicio_tiempo > tiempo_limite:
        print(f"Se acabó el tiempo. El número era {numero_secreto}.")
        break

    # Pedir al usuario que introduzca un número
    try:
        intento = int(input("Adivina el número: "))
    except ValueError:
        print("Por favor, introduce un número válido.")
        continue

    # Comprobar si el intento es correcto
    if intento == numero_secreto:
        print("¡Felicidades! Has adivinado el número.")
        break
    elif intento < numero_secreto:
        print("El número es mayor.")
    else:
        print("El número es menor.")"""

import random 
import time

tiempo_limite = random.randint(8,15)

numero_secreto = random.randint(1, 100)

print(f"Tienes {tiempo_limite} segundos para adicinar el numero entre 1 y 100")

inicio_tiempo = time.time()

while True:
    tiempo_actual = time.time()
    if tiempo_actual - inicio_tiempo > tiempo_limite:
        print(f"Se acabo el tiempo. El  numero era {numero_secreto}")
        break

    try:
        intento = int(input("Adivina el numero : "))
    except ValueError:
        print("Por favor introduce un numero valido.")
        continue
    if intento == numero_secreto:
        print("Felicidades has adivinado el numero.")
        break
    elif intento < numero_secreto:
        print("El numero es mayor")
    else:
        print("El numero es menor")
