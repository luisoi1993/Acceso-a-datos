#6. Realiza un programa que simule el juego de "Piedra, Papel o Tijeras" contra el
#ordenador.
import random

print("Bienvenido al juego de Piedra, Papel o Tijeras")

# Opciones del juego
opciones = {1: "Piedra", 2: "Papel", 3: "Tijeras"}

# Entrada del jugador
jugador = int(input("Selecciona: 1. Piedra, 2. Papel o 3. Tijeras: "))

# Validar la entrada del jugador
if jugador not in opciones:
    print("Selección no válida. Por favor elige 1, 2 o 3.")
else:
    # Generar la elección del ordenador
    aleatorio = random.randint(1, 3)
    
    # Mostrar las elecciones
    print(f"Has elegido: {opciones[jugador]}")
    print(f"El ordenador ha elegido: {opciones[aleatorio]}")
    
    # Determinar el ganador
    if jugador == aleatorio:
        print("¡Es un empate!")
    elif (jugador == 1 and aleatorio == 3) or (jugador == 2 and aleatorio == 1) or (jugador == 3 and aleatorio == 2):
        print("¡Has ganado!")
    else:
        print("¡El ordenador ha ganado!")