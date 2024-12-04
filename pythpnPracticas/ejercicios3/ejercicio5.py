#5. Sin asustarte, escribe un programa que encuentre el máximo común divisor (MCD) de
#dos números ingresados por el usuario.

def calcular_mcd(a, b):
    while b !=0:
        a, b = b, a % b 
        return a
    
try: 
    numero1 = int(input("Ingrese el primer numero: "))
    numero2 = int(input("Ingrese el segundo numero: "))
    mcd = calcular_mcd(numero1, numero2)
    print(f"El maximo comun divisor (MCD) de {numero1} y {numero2} es: {mcd}")

except ValueError:
    print("Ingrese solo numeros enteros validos.")
