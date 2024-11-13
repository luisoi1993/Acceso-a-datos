#opcion 1 funciona
#opcion 2 funciona toda
#opcion 3 funciona tocado y funciona hundido pero solo con la ultima posicion aveces 
#b cambiadas por numeros con colores


import random
import time
from colorama import Fore, Style

# Configuración del tablero
TAMANO_TABLERO = 10

# Barcos y sus tamaños
barcos = {
    4: 1,
    3: 2,
    2: 3,
    1: 4
}

# Colores y símbolos
COLOR_RESET = Style.RESET_ALL
COLOR_AGUA = Fore.BLUE
COLOR_TOCADO = Fore.YELLOW
COLOR_BARCO = Fore.GREEN
COLOR_NUMERO_BARCO = Fore.RED + Style.BRIGHT  # Color para los números de los barcos
COLOR_MENU = Fore.YELLOW
COLOR_TITULO = Fore.MAGENTA + Style.BRIGHT
COLOR_BLANCO = Fore.WHITE

SIMBOLO_AGUA = "0"
SIMBOLO_TOCADO = "T"
SIMBOLO_HUNDIDO = "H"
SIMBOLO_AGUA_ATACADA = "A"

# Crear tablero vacío
def crear_tablero():
    return [[SIMBOLO_AGUA] * TAMANO_TABLERO for _ in range(TAMANO_TABLERO)]

# Mostrar tablero
def mostrar_tablero(tablero, mostrar_barcos=True):
    print(f"\n    {COLOR_MENU}" + "   ".join(str(i) for i in range(TAMANO_TABLERO)) + f"{COLOR_RESET}")
    print("  +" + "────" * TAMANO_TABLERO + "+")
    for i, fila in enumerate(tablero):
        letra_fila = chr(ord('A') + i)
        fila_mostrar = " │ ".join(colorear_celda(celda, mostrar_barcos) for celda in fila)
        print(f"{COLOR_BLANCO}{letra_fila} │ {fila_mostrar} │{COLOR_RESET}")
        if i < TAMANO_TABLERO - 1:
            print("  ├" + "───┼" * (TAMANO_TABLERO - 1) + "───┤")
    print("  +" + "────" * TAMANO_TABLERO + "+")

# Colorear celdas para que sean más visibles
def colorear_celda(celda, mostrar_barcos):
    if celda == SIMBOLO_AGUA:
        return f"{COLOR_AGUA}{celda}{COLOR_RESET}"
    elif celda == SIMBOLO_TOCADO:
        return f"{COLOR_TOCADO}{celda}{COLOR_RESET}"
    elif celda == SIMBOLO_HUNDIDO:
        return f"{COLOR_TOCADO}{celda}{COLOR_RESET}"
    elif celda == SIMBOLO_AGUA_ATACADA:
        return f"{COLOR_AGUA}{celda}{COLOR_RESET}"
    elif celda in ['1', '2', '3', '4']:  # Si la celda es un número de barco
        return f"{COLOR_NUMERO_BARCO}{celda}{COLOR_RESET}"
    return celda

# Verifica si se puede colocar un barco en la posición deseada
def puedo_colocar_barco(tablero, tamano_barco, fila, col, direccion):
    if direccion == 'H':
        if col + tamano_barco > TAMANO_TABLERO:
            return False
        return all(tablero[fila][col + i] == SIMBOLO_AGUA for i in range(tamano_barco))
    else:
        if fila + tamano_barco > TAMANO_TABLERO:
            return False
        return all(tablero[fila + i][col] == SIMBOLO_AGUA for i in range(tamano_barco))

# Coloca el barco en el tablero
def colocar_barco(tablero, tamano_barco):
    colocado = False
    while not colocado:
        fila = random.randint(0, TAMANO_TABLERO - 1)
        col = random.randint(0, TAMANO_TABLERO - 1)
        direccion = random.choice(['H', 'V'])
        if puedo_colocar_barco(tablero, tamano_barco, fila, col, direccion):
            if direccion == 'H':
                for i in range(tamano_barco):
                    tablero[fila][col + i] = str(tamano_barco)  # Cambiado para mostrar el tamaño del barco
            else:
                for i in range(tamano_barco):
                    tablero[fila + i][col] = str(tamano_barco)  # Cambiado para mostrar el tamaño del barco
            colocado = True

