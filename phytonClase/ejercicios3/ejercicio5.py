#Sin asustarte, escribe un programa que encuentre el máximo común divisor (MCD) de
#dos números ingresados por el usuario.

def calcular_mcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

num1 = int(input("Ingresa el primer número: "))
num2 = int(input("Ingresa el segundo número: "))

mcd = calcular_mcd(num1, num2)

print(f"El MCD de {num1} y {num2} es: {mcd}")
