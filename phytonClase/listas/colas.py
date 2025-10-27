def encolar(cola, elemento):
    # se añade el elemento al final de la cola
    cola.append(elemento)

def desencolar(cola):
    # si la cola esta vacia no se puede quitar elementos
    if cola_vacia(cola):
        print("la cola esta vacia.")
        return None
    # se quita el primer elemento de la cola
    return cola.pop(0)

def cola_vacia(cola):
    # revisa si la cola tiene elementos o no
    return len(cola) == 0

def frente(cola):
    # si la cola esta vacia no tiene frente
    if cola_vacia(cola):
        print("la cola esta vacia.")
        return None
    # devuelve el primer elemento de la cola
    return cola[0]

def imprimir_cola(cola):
    # muestra todos los elementos de la cola
    if cola_vacia(cola):
        print("la cola esta vacia.")
    else:
        print("contenido de la cola:")
        for elemento in cola:
            print(elemento)

def contar(cola):
    # muestra cuantos elementos hay en la cola
    print(f"numero de elementos en la cola: {len(cola)}")

def invertir_cola(cola):
    # copia los elementos en una nueva cola pero al reves
    cola_invertida = []
    for elemento in reversed(cola):
        encolar(cola_invertida, elemento)
    return cola_invertida

def copiar_cola(cola):
    # copia todos los elementos en una nueva cola
    cola_copiada = []
    for elemento in cola:
        encolar(cola_copiada, elemento)
    return cola_copiada

def vaciar_cola(cola):
    # borra todos los elementos de la cola
    cola.clear()
    print("la cola ha sido vaciada.")

def guardar_cola(cola, nombre_archivo):
    # guarda el contenido de la cola en un archivo
    with open(nombre_archivo, "w") as archivo:
        archivo.write("contenido de la cola:\n")
        for elemento in cola:
            archivo.write(f"{elemento}\n")
        archivo.write(f"numero total de elementos: {len(cola)}\n")
    print(f"la cola ha sido guardada en el archivo '{nombre_archivo}'.")

def menu():
    cola = []
    while True:
        print("\nmenu de opciones:")
        print("1. encolar animal vertebrado")
        print("2. desencolar animal vertebrado")
        print("3. mostrar frente de la cola")
        print("4. comprobar si la cola esta vacia")
        print("5. imprimir cola")
        print("6. contar elementos en la cola")
        print("7. invertir cola")
        print("8. copiar cola")
        print("9. vaciar cola")
        print("10. guardar cola en un archivo")
        print("11. salir")

        opcion = input("seleccione una opcion: ")

        if opcion == "1":
            animal = input("ingrese el nombre del animal vertebrado: ")
            encolar(cola, animal)
        elif opcion == "2":
            desencolado = desencolar(cola)
            if desencolado:
                print(f"elemento desencolado: {desencolado}")
        elif opcion == "3":
            frente_cola = frente(cola)
            if frente_cola:
                print(f"el frente de la cola es: {frente_cola}")
        elif opcion == "4":
            if cola_vacia(cola):
                print("la cola esta vacia.")
            else:
                print("la cola no esta vacia.")
        elif opcion == "5":
            imprimir_cola(cola)
        elif opcion == "6":
            contar(cola)
        elif opcion == "7":
            cola_invertida = invertir_cola(cola)
            print("cola invertida:")
            imprimir_cola(cola_invertida)
        elif opcion == "8":
            cola_copiada = copiar_cola(cola)
            print("cola copiada:")
            imprimir_cola(cola_copiada)
        elif opcion == "9":
            vaciar_cola(cola)
        elif opcion == "10":
            nombre_archivo = input("ingrese el nombre del archivo para guardar la cola: ")
            guardar_cola(cola, nombre_archivo)
        elif opcion == "11":
            print("saliendo del programa...")
            break
        else:
            print("opcion no valida. intente nuevamente.")


menu()
