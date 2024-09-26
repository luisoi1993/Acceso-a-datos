#2. Realiza un programa que calcule la suma de los dígitos de un número entero
#ingresado por el usuario. Es decir, el usuario introduce por ejemplo el 123 por teclado, y
#la salida deberá ser 1+2+3=6

numero = int(input("Digite el numero: "))
suma = int(0)
if numero < 10:
    print("La suma del numero es: ",numero)
else:
    cifras = [int(digito) for digito in str (numero)]
    for i in range(len(cifras)):
        suma = suma + cifras[i] 

    print("El resultado de la suma de los numeros es: ",suma)






    
