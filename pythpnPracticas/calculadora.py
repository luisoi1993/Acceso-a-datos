import math
from colorama import Fore, Style, init

# Inicializa colorama para colores en la terminal
init(autoreset=True)

def suma():
    num1 = float(input(Fore.YELLOW + "Digite el primer número para sumar: "))
    num2 = float(input(Fore.YELLOW + "Digite el segundo número para sumar: "))
    resultado = num1 + num2
    print(Fore.GREEN + f"El resultado de la suma es: {resultado}")

def resta():
    num1 = float(input(Fore.YELLOW + "Digite el primer número para restar: "))
    num2 = float(input(Fore.YELLOW + "Digite el segundo número para restar: "))
    resultado = num1 - num2
    print(Fore.GREEN + f"El resultado de la resta es: {resultado}")

def multiplicar():
    num1 = float(input(Fore.YELLOW + "Digite el primer número para multiplicar: "))
    num2 = float(input(Fore.YELLOW + "Digite el segundo número para multiplicar: "))
    resultado = num1 * num2
    print(Fore.GREEN + f"El resultado de la multiplicación es: {resultado}")

def dividir():
    num1 = float(input(Fore.YELLOW + "Digite el primer número para dividir: "))
    num2 = float(input(Fore.YELLOW + "Digite el segundo número para dividir: "))
    if num2 != 0:
        resultado = num1 / num2
        print(Fore.GREEN + f"El resultado de la división es: {resultado}")
    else:
        print(Fore.RED + "No se puede dividir entre cero.")


# Función para calcular el valor absoluto
def valor_absoluto():
    num = float(input(Fore.YELLOW + "Digite un número para calcular el valor absoluto: "))
    resultado = abs(num)
    print(Fore.GREEN + f"El valor absoluto de {num} es: {resultado}")

# Función para calcular la tangente
def tangente():
    num = float(input(Fore.YELLOW + "Digite un ángulo (en grados) para calcular la tangente: "))
    resultado = math.tan(math.radians(num))
    print(Fore.GREEN + f"La tangente de {num} grados es: {resultado}")

# Función para calcular el seno
def seno():
    num = float(input(Fore.YELLOW + "Digite un ángulo (en grados) para calcular el seno: "))
    resultado = math.sin(math.radians(num))
    print(Fore.GREEN + f"El seno de {num} grados es: {resultado}")

# Función para calcular el coseno
def coseno():
    num = float(input(Fore.YELLOW + "Digite un ángulo (en grados) para calcular el coseno: "))
    resultado = math.cos(math.radians(num))
    print(Fore.GREEN + f"El coseno de {num} grados es: {resultado}")

# Función para calcular el logaritmo base 10
def logaritmo_base_10():
    num = float(input(Fore.YELLOW + "Digite un número positivo para calcular el logaritmo base 10: "))
    if num > 0:
        resultado = math.log10(num)
        print(Fore.GREEN + f"El logaritmo base 10 de {num} es: {resultado}")
    else:
        print(Fore.RED + "El número debe ser positivo.")

# Función para calcular el logaritmo neperiano
def calcular_logaritmo_neperiano():
    num = float(input(Fore.YELLOW + "Digite un número positivo para calcular el logaritmo natural: "))
    if num > 0:
        resultado = math.log(num)
        print(Fore.GREEN + f"El logaritmo natural de {num} es: {resultado}")
    else:
        print(Fore.RED + "El número debe ser positivo.")

# Función para calcular la exponencial
def calcular_exponencial():
    num = float(input(Fore.YELLOW + "Digite un número para calcular el exponencial: "))
    resultado = math.exp(num)
    print(Fore.GREEN + f"El exponencial de {num} es: {resultado}")

# Función para calcular la raíz cuadrada
def calcular_raiz_cuadrada():
    num = float(input(Fore.YELLOW + "Digite un número no negativo para calcular la raíz cuadrada: "))
    if num >= 0:
        resultado = math.sqrt(num)
        print(Fore.GREEN + f"La raíz cuadrada de {num} es: {resultado}")
    else:
        print(Fore.RED + "El número debe ser no negativo.")

