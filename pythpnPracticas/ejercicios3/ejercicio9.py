# Función para verificar si un número es primo
def Es_Primo(Numero):
    if Numero < 2:
        return False  # Los números menores de 2 no son primos
    for i in range(2, int(Numero**0.5) + 1):  # Comprobar divisores hasta la raíz cuadrada
        if Numero % i == 0:
            return False  # Si es divisible, no es primo
    return True  # Si no se encuentra divisor, es primo

# Función principal para mostrar los números primos del 1 al 50
def mostrar_primos():
    print("Números primos entre 1 y 50:")
    for num in range(1, 51):
        if Es_Primo(num):
            print(num, end=" ")  # Imprimir en una sola línea separados por espacios
    print()  # Salto de línea final

# Llamar a la función principal
mostrar_primos()