# Configura el tablero con todos los barcos
def configurar_tablero():
    tablero = crear_tablero()
    for tamano_barco, cantidad in barcos.items():
        for _ in range(cantidad):
            colocar_barco(tablero, tamano_barco)
    return tablero

# Mostrar menú del juego
def mostrar_menu():
    print(f"\n{COLOR_MENU}==============================")
    print("        Menú de Batalla Naval")
    print("==============================")
    print(f"{COLOR_BLANCO}💥  1. Iniciar batalla (colocar barcos)")
    print(f"{COLOR_BLANCO}🎯  2. Elegir coordenadas para atacar")
    print(f"{COLOR_BLANCO}📡  3. Ataque recibido")
    print(f"{COLOR_BLANCO}🗺️  4. Visualizar mapas")
    print(f"{COLOR_BLANCO}🚪  5. Salir del juego{COLOR_RESET}")
    print("==============================")

# Convertir letras de columnas a índices
def letra_a_indice(fila):
    return ord(fila.upper()) - ord('A')

# Verifica si un barco está hundido
def esta_hundido(tablero, fila, col):
    # Comprobar celdas adyacentes
    for i in range(max(0, fila - 1), min(TAMANO_TABLERO, fila + 2)):
        for j in range(max(0, col - 1), min(TAMANO_TABLERO, col + 2)):
            if tablero[i][j] in ['1', '2', '3', '4']:  # Ajustado para comprobar los barcos
                return False
    return True

# Juego principal
def main():
    tablero_jugador = crear_tablero()
    tablero_ataque = crear_tablero()
    juego_iniciado = False

    print(f"{COLOR_TITULO}¡Bienvenido a Batalla Naval!{COLOR_RESET}")
    
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción (1-5): ")

        if opcion == '1':
            print("\nConfigurando tu tablero... ¡Listo para la batalla!")
            tablero_jugador = configurar_tablero()
            juego_iniciado = True
            print("Barcos colocados. ¡Que comience la batalla!")
            mostrar_tablero(tablero_jugador, mostrar_barcos=False)

        elif opcion == '2' and juego_iniciado:
            fila = input("Introduce columna (A-J) para atacar: ")
            col = int(input("Introduce fila (0-9) para atacar: "))
            fila_index = letra_a_indice(fila)

            resultado = input("¿Cuál fue el resultado (agua, tocado, hundido)?: ").strip().lower()
            if resultado == "agua":
                tablero_ataque[fila_index][col] = SIMBOLO_AGUA_ATACADA
            elif resultado == "tocado":
                tablero_ataque[fila_index][col] = SIMBOLO_TOCADO
            elif resultado == "hundido":
                tablero_ataque[fila_index][col] = SIMBOLO_HUNDIDO

            print("\nMapa de tus ataques:")
            mostrar_tablero(tablero_ataque, mostrar_barcos=False)

        elif opcion == '3' and juego_iniciado:
            fila = input("Tu compañero, introduce columna (A-J) que atacaste: ")
            col = int(input("Tu compañero, introduce fila (0-9) que atacaste: "))
            fila_index = letra_a_indice(fila)

            if tablero_jugador[fila_index][col] in ['1', '2', '3', '4']:  # Ajustado para comprobar barcos
                tablero_jugador[fila_index][col] = SIMBOLO_TOCADO
                print("Resultado del ataque: ¡Tocado!")
                # Comprobar si el barco está hundido
                if esta_hundido(tablero_jugador, fila_index, col):
                    print("¡Barco hundido!")
                    # Marcar la casilla como hundido
                    for j in range(TAMANO_TABLERO):
                        if tablero_jugador[fila_index][j] == SIMBOLO_TOCADO:
                            tablero_jugador[fila_index][j] = SIMBOLO_HUNDIDO
            else:
                tablero_jugador[fila_index][col] = SIMBOLO_AGUA_ATACADA
                print("Resultado del ataque: Agua.")

            print("\nTu mapa:")
            mostrar_tablero(tablero_jugador)

        elif opcion == '4':
            print("Mostrando el mapa actual:")
            mostrar_tablero(tablero_jugador)
            mostrar_tablero(tablero_ataque)

        elif opcion == '5':
            print("Saliendo del juego. ¡Hasta la próxima!")
            break

        else:
            print("Opción no válida. Por favor, selecciona de nuevo.")

if __name__ == "__main__":
    main()
