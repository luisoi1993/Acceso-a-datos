"""5- resta de dos números
La resta de dos números a y b (mayores de 0 y a>b) se puede expresar
recursivamente como:
a si b=0

resta(a,b)=

resta(a-1,b-1)"""

def resta(a, b):
    # caso base: si b es 0, la resta es a
    if b == 0:
        return a
    # caso recursivo: resta(a-1, b-1)
    else:
        return resta(a - 1, b - 1)


a = 5
b = 3
print(f"La resta de {a} y {b} es: {resta(a, b)}")
