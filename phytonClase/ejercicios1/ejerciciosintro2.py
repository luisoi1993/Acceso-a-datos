"""#6.7. Calcular el promedio de tres números: Desarrolla un programa que calcule el
#promedio de tres números ingresados por el usuario.
#Ayuda: promedio = algo/3

numero1 = int(input("Digite el primer numero: "))
numero2 = int(input("Digite el segundo numero: "))
numero3 = int(input("Digite el tercer numero: "))
numeroFinal = (numero1+numero2+numero3)/3
print("El promedio de los tres numeros es :",numeroFinal)"""

"""#6.8. Área de un triángulo: Crea un programa que calcule el área de un triángulo a
#partir de la base y la altura ingresadas por el usuario.
#Ayuda: area = (base * altura) / 2

base = float(input("Digite la base: "))
altura = float(input("Digite la altura: "))
area = (base * altura) / 2
print("El area del triangulo es: ",area)"""

"""#6.9. Edad en el futuro: Escribe un programa que pida la edad actual del usuario y un
#número de años, y calcule la edad que tendrá el usuario en ese futuro número de
#años.

edad = int(input("Digita tu edad: "))
tiempo =int(input("Digita un numero de años: "))
edadFinal = edad + tiempo
print("Cuando pasen ",tiempo," años, tendras estos años: ",edadFinal)"""

"""#6.10. Área de un rectángulo: Crea un programa que calcule el área de un
#rectángulo a partir de su longitud y ancho ingresados por el usuario.

longitud = float(input("Digite la longitud del rectangulo: "))
ancho = float(input("Digite el acho del rectangulo: "))
area = longitud * ancho 
print("El area del rectangulo es: ",area)"""

#6.11. Días a segundos: Crea un programa que convierta un número de días
#ingresado por el usuario a segundos.
dias = int(input("Digite el numero de dias: "))
segundos = dias * 86400 
print("En esta cantidad de dias",dias," hay esta cantidad de segundos: ",segundos)

#6.12. Raíz cuadrada: Desarrolla un programa que calcule la raíz cuadrada de un
#número ingresado por el usuario.
#Ayuda: importamos la librería de matemáticas que nos resuelve el problema de
#realizar una raíz cuadrada. Ya tendremos tiempo de hacerlo sin la librería.
import math
numero = float(input("Ingresa un número para calcular su raíz cuadrada: "))
raiz_cuadrada = math.sqrt(numero)
print(f"La raíz cuadrada de {numero} es {raiz_cuadrada}.")


#6.13. Conversión de moneda: Escribe un programa que convierta una cantidad de
#dólares a euros. El tipo de cambio debe ser ingresado por el usuario.
dolares = float(input("Ingresa la cantidad en dólares: "))
tipo_cambio = float(input("Ingresa el tipo de cambio (dólares a euros): "))
euros = dolares * tipo_cambio
print(f"{dolares} dólares son {euros} euros con un tipo de cambio de {tipo_cambio}.")