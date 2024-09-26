#5. Realiza un programa que muestre los números del 1 al 100, pero que reemplace
#los múltiplos de 3 por "Triplete" y los múltiplos de 5 por "Cinquillo".

for numero in range(1, 101):
    if numero % 3 == 0 and numero % 5 == 0:
        print("Triplete y Cinquillo")
    elif numero % 3 == 0:
        print("Triplete")
    elif numero % 5 == 0:
        print("Cinquillo")
    else:
        print(numero)
