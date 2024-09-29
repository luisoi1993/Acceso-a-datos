#7. Dibujo de un rombo: Diseña un programa que dibuje un rombo equilibrado de
#asteriscos. El usuario debe ingresar la altura del rombo, siendo esta siempre impar. Si
#introduce una altura par, deberá indicar por pantalla que vuelva a introducir la altura
#(rombos con altura par...no son rombos equilibrados).

def dibujar_rombo(altura):
    if altura % 2 == 0:
        print("Por favor, ingresa una altura impar.")
        return
    
    mitad = altura // 2  # La mitad del rombo

    # Parte superior del rombo
    for i in range(mitad + 1):
        espacios = mitad - i
        asteriscos = 2 * i + 1
        print(" " * espacios + "*" * asteriscos)

    # Parte inferior del rombo
    for i in range(mitad - 1, -1, -1):
        espacios = mitad - i
        asteriscos = 2 * i + 1
        print(" " * espacios + "*" * asteriscos)

# Solicitar al usuario la altura
while True:
    altura = int(input("Introduce la altura del rombo (impar): "))
    if altura % 2 != 0:
        break
    print("La altura debe ser impar. Inténtalo de nuevo.")

dibujar_rombo(altura)