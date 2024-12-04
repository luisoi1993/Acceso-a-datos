#6.6. Determinar el tipo de dato: Escribe un programa que determine el tipo de dato de
#una variable ingresada por el usuario.

entrada = input("Ingresa un valor: ")

try:
    valor = int(entrada)
    tipo_dato = "entero (int)"
except ValueError:
    try:
        valor = float(entrada)
        tipo_dato = "decimal (float)"
    except ValueError:
        valor = entrada
        tipo_dato = "cadera (str)"

print(f"El tipo de dato de la entrada es: {tipo_dato}")

