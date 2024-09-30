#1. Tabla de multiplicar:
#Escribe un programa en python que imprima todas las tablas de multiplicar del 1 al 10.
#Será importante que se presenten de forma clara y ordenada.


for i in range(1, 11):
    # Imprime el encabezado de la tabla
    print(f"Tabla del {i}:")
    
    # Un bucle interno que va del 1 al 10, que representa los multiplicadores
    for j in range(1, 11):
        # Calcula el resultado de la multiplicación
        numero = i * j
        
        # Imprime el resultado de la multiplicación en formato: "i x j = resultado"
        print(f"{i} x {j} = {numero}")
    
    # Imprime una línea en blanco para separar las tablas
    print()
