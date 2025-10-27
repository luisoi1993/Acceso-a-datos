"""Ejercicio 1: Lectura de un archivo
Crea un archivo de texto llamado archivo.txt y escribe algunas líneas de texto en él.
Escribe un programa en Python que abra y lea el contenido del archivo en modo
lectura (r) y lo imprima en la consola."""

def leer_archivo():
    try:
        # abre el archivo archivo.txt en modo lectura
        with open("archivo.txt", "r") as archivo:
            contenido = archivo.read()  # lee el contenido completo del archivo
            print("Contenido del archivo:")
            print(contenido)  # muestra el contenido en la consola
    except FileNotFoundError:
        print("Error: El archivo 'archivo.txt' no existe.")  # maneja si el archivo no se encuentra
    except Exception as e:
        print(f"Se produjo un error inesperado: {e}")  # maneja otros errores inesperados


leer_archivo()
