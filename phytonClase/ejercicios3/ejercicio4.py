#4. Crea un programa que determine si una palabra es un palíndromo.

palabra = str(input("Digite una palabra: "))
letras = [letra for letra in palabra]
letrasReves = [len(letras)]
contador = int(0)
for i in range(len(letras) -1, -1, -1):
    letrasReves[contador]=letras[i]
    contador +=1

palabraReves = ''.join(letras)

if palabra.lower() == palabraReves.lower():
    print("La palabra es palindroma: ")
else:
    print("La palabra no es palindroma: ")
