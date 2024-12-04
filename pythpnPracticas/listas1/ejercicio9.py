"""7. Dibujo de un rombo: Diseña un programa que dibuje un rombo equilibrado de
asteriscos. El usuario debe ingresar la altura del rombo, siendo esta siempre impar. Si
introduce una altura par, deberá indicar por pantalla que vuelva a introducir la altura
(rombos con altura par...no son rombos equilibrados).
"""

# Solicitar la altura del rombo
while True:
    altura = int(input("Introduce la altura del rombo (debe ser un número impar): "))
    if altura % 2 != 0:
        break
    print("La altura debe ser impar. Inténtalo de nuevo.")

# Dibujar la parte superior del rombo (incluye la línea central)
for i in range((altura // 2) + 1):
    espacios = " " * ((altura // 2) - i)  # Espacios antes de los asteriscos
    asteriscos = "*" * (2 * i + 1)       # Cantidad de asteriscos
    print(espacios + asteriscos)

# Dibujar la parte inferior del rombo
for i in range((altura // 2) - 1, -1, -1):
    espacios = " " * ((altura // 2) - i)  # Espacios antes de los asteriscos
    asteriscos = "*" * (2 * i + 1)       # Cantidad de asteriscos
    print(espacios + asteriscos)
