#6.3. Conversión de temperatura: Escribe un programa que convierta grados Celsius a
#grados Fahrenheit. Pide al usuario ingresar la temperatura en Celsius.
#Ayuda: fahrenheit = (celsius 9/5) + 32

celsius = float(input("Digite el valor de los grados celsius "))
fahrenheit = (celsius * 9 / 5) + 32

print("El resultado en fahrenheit: " , fahrenheit) 