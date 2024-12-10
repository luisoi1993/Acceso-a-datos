"""2- Multiplicación de dos números mayores de cero
De forma recursiva, se puede definir matemáticamente la multiplicación descrita
como:

0 si b=0
axb=
a + (a x (b-1)) si b>0

Se puede mejorar teniendo en cuenta que a también pueda tomar el valor 0."""


def multiplicacion(a, b):
    # caso base
    if b == 0 or a == 0:
        return 0
    # caso recursivo
    else:
        return a + multiplicacion(a, b - 1)


a = 5
b = 3
print(f"El resultado de la multiplicación de {a} y {b} es: {multiplicacion(a, b)}")
