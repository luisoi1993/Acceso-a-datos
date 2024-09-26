"""#Suma de números: Escribe un programa que sume dos números enteros
#ingresados por el usuario mediante teclado y muestre el resultado por pantalla.

num1 = int(input("Ingresa el primer numero: "))
num2 = int(input("ingresa el segundo numero: "))
suma = num1 + num2
print("La suma es : ", suma)

#6.2. Calculadora de área de un cuadrado: Crea un programa que calcule el área de
#un cuadrado cuando el usuario ingresa la longitud de un lado.

longitud = float(input("Ingresa la longitud de uno de los lados :"))
final = longitud * longitud
print("El area del cuadrado es: ",final)


#6.3. Conversión de temperatura: Escribe un programa que convierta grados Celsius a
#grados Fahrenheit. Pide al usuario ingresar la temperatura en Celsius.
#Ayuda: fahrenheit = (celsius 9/5) + 32

grados = float(input("Ingresa los grados:"))
celsius = (grados - 32) * 5 / 9;
print("El resultado en grados celsius: ",celsius)"""

"""#6.4. Calculadora de IMC (Índice de Masa Corporal): Desarrolla un programa que
#calcule el IMC a partir del peso y la altura ingresados por el usuario.
#Ayuda: imc = peso / (altura^2)

peso =float(input("Ingresa el peso: "))
altura = float(input("Ingresa la altura: "))
final = peso/ (altura * altura)
print("El indice de masa corporal es: ",final)"""


"""#6.5. Concatenación de cadenas: Crea un programa que tome dos cadenas como
#entrada del usuario y las concatene en una sola cadena.

cadena1 = input("Ingresa la primera cadena: ")
cadena2 = input("Ingresa la segunda cadena: ")
cadena3 = cadena1 + cadena2
print(cadena3)"""

"""#6.6. Determinar el tipo de dato: Escribe un programa que determine el tipo de dato de
#una variable ingresada por el usuario.

# Solicita al usuario que ingrese un valor
entrada = input("Ingresa un valor: ")

# Intentamos convertir la entrada a diferentes tipos y determinar cuál es el correcto
try:
    # Convertimos a entero
    valor = int(entrada)
    tipo_dato = "entero (int)"
except ValueError:
    try:
        # Convertimos a flotante
        valor = float(entrada)
        tipo_dato = "decimal (float)"
    except ValueError:
        # Si no es ni entero ni decimal, asumimos que es una cadena
        valor = entrada
        tipo_dato = "cadena (str)"

# Imprimimos el tipo de dato
print(f"El tipo de dato de la entrada es: {tipo_dato}")"""


#6.7. Calcular el promedio de tres números: Desarrolla un programa que calcule el
#promedio de tres números ingresados por el usuario.
#Ayuda: promedio = algo/3

