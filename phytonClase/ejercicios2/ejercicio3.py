#3. Escribe un algoritmo que sume los números pares del 1 al 100.

suma = 0
for numero in range(1, 101):  
    if numero % 2 == 0:
        suma = suma + numero

print("La suma de los numeros pares del 1 al 100 es: ",suma)