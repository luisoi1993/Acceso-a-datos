"""3- MCD de dos números (mayores de cero)(MCD=Máximo Común Divisor)
El máximo común divisor (MCD) de dos números se resuelve de forma recursiva
utilizando el algoritmo de Euclides:
a si b=0

MCD (a,b)=

MCD(b, a mod b) si b>0

En Python, el módulo se realiza mediante la operación %, el cual da el módulo o
residuo de un número.
Recuerda que MCD(0,0) = indeterminación.
Si a=0, entonces el MCD es b."""

def mcd(a, b):
    # caso base: si b es 0, el MCD es a
    if b == 0:
        return a
    # si a es 0, el MCD es b
    elif a == 0:
        return b
    # caso recursivo: aplicar el algoritmo de Euclides
    else:
        return mcd(b, a % b)


a = 48
b = 18
print(f"El MCD de {a} y {b} es: {mcd(a, b)}")
