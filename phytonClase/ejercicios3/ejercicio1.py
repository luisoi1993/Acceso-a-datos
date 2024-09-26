#1. Empezamos fuerte. Implementa un programa que muestre los números primos
#comprendidos entre 1 y 50.
#Ayuda:
#Vamos a instalar una librería que nos lo facilita. Seguramente tengas que instalarla:

#pip install sympy

#Esta librería te facilita si un número es primo o no lo es.

 
from sympy import isprime

for num in range(1, 51):
    if isprime(num):
        print(num)
