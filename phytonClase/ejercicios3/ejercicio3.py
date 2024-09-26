#3. Realiza un programa que cuente el número de vocales que hay en una cadena de
#texto ingresada por el usuario.

contador = int(0)
frase = str(input("Digite una frase: "))
letras = [letra for letra in frase]

for i in range(len(letras)):
    if letras[i].lower() in "aeiou":
        contador += 1

print("El numero de letras es: ",contador)


