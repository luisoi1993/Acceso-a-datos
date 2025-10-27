"""Ejercicio 3: Agregar contenido a un archivo
Añade más líneas de texto al archivo nuevo.txt en modo adición (a).
Vuelve a abrir el archivo en modo lectura (r) y muestra el contenido en la consola."""

def agregar_y_leer_archivo():
    try:
        # abre el archivo en modo adición (append) y añade más líneas
        with open("nuevo.txt", "a") as archivo:
            archivo.write("Esta es una línea añadida en modo adición.\n")
            archivo.write("Seguimos aprendiendo sobre archivos en Python.\n")
        print("Texto añadido exitosamente a 'nuevo.txt'.")

        # abre el archivo en modo lectura y muestra su contenido
        with open("nuevo.txt", "r") as archivo:
            contenido = archivo.read()
            print("\nContenido actualizado del archivo:")
            print(contenido)

    except Exception as e:
        print(f"Se produjo un error: {e}")  # maneja cualquier error inesperado


agregar_y_leer_archivo()
