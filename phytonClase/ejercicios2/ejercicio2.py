#2. Crea un algoritmo que calcule el factorial de un número introducido por el
#usuario.
#Ayuda:
#Factorial (n!) de un número es el resultado de multiplicar ese número por todos
#los números inferiores hasta llegar al 1.
#n!(3)=3*2*1=6
#n!(5)=5*4*3*2*1=120

factorial = int(input("Ingresa el número: "))

for numero in range(factorial - 1, 0, -1):
    factorial *= numero

print(factorial)