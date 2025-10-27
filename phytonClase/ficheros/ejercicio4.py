"""Ejercicio 4: Modificación de un archivo
Escribe un programa que abra el archivo nuevo.txt
Dicho fichero tendrá escrito:

Contenido del archivo 1.
Contenido Modificado del archivo 2. Más contenido

Utiliza las funciones .replace para cambiar la palabra “Contenido” por “Modificado”
contenido_modificado = contenido.replace("Contenido", "Modificado")

La salida por pantalla deberá ser:

Contenido antes de la modificación:
Contenido del archivo 1.
Contenido modificado del archivo 2. Más contenido
Contenido después de la modificación:
Modificado del archivo 1.
Modificado modificado del archivo 2. Más contenido

Y la del fichero:

Modificado del archivo 1.
Modificado Modificado del archivo 2. Más contenido"""

# abrimos el archivo en modo lectura
with open("nuevo.txt", "r") as archivo:
    # leemos el contenido del archivo y lo guardamos en una variable
    contenido = archivo.read()

# mostramos el contenido antes de la modificación
print("contenido antes de la modificación:")
print(contenido)

# cambiamos la palabra "Contenido" por "Modificado" en el contenido
contenido_modificado = contenido.replace("Contenido", "Modificado")

# mostramos el contenido después de la modificación
print("contenido después de la modificación:")
print(contenido_modificado)

# abrimos el archivo en modo escritura para sobrescribir el contenido
with open("nuevo.txt", "w") as archivo:
    # escribimos el contenido modificado en el archivo
    archivo.write(contenido_modificado)
