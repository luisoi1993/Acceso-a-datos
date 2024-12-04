#10. Crea un programa que cuente cuántas veces aparece una letra específica en
#una cadena de texto ingresada por el usuario.

cadena = input("Introduce una cadena de texto: ")

letra = input("Introduce la letra que quieres contar: ")

contador = cadena.count(letra)

print(f"La letra '{letra}' aparece {contador} veces en la cadena.")

