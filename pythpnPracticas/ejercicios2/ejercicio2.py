#2. Crea un algoritmo que calcule el factorial de un número introducido por el
#usuario.
#Ayuda:
#Factorial (n!) de un número es el resultado de multiplicar ese número por todos
#los números inferiores hasta llegar al 1.
#n!(3)=3*2*1=6
#n!(5)=5*4*3*2*1=120



numero = int(input("Digite el numero del que quieres calcular el factorial: "))
factorial = 1  # Variable para almacenar el resultado del factorial

for i in range(numero, 0, -1):  # Empieza en 'numero' y termina en 1 (inclusive)
    factorial *= i

print(f"El resultado del factorial de {numero} es: {factorial}")

