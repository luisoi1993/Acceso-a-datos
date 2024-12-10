"""11. Crea de programa que genere contraseñas.
Para ello, deberás tener 3 tuplas de las que se cogerán los elementos que formarán las
contraseñas.
\ Tupla con dígitos: tupla que contiene los dígitos del 0 al 9
\ Tupla con letras: tupla que contiene las letras del abecedario (sin la letra ñ)
\ Tupla con caracteres especiales: tupla que contiene al menos 15 caracteres
especiales, los que consideresb(¡”$%&/()=......)
Especificaciones:
\ La contraseñas generadas deberán ser también tuplas.
\ Se generarán dos contraseñas, una fuerte y una débil.
\ El usuario decide por teclado la longitud de la contraseña, mínimo 8
caracteres y máximo 64.
\ La contraseña fuerte deberá tener una compensación aproximada según la
siguiente distribución:
- Un 20% de dígitos, un 40% de letras y un 40% de caracteres especiales.
\ La contraseña débil deberá tener una compensación aproximada según la
siguiente distribución:
- Un 80 % dígitos, un 15% letras y un 5% caracteres especiales."""

import random


digitos = tuple("0123456789")
letras = tuple("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
caracteres_especiales = tuple("!\"#$%&/()=?¡@#^*+,-.:;<>[]{}")

def generar_contraseña(longitud, distribucion):
    """
    Genera una contraseña basada en la longitud y distribución proporcionada.

    Args:
        longitud (int): Longitud de la contraseña.
        distribucion (dict): Diccionario con la proporción de cada tipo de carácter.

    Returns:
        tuple: Contraseña generada como una tupla.
    """
    cantidad_digitos = int(longitud * distribucion["digitos"])
    cantidad_letras = int(longitud * distribucion["letras"])
    cantidad_especiales = longitud - cantidad_digitos - cantidad_letras  # Lo que falta para completar la longitud

    # Seleccionamos caracteres aleatorios de cada tipo
    seleccion_digitos = random.choices(digitos, k=cantidad_digitos)
    seleccion_letras = random.choices(letras, k=cantidad_letras)
    seleccion_especiales = random.choices(caracteres_especiales, k=cantidad_especiales)

    # Combinamos los caracteres y los mezclamos
    contraseña = seleccion_digitos + seleccion_letras + seleccion_especiales
    random.shuffle(contraseña)

    return tuple(contraseña)


longitud = int(input("Introduce la longitud de la contraseña (entre 8 y 64): "))
while longitud < 8 or longitud > 64:
    longitud = int(input("Por favor, introduce un valor válido (entre 8 y 64): "))

# Generamos la contraseña fuerte
contraseña_fuerte = generar_contraseña(
    longitud,
    {"digitos": 0.2, "letras": 0.4, "especiales": 0.4}
)

# Generamos la contraseña débil
contraseña_debil = generar_contraseña(
    longitud,
    {"digitos": 0.8, "letras": 0.15, "especiales": 0.05}
)

# Mostramos las contraseñas generadas
print("\nContraseña fuerte generada:", contraseña_fuerte)
print("Contraseña débil generada:", contraseña_debil)
