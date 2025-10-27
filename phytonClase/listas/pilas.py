def apilar(pila, elemento):
    # esto es pa meter algo en la pila, usamos append pa añadir el elemento al final
    pila.append(elemento)

def desapilar(pila):
    # aki sacamos el ultimo elemento de la pila, pero antes miramos si esta vacia
    if pila_vacia(pila):
        print("La pila está vacía.")
        return None
    return pila.pop()

def pila_vacia(pila):
    # esta funcion solo dice si la pila no tiene nada dentro, devuelve true o false
    return len(pila) == 0

def tope(pila):
    # aki miramos el ultimo elemento de la pila sin quitarlo, si esta vacia decimos eso
    if pila_vacia(pila):
        print("La pila está vacía.")
        return None
    return pila[-1]

def imprimir_pila(pila):
    # esta sirve pa enseñar todos los elementos de la pila, de arriba a abajo
    if pila_vacia(pila):
        print("La pila está vacía.")
    else:
        print("Contenido de la pila:")
        for elemento in reversed(pila):
            print(elemento)

def contar(pila):
    # con esta contamos cuantos elementos tiene la pila y lo mostramos en pantalla
    print(f"Número de elementos en la pila: {len(pila)}")

def invertir_pila(pila):
    # esto hace una nueva pila pero con los elementos al reves que la original
    pila_invertida = []
    for elemento in reversed(pila):
        apilar(pila_invertida, elemento)
    return pila_invertida

def copiar_pila(pila):
    # aki copiamos todos los elementos de una pila en otra nueva sin cambiar el orden
    pila_copiada = []
    for elemento in pila:
        apilar(pila_copiada, elemento)
    return pila_copiada

def vaciar_pila(pila):
    # con esta quitamos todo lo que hay en la pila y la dejamos vacia
    pila.clear()
    print("La pila ha sido vaciada.")

def guardar_pila(pila, nombre_archivo):
    # esta funcion guarda los datos de la pila en un archivo de texto pa no perderlos
    with open(nombre_archivo, "w") as archivo:
        archivo.write("Contenido de la pila:\n")
        for elemento in reversed(pila):
            archivo.write(f"{elemento}\n")
        archivo.write(f"Número total de elementos: {len(pila)}\n")
    print(f"La pila ha sido guardada en el archivo '{nombre_archivo}'.")

def menu():
    pila = []
    while True:
        print("\nMenú de opciones:")
        print("1. Apilar marca de coche")
        print("2. Desapilar marca de coche")
        print("3. Mostrar tope de la pila")
        print("4. Comprobar si la pila está vacía")
        print("5. Imprimir pila")
        print("6. Contar elementos en la pila")
        print("7. Invertir pila")
        print("8. Copiar pila")
        print("9. Vaciar pila")
        print("10. Guardar pila en un archivo")
        print("11. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            marca = input("Ingrese la marca de coche: ")
            apilar(pila, marca)
        elif opcion == "2":
            desapilado = desapilar(pila)
            if desapilado:
                print(f"Elemento desapilado: {desapilado}")
        elif opcion == "3":
            tope_pila = tope(pila)
            if tope_pila:
                print(f"El tope de la pila es: {tope_pila}")
        elif opcion == "4":
            if pila_vacia(pila):
                print("La pila está vacía.")
            else:
                print("La pila no está vacía.")
        elif opcion == "5":
            imprimir_pila(pila)
        elif opcion == "6":
            contar(pila)
        elif opcion == "7":
            pila_invertida = invertir_pila(pila)
            print("Pila invertida:")
            imprimir_pila(pila_invertida)
        elif opcion == "8":
            pila_copiada = copiar_pila(pila)
            print("Pila copiada:")
            imprimir_pila(pila_copiada)
        elif opcion == "9":
            vaciar_pila(pila)
        elif opcion == "10":
            nombre_archivo = input("Ingrese el nombre del archivo para guardar la pila: ")
            guardar_pila(pila, nombre_archivo)
        elif opcion == "11":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

menu()
