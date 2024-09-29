#2. Semi-triángulo de asteriscos: Crea un programa que dibuje un semi-triángulo de
#asteriscos. El usuario debe ingresar la altura por teclado.

asterisco = "*"
espacio = ""

numero = int(input("Digite el número de asteriscos: "))

for i in range(1, numero + 1):
    espacio += asterisco
    print(espacio)