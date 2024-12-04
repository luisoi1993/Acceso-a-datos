from sympy import isprime

primos = [num for num in range(1,51) if isprime(num)]

print("Los numeros primos entre 1 y 50 son: ")
print(primos)

