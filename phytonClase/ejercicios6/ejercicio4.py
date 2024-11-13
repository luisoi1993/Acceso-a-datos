#4- Igual que 3 pero que el valor a buscar sea leído por teclado.
#Recuerda cuando usas input en Python, obtienes una cadena, sin importar si el usuario
#ingresa un número o cualquier otro tipo de entrada. Por lo que es necesario distinguir si
#lo que se ha introducido es, por ejemplo, un dígito (isdigit())

mi_tupla = (1, 2, 3, "cuatro", "cinco")

# Leer el valor desde el teclado
valor = input("Introduce el valor a buscar en la tupla: ")

# Verificar si el valor es un dígito
if valor.isdigit():
    # Convertir a entero si es un dígito
    valor = int(valor)
    
# Comprobar si el valor está en la tupla
if valor in mi_tupla:
    print(f"El valor '{valor}' está en la tupla.")
else:
    print(f"El valor '{valor}' no está en la tupla.")