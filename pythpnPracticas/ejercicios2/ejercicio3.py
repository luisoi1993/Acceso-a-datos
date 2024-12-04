#3. Escribe un algoritmo que sume los números pares del 1 al 100.
resultado = 0

for numero in (1,101):
    if(numero % 2 ==0):
        resultado = resultado + numero

print(f"El resultado es {resultado}")