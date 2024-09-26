#9. Realiza un programa que sume los números impares del 1 al 100.

suma = 0;
for numero in range(1,101):
    if numero % 2 !=0:
        suma = suma + numero

print("El resultado de la suma de los cien primeros numeros impares es: ",suma)
