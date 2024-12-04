palabra = input("Introduce una frase: ")

palabra_normalizada = palabra.lower()

es_palindromo = palabra_normalizada == palabra_normalizada[::-1]

if es_palindromo:
    print(f"La palabra '{palabra}' es un palindromo. " )
else:
    print(f"La palabra {palabra} no es un palindromo")


