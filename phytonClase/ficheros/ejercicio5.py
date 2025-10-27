"""Ejercicio 5: Combinación de archivos
Desarrolla un algoritmo que genere dos archivos de texto, por ejemplo, archivo1.txt y
archivo2.txt, con contenido diferente (una frase diferente cada uno)
Escribe un programa que abra ambos archivos y combine su contenido en un nuevo
archivo llamado combinado.txt y además lo muestre por pantalla.
Puedes abrir varios ficheros a la vez:
contenido1 = f1.read()
contenido2 = f2.read()

Y luego combinarlos:

f_combinado.write(contenido1 + '\n' + contenido2)"""

# primero creamos dos archivos de texto con contenido diferente
with open("archivo1.txt", "w") as archivo1:
    archivo1.write("este es el contenido del archivo 1.")

with open("archivo2.txt", "w") as archivo2:
    archivo2.write("este es el contenido del archivo 2.")

# ahora abrimos los dos archivos para leer su contenido
with open("archivo1.txt", "r") as f1, open("archivo2.txt", "r") as f2:
    # leemos el contenido de ambos archivos
    contenido1 = f1.read()
    contenido2 = f2.read()

# combinamos el contenido de ambos archivos en uno nuevo llamado combinado.txt
with open("combinado.txt", "w") as f_combinado:
    # escribimos el contenido de los dos archivos en el archivo combinado
    f_combinado.write(contenido1 + '\n' + contenido2)

# mostramos el contenido del archivo combinado por pantalla
with open("combinado.txt", "r") as f_combinado:
    print("contenido combinado:")
    print(f_combinado.read())
