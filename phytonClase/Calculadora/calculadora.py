import math
from colorama import Fore, Back, Style, init


init(autoreset=True)

def calculadora():
    contraseniaFinal = "1234"
    contrasenia = ""
    while True:
        print(Fore.GREEN +"1. Digite la contraseña:\n2. Cambiar la contraseña:\n3. Salir del programa")
        menuContrasenia = int(input("Elija una opción: "))
        
        if menuContrasenia == 1:
            contrasenia = input(Fore.YELLOW + "Escriba la contraseña: ")
            if contrasenia == contraseniaFinal:
                print(Back.RED + "Contraseña correcta.")
                break
            else:
                print("Contraseña incorrecta.")
                
        elif menuContrasenia == 2:
            contraseniaFinal = input(Fore.MAGENT + "Digite la nueva contraseña: ")
            print("Contraseña cambiada con éxito.")
            
        elif menuContrasenia == 3:
            print(Style.DIM + "Salir del programa.")
            return  

        else:
            print("Opción no válida. Intente de nuevo.")

    while True:
        print(Back.CYAN + """Bienvenido a la calculadora
            1. Sumar
            2. Restar
            3. Multiplicar
            4. Dividir
            5. Valor absoluto
            6.Tangente
            7.Seno
            8.Coseno
            9.Tangente
            10.Logaritmo en base 10
            11.Logaritmo neperiano
            12.a elevado a x
            13.Raíz cuadrada
            14. Hipotenusa de un triángulo rectángulo 
            15. Factorial
            16. Área de un círculo
            17. Conversión de grados a radianes
            18. Conversión de radianes a grados
            19.Salir """)
        
        menu = int(input(Back.WHITE + "Elija una opción: "))
        
        if menu == 1:
            num1 = int(input("Digite el primer número: "))
            num2 = int(input("Digite el segundo número: "))
            suma = num1 + num2
            print("El resultado es ", suma)
        
        elif menu == 2:
            num1 = int(input("Digite el primer número: "))
            num2 = int(input("Digite el segundo número: "))
            resta = num1 - num2
            print("El resultado es ", resta)

        elif menu == 3:
            num1 = int(input("Digite el primer número: "))
            num2 = int(input("Digite el segundo número: "))
            multiplicacion = num1 * num2
            print("El resultado es ", multiplicacion)

        elif menu == 4:
            num1 = int(input("Digite el primer número: "))
            num2 = int(input("Digite el segundo número: "))
            if num2 != 0:  # Verifica que no se divida por cero
                division = num1 / num2
                print("El resultado es ", division)
            else:
                print("No se puede dividir por cero.")

        elif menu == 5:
            num1 = int(input("Digite el numero: "))
            if num1 == 0:
                print("El numero no puedo ser cero: ")
            else: 
                num1 = abs(num1)
                print("El resultado es: ",num1)

        elif menu == 6:
            num1 = int(input("Digite los grados : "))
            num1 = math.radians(num1)
            num1 = math.tan(num1)
            print("EL resultado es: ",num1)

        elif menu == 7:
            num1 = int(input("Digite los grados : "))
            num1 = math.radians(num1)
            num1 = math.sin(num1)
            print("EL resultado es: ",num1)

        elif menu == 8:
            num1 = int(input("Digite los grados : "))
            num1 = math.radians(num1)
            num1 = math.cos(num1)
            print("EL resultado es: ",num1)

        elif menu ==  9:
            num1 = int(input("Digite los grados : "))
            num1 = math.radians(num1)
            num1 = math.tan(num1)
            print("EL resultado es: ",num1)

        elif menu == 10:
            num1 = int(input("Digite el numero: "))
            if num1 == 0:
                print("El numero no puedo ser cero: ")
            else: 
                num1 = math.log10(num1)
                print("El resultado es: ",num1)

        elif menu == 11:
            num1 = int(input("Digite el numero: "))
            if num1 == 0:
                print("El numero no puedo ser cero: ")
            else: 
                num1 = math.log(num1)
                print("El resultado es: ",num1) 

        elif menu == 12:
            num1 = float(input("Digite la base: "))
            num2 = float(input("Digite el exponente: "))
            resultado = math.pow(num1, num2)
            print("El resultado es : ",resultado)

        elif menu == 13:
            num1 = int(input("Digite el numero : "))
            resultado = math.sqrt(num1)
            print("El resultado es : ",resultado)

        elif menu == 14:
            cateto1 = float(input("Digite el primer cateto: "))
            cateto2 = float(input("Digite el segundo cateto: "))
            hipotenusa = math.hypot(cateto1, cateto2)
            print(f"La hipotenusa es: {hipotenusa:.2f}")

        elif menu == 15:
            num1 = int(input("Digite un número: "))
            print("El factorial es: ", math.factorial(num1))

        elif menu == 16:
            radio = float(input("Digite el radio del círculo: "))
            area = math.pi * radio ** 2
            print(f"El área del círculo es: {area:.2f}")
        
        elif menu == 17:
            grados = float(input("Digite los grados: "))
            radianes = math.radians(grados)
            print(f"{grados} grados son {radianes:.2f} radianes")

        elif menu == 18:
            radianes = float(input("Digite los radianes: "))
            grados = math.degrees(radianes)
            print(f"{radianes} radianes son {grados:.2f} grados")

        elif menu == 19:
            print(Back.CYAN +"Saliendo de la calculadora.")
            break
        
        else:
            print("Opción no válida. Intente de nuevo.")

calculadora()