# Función para calcular la potencia
def potencia():
    base = float(input(Fore.YELLOW + "Digite la base: "))
    exponente = float(input(Fore.YELLOW + "Digite el exponente: "))
    resultado = math.pow(base, exponente)
    print(Fore.GREEN + f"{base} elevado a la potencia de {exponente} es: {resultado}")

# Función para calcular la raíz cúbica
def raiz_cubica():
    num = float(input(Fore.YELLOW + "Digite un número para calcular la raíz cúbica: "))
    resultado = num ** (1 / 3)
    print(Fore.GREEN + f"La raíz cúbica de {num} es: {resultado}")

# Función para calcular la hipotenusa
def hipotenusa():
    cateto1 = float(input(Fore.YELLOW + "Digite el primer cateto: "))
    cateto2 = float(input(Fore.YELLOW + "Digite el segundo cateto: "))
    resultado = math.hypot(cateto1, cateto2)
    print(Fore.GREEN + f"La hipotenusa del triángulo es: {resultado}")

# Función para convertir grados a radianes
def grados_a_radianes():
    grados = float(input(Fore.YELLOW + "Digite un ángulo en grados: "))
    resultado = math.radians(grados)
    print(Fore.GREEN + f"{grados} grados equivalen a {resultado} radianes")

# Función para convertir radianes a grados
def radianes_a_grados():
    radianes = float(input(Fore.YELLOW + "Digite un ángulo en radianes: "))
    resultado = math.degrees(radianes)
    print(Fore.GREEN + f"{radianes} radianes equivalen a {resultado} grados")


def mostrar_menu():
    print(Fore.CYAN + Style.BRIGHT + "\n" + "="*40)
    print(Fore.BLUE + Style.BRIGHT + "           🧮 CALCULADORA 🧮")
    print(Fore.CYAN + Style.BRIGHT + "="*40)
    opciones = [
        "Sumar", "Restar", "Multiplicar", "Dividir",
        "Valor absoluto", "Tangente", "Seno", "Coseno",
        "Logaritmo en base 10", "Logaritmo Neperiano",
        "Exponencial", "Raíz cuadrada", "Potencia",
        "Raíz cúbica", "Hipotenusa", "Grados a radianes",
        "Radianes a grados", "Salir"
    ]
    for i, opcion in enumerate(opciones, start=1):
        print(Fore.MAGENTA + f"{i:2}. {Fore.YELLOW}{opcion}")
    print(Fore.CYAN + "="*40)

def ejecutar_menu():
    while True:
        mostrar_menu()
        try:
            opcion = int(input(Fore.GREEN + "Selecciona una opción: "))
            if opcion == 1:
                suma()
            elif opcion == 2:
                resta()
            elif opcion == 3:
                multiplicar()
            elif opcion == 4:
                dividir()
            elif opcion == 5:
                valor_absoluto()
            elif opcion == 6:
                tangente()
            elif opcion == 7:
                seno()
            elif opcion == 8:
                coseno()
            elif opcion == 9:
                logaritmo_base_10()
            elif opcion == 10:
                calcular_logaritmo_neperiano()
            elif opcion == 11:
                calcular_exponencial()
            elif opcion == 12:
                calcular_raiz_cuadrada()
            elif opcion == 13:
                potencia()
            elif opcion == 14:
                raiz_cubica()
            elif opcion == 15:
                hipotenusa()
            elif opcion == 16:
                grados_a_radianes()
            elif opcion == 17:
                radianes_a_grados()
            elif opcion == 18:
                print(Fore.BLUE + Style.BRIGHT + "¡Gracias por usar la calculadora! Hasta luego. 👋")
                break
            else:
                print(Fore.RED + "Opción no válida, elija otro número.")
        except ValueError:
            print(Fore.RED + "Entrada no válida. Por favor ingrese un número.")

# Ejecutar el menú
ejecutar_menu()
