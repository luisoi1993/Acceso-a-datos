"""Ejercicio 6: Lectura y escritura simultánea
Crea un programa que genere un archivo con el siguiente contenido:
“Este archivo existe.
Contiene algunas líneas de texto. en modo lectura y escritura simultánea."
A continuación lo tiene que modificar añadiendo:
“Añadiendo más líneas al contenido existente!
Esto es una adición al archivo”
Se tiene que quedar en el fichero grabado todos los mensajes y por pantalla
visualizar, además de los mensajes que se han grabado en el fichero, lo que ha ido
haciendo.
Ejemplo de lo que se muestra por pantalla:
Contenido antes de la modificación:
Este archivo existe.
Contiene algunas líneas de texto.
Contenido después de la modificación:
Este archivo existe.
Contiene algunas líneas de texto.
¡Añadiendo más líneas al contenido existente!
Esto es una adición al archivo.

Contenido del fichero:

Este archivo existe.
Contiene algunas líneas de texto.
¡Añadiendo más líneas al contenido existente!
Esto es una adición al archivo."""

# primero creamos el archivo con el contenido inicial
with open("archivo.txt", "w") as archivo:
    archivo.write("Este archivo existe.\nContiene algunas líneas de texto.\n")

# mostramos el contenido antes de la modificación
with open("archivo.txt", "r") as archivo:
    contenido = archivo.read()
    print("contenido antes de la modificación:")
    print(contenido)

# ahora, modificamos el archivo añadiendo más contenido en modo lectura y escritura simultánea
with open("archivo.txt", "a+") as archivo:
    # nos aseguramos de mover el cursor al final del archivo antes de añadir el nuevo contenido
    archivo.write("¡Añadiendo más líneas al contenido existente!\nEsto es una adición al archivo.\n")

# mostramos el contenido después de la modificación
with open("archivo.txt", "r") as archivo:
    contenido_modificado = archivo.read()
    print("contenido después de la modificación:")
    print(contenido_modificado)

# mostramos el contenido del archivo por pantalla
print("\ncontenido del fichero:")
print(contenido_modificado)
