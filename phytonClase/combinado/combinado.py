def leer_archivo(nombre_archivo):
    """
    Lee un archivo y devuelve una lista de tuplas con su contenido.
    """
    try:
        with open(nombre_archivo, "r") as archivo:
            return [tuple(linea.strip().split(",")) for linea in archivo]
    except FileNotFoundError:
        print(f"Error: El archivo '{nombre_archivo}' no existe.")
        return []
    except Exception as e:
        print(f"Error inesperado al leer el archivo '{nombre_archivo}': {e}")
        return []

def combinar_informacion(lista1, lista2):
    """
    Combina dos listas basadas en el primer elemento (nombre) y devuelve una lista combinada.
    """
    # Crear diccionarios para acceso rápido
    dict1 = {nombre: valor for nombre, valor in lista1}
    dict2 = {nombre: valor for nombre, valor in lista2}

    # Crear conjunto de todos los nombres
    nombres = set(dict1.keys()).union(dict2.keys())

    # Combinar la información
    combinada = []
    for nombre in nombres:
        edad = dict1.get(nombre, "N/A")
        correo = dict2.get(nombre, "N/A")
        combinada.append((nombre, edad, correo))

    return combinada

def guardar_archivo(nombre_archivo, datos):
    """
    Guarda la información combinada en un archivo.
    """
    try:
        with open(nombre_archivo, "w") as archivo:
            archivo.write("Nombre,Edad,Correo\n")
            for nombre, edad, correo in datos:
                archivo.write(f"{nombre},{edad},{correo}\n")
        print(f"La información combinada ha sido guardada en '{nombre_archivo}'.")
    except Exception as e:
        print(f"Error al guardar en el archivo '{nombre_archivo}': {e}")

def mostrar_resultados(datos):
    """
    Muestra los resultados combinados en consola.
    """
    print("\nInformación combinada:")
    print("Nombre,Edad,Correo")
    for nombre, edad, correo in datos:
        print(f"{nombre},{edad},{correo}")

def main():
    nombres_edades = leer_archivo("nombres_edades.txt")
    nombres_correos = leer_archivo("nombres_correos.txt")

    if not nombres_edades and not nombres_correos:
        print("No se pudo procesar ningún archivo. Saliendo del programa.")
        return

    informacion_combinada = combinar_informacion(nombres_edades, nombres_correos)

    guardar_archivo("info.txt", informacion_combinada)
    mostrar_resultados(informacion_combinada)


main()
