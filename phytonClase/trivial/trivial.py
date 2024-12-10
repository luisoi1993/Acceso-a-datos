import random

# Colores asignados a los jugadores
COLORES = ["azul", "rojo", "verde", "amarillo"]

# Función para calcular la puntuación final del juego
def calcular_puntuaciones():
    # Solicitar el número de jugadores
    num_jugadores = int(input("Número de jugadores (máximo 4): "))
    while num_jugadores < 1 or num_jugadores > 4:
        print("El número de jugadores debe estar entre 1 y 4.")
        num_jugadores = int(input("Número de jugadores (máximo 4): "))

    # Inicializar los jugadores con puntos aleatorios
    jugadores = {}
    for i in range(num_jugadores):
        jugador = COLORES[i]
        puntos_iniciales = random.randint(50, 70)
        jugadores[jugador] = {
            "puntos": puntos_iniciales,
            "preguntas": []  # Lista para registrar las preguntas y respuestas
        }

    # Mostrar los puntos iniciales
    print("\nPuntos iniciales de los jugadores:")
    for jugador, datos in jugadores.items():
        print(f"Jugador {jugador}: {datos['puntos']} puntos")

    # Turnos y preguntas
    OPCIONES = ["A", "B", "C", "D"]
    for turno in range(1, 5):  # Cuatro turnos por jugador
        print(f"\nTurno {turno}:")
        for jugador, datos in jugadores.items():
            respuesta_correcta = random.choice(OPCIONES)
            print(f"* Pregunta: ¿Cuál es la respuesta a '{respuesta_correcta}'? (Jugador {jugador})")
            respuesta_jugador = input("Responde (A/B/C/D): ").strip().upper()

            # Validar la respuesta del jugador
            while respuesta_jugador not in OPCIONES:
                print("Respuesta inválida. Por favor responde con A, B, C o D.")
                respuesta_jugador = input("Responde (A/B/C/D): ").strip().upper()

            # Evaluar la respuesta
            if respuesta_jugador == respuesta_correcta:
                print("Respuesta correcta. Has ganado 5 puntos.")
                jugadores[jugador]["puntos"] += 5
            else:
                print("Respuesta incorrecta. Has perdido 5 puntos.")
                jugadores[jugador]["puntos"] -= 5

            # Registrar la pregunta y respuesta
            jugadores[jugador]["preguntas"].append((respuesta_correcta, respuesta_jugador))

    # Mostrar resultados finales
    print("\nResultados finales:")
    ganador = None
    max_puntos = float("-inf")
    for jugador, datos in jugadores.items():
        print(f"\nJugador {jugador}:")
        print(f"Puntos finales: {datos['puntos']}")
        if datos["puntos"] > max_puntos:
            max_puntos = datos["puntos"]
            ganador = jugador

    # Anunciar al ganador
    print(f"\n!!!!!!!!!!!!!!! Gana jugador {ganador} !!!!!!!!!!!!!!!!")

# Ejecutar el programa
if __name__ == "__main__":
    calcular_puntuaciones()
