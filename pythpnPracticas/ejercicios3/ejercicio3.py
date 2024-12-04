"""3. Realiza un programa que cuente el número de vocales que hay en una cadena de
texto ingresada por el usuario."""

texto = input("Introduce una cadena de texto: ")

vocales = "aeiouAEIOU"

contador_vocales = sum(1 for letra in texto if letra in vocales)

print(f"El numero de vocales em la cadena es: {contador_vocales}")
