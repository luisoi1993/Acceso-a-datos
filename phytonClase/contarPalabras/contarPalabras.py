def contar_palabras(archivo_entrada, archivo_salida):
    try:
        # abro el archivo pa leer lo que tiene dentro
        with open(archivo_entrada, "r", encoding="utf-8") as file:
            contenido = file.read()

        # parto el texto en palabras usando split, es como cortar en trozos
        palabras = contenido.split()
        numero_palabras = len(palabras)  # cuento cuantas palabras hay

        # lo muestro en la consola pa que se vea
        print(f"el archivo '{archivo_entrada}' tiene {numero_palabras} palabras.")

        # ahora creo otro archivo y meto el numero ahi
        with open(archivo_salida, "w", encoding="utf-8") as file:
            file.write(f"el archivo '{archivo_entrada}' tiene {numero_palabras} palabras.\n")
        
        # aviso que ya ta guardado
        print(f"el resultado se guardo en el archivo '{archivo_salida}'.")

    except FileNotFoundError:
        # si no encuentra el archivo, aviso que no existe
        print(f"error: no esta el archivo '{archivo_entrada}'.")
    except Exception as e:
        # si pasa algo raro, lo muestro
        print(f"paso algo raro: {e}")

# rutas de los archivos que uso pa el programa
archivo_entrada = "texto_ini.txt"
archivo_salida = "texto_sal.txt"

# llamo a la funcion pa que haga todo
contar_palabras(archivo_entrada, archivo_salida)
