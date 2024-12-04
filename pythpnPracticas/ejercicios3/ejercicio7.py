# Función para la puerta lógica AND
def puerta_and(a, b):
    return a and b

# Función para la puerta lógica OR
def puerta_or(a, b):
    return a or b

# Función para la puerta lógica NOT
def puerta_not(a):
    return not a

# Menú para seleccionar la operación lógica
print("Seleccione la puerta lógica que desea usar:")
print("1. AND")
print("2. OR")
print("3. NOT")

opcion = int(input("Ingrese el número de la opción: "))

# Operaciones según la opción seleccionada
if opcion == 1:
    # Operación AND
    a = int(input("Introduce el primer valor (0 o 1): "))
    b = int(input("Introduce el segundo valor (0 o 1): "))
    if a in [0, 1] and b in [0, 1]:
        print(f"Resultado de AND({a}, {b}): {puerta_and(a, b)}")
    else:
        print("Error: los valores deben ser 0 o 1.")

elif opcion == 2:
    # Operación OR
    a = int(input("Introduce el primer valor (0 o 1): "))
    b = int(input("Introduce el segundo valor (0 o 1): "))
    if a in [0, 1] and b in [0, 1]:
        print(f"Resultado de OR({a}, {b}): {puerta_or(a, b)}")
    else:
        print("Error: los valores deben ser 0 o 1.")

elif opcion == 3:
    # Operación NOT
    a = int(input("Introduce un valor (0 o 1): "))
    if a in [0, 1]:
        print(f"Resultado de NOT({a}): {puerta_not(a)}")
    else:
        print("Error: el valor debe ser 0 o 1.")

else:
    print("Opción no válida.")
