#8. Implementa un programa que genere la tabla de multiplicar de un número
#ingresado por el usuario.

numero = int(input("Digite el numero: "))


for num in range (1,11):
    resultado = numero * num
    print(numero," * ",num," = ",resultado)
