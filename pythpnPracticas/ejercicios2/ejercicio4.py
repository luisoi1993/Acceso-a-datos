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

# Entrada de datos
base = float(input("Digite el valor de la base: "))
altura = float(input("Digite el valor de la altura: "))

# Cálculo del área del triángulo
area = (base * altura) / 2

# Mostrando el resultado con precisión de 2 decimales:

# Forma 1: Usando round()
# print(round(area, 2))

# Forma 2: Usando format()
# print("{:.2f}".format(area))

# Forma 3: Usando f-string (esta está activada)
print(f"El área del triángulo es: {area:.2f}")
