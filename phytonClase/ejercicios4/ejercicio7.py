#7. Dibujo de un rombo: Diseña un programa que dibuje un rombo equilibrado de
#asteriscos. El usuario debe ingresar la altura del rombo, siendo esta siempre impar. Si
#introduce una altura par, deberá indicar por pantalla que vuelva a introducir la altura
#(rombos con altura par...no son rombos equilibrados).


def dibujar_rombo(altura):
    # Verifica si la altura es par
    if altura % 2 == 0:
        print("Por favor, ingresa una altura impar.")  # Avísale que la altura no está bien
        return  # Sale de la función si la altura es par
    
    mitad = altura // 2  # Encuentra la mitad de la altura

    # Parte de arriba del rombo
    for i in range(mitad + 1):  # Dibuja la parte de arriba
        espacios = mitad - i  # Cantidad de espacios antes de los asteriscos
        asteriscos = 2 * i + 1  # Cantidad de asteriscos en cada línea
        print(" " * espacios + "*" * asteriscos)  # Imprime los espacios y los asteriscos

    # Parte de abajo del rombo
    for i in range(mitad - 1, -1, -1):  # Dibuja la parte de abajo
        espacios = mitad - i  # Espacios para la línea
        asteriscos = 2 * i + 1  # Asteriscos en la línea
        print(" " * espacios + "*" * asteriscos)  # Imprime los espacios y los asteriscos


while True:  # Bucle para pedir la altura hasta que sea impar
    altura = int(input("Introduce la altura del rombo (impar): "))  # Pide la altura
    if altura % 2 != 0:  # Verifica si la altura es impar
        break  # Sale del bucle si es impar
    print("La altura debe ser impar. Inténtalo de nuevo.")  # Si es par, pide que lo intente otra vez

dibujar_rombo(altura)  # Llama a la función para dibujar el rombo