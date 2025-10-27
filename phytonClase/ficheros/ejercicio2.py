"""Ejercicio 2: Escritura en un archivo
Escribe un programa que cree un nuevo archivo llamado nuevo.txt y escriba algunas
líneas de texto en él en modo escritura (w).
Abre el archivo en modo lectura (r) y muestra el contenido en la consola."""



def escribir_y_leer_archivo():
    try:
        # crea un nuevo archivo llamado nuevo.txt y escribe texto en él
        with open("nuevo.txt", "w") as archivo:
            archivo.write("Esta es la primera línea.\n")
            archivo.write("Esta es la segunda línea.\n")
            archivo.write("¡Python facilita trabajar con archivos!\n")
        print("Texto escrito exitosamente en 'nuevo.txt'.")

        # abre el archivo en modo lectura y muestra su contenido
        with open("nuevo.txt", "r") as archivo:
            contenido = archivo.read()
            print("\nContenido del archivo:")
            print(contenido)

    except Exception as e:
        print(f"Se produjo un error: {e}")  # maneja cualquier error inesperado


escribir_y_leer_archivo()
