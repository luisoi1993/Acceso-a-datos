#6.4. Calculadora de IMC (Índice de Masa Corporal): Desarrolla un programa que
#calcule el IMC a partir del peso y la altura ingresados por el usuario.
#Ayuda: imc = peso / (altura^2)

peso = int(input("Digite el peso en kg "))
altura = int(input("Digite el valor en cm "))
imc = peso / (altura * altura)

print("El indice de masa corporal es : " , imc)