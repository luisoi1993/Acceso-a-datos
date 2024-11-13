#3- Indicar si los elementos “cuatro”, “2” y 2 están en la tupla anterior

mi_tupla = (1, 2, 3, "cuatro", "cinco")

elementos_a_buscar = ["cuatro", "2", 2]

for elemento in elementos_a_buscar:
    if elemento in mi_tupla:
        print(f"El elemento '{elemento}' está en la tupla.")
    else:
        print(f"El elemento '{elemento}' no está en la tupla.")
