#6.12. Raíz cuadrada: Desarrolla un programa que calcule la raíz cuadrada de un
#número ingresado por el usuario.
#Ayuda: importamos la librería de matemáticas que nos resuelve el problema de
#realizar una raíz cuadrada. Ya tendremos tiempo de hacerlo sin la librería.

import math

numero = float(input("Digite el numero al que le quieres hacer la raiz cuadrada: "))
resultado = math.sqrt(numero)

print(f"El resultado es: {resultado}")