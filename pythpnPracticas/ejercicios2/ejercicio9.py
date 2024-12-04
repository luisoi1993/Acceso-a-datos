#Realiza un programa que sume los números impares del 1 al 100.

print("Bienvenido a la suma de los numeros impares del 1 al 100")
suma = 0

for i in range (1,101):
    if(i % 2 != 0):
        suma = suma +  i

print(f"La suma total  de los numeros impares del 1 al 100 es  {suma}")
