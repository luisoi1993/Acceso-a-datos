#4. Escribe un programa que calcule el área de un triángulo dados su base y altura
#con precisión de 2 decimales.
#Ayuda:
#Puedes limitar el número de decimales de varias formas:
#\ round
#round(variable,no de decimales)
#print(round(numero, 2)
#\ Format
#print("{:.2f}".format(numero))
#\ f-string
#print(f"{numero:.2f}")

base = float(input("Ingresa la base del triangulo: "))
altura = float(input("Ingresa la altura del triangulo: "))
resultado = (base * altura)/2
print("El area del triangulo es: ",round(resultado, 2))
