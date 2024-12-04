#1. Tabla de multiplicar:
#Escribe un programa en python que imprima todas las tablas de multiplicar del 1 al 10.
#Será importante que se presenten de forma clara y ordenada.

for i in range (1 ,11):
    for j in range (1 ,11):
        print(f" {i}  * {j} = {i*j}")