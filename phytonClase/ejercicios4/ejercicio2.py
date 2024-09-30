#2. Semi-triángulo de asteriscos: Crea un programa que dibuje un semi-triángulo de
#asteriscos. El usuario debe ingresar la altura por teclado.

asterisco = "*"  # este es el simbolo que vamos a usar
espacio = ""  # aqui guardamos los asteriscos que vamos a ir agregando

# le pedimos al usuario que diga cuántos asteriscos quiere
numero = int(input("Digite el número de asteriscos: "))

# empezamos un ciclo que va de 1 a la altura que puso el usuario
for i in range(1, numero + 1):
    espacio += asterisco  # vamos agregando asteriscos uno por uno
    print(espacio)  # mostramos los asteriscos
