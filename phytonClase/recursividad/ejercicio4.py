"""4- Exponente de dos números (n elevado a m)
El exponente de dos números n elevado a m se puede expresar recursivamente como:

1 si m=0
nm=
n x (nm-1) si m >0

Recuerda que todo número elevado a 0 = 1; 0 elevado a cualquier número >0 es
igual a 0; pero no se puede elevar a ningún número el cero, por lo que 0 elevado a 0
es una indeterminación!!!
"""

def exponente(n, m):
    # caso base: cualquier número elevado a 0 es 1
    if m == 0:
        return 1
    # caso recursivo: n * (n^(m-1))
    elif m > 0:
        return n * exponente(n, m - 1)
    # casos especiales
    elif n == 0 and m == 0:
        raise ValueError("0 elevado a 0 es indeterminado")
    elif n == 0 and m > 0:
        return 0


n = 2
m = 3
print(f"{n} elevado a {m} es: {exponente(n, m)}")
