import random

def encolar(cola, paciente):
    """
    agrega un paciente a la cola basado en su prioridad
    paciente es una tupla (prioridad, nombre, apellido)
    """
    cola.append(paciente)
    cola.sort(reverse=True, key=lambda x: x[0])  # ordenar por prioridad, 10 al principio

def desencolar(cola):
    """
    elimina el paciente con mayor prioridad de la cola
    """
    if cola_vacia(cola):
        print("la cola esta vacia.")
        return None
    return cola.pop(0)

def cola_vacia(cola):
    """
    verifica si la cola esta vacia
    """
    return len(cola) == 0

def frente(cola):
    """
    muestra el paciente con mayor prioridad
    """
    if cola_vacia(cola):
        print("la cola esta vacia.")
        return None
    return cola[0]

def imprimir_cola(cola):
    """
    muestra todos los pacientes en la cola
    """
    if cola_vacia(cola):
        print("la cola esta vacia.")
    else:
        print("contenido de la cola:")
        for prioridad, nombre, apellido in cola:
            print(f"prioridad {prioridad}: {nombre} {apellido}")

def contar(cola):
    """
    muestra el numero de pacientes en la cola
    """
    print(f"numero de pacientes en la cola: {len(cola)}")

def invertir_cola(cola):
    """
    invierte la cola en una nueva lista
    """
    return list(reversed(cola))

def copiar_cola(cola):
    """
    copia el contenido de la cola en otra lista
    """
    return cola[:]

def vaciar_cola(cola):
    """
    vacia completamente la cola
    """
    cola.clear()
    print("la cola ha sido vaciada.")

def guardar_cola(cola, nombre_archivo):
    """
    guarda el contenido de la cola en un archivo
    """
    with open(nombre_archivo, "w") as archivo:
        archivo.write("contenido de la cola:\n")
        for prioridad, nombre, apellido in cola:
            archivo.write(f"prioridad {prioridad}: {nombre} {apellido}\n")
        archivo.write(f"numero total de pacientes: {len(cola)}\n")
    print(f"la cola ha sido guardada en el archivo '{nombre_archivo}'.")

def modulo_priorizacion():
    """
    asigna una prioridad aleatoria entre 1 y 10
    """
    return random.randint(1, 10)

def menu():
    cola = []  # cola inicial

    while True:
        print("\nmenu de opciones:")
        print("1. agregar paciente")
        print("2. atender paciente")
        print("3. mostrar proximo paciente")
        print("4. comprobar si la cola esta vacia")
        print("5. imprimir cola completa")
        print("6. contar pacientes")
        print("7. invertir cola")
        print("8. copiar cola")
        print("9. vaciar cola")
        print("10. guardar cola en un archivo")
        print("11. salir")

        opcion = input("seleccione una opcion: ")

        if opcion == "1":
            nombre = input("ingrese el nombre del paciente: ")
            apellido = input("ingrese el apellido del paciente: ")
            prioridad = modulo_priorizacion()
            encolar(cola, (prioridad, nombre, apellido))
            print(f"paciente {nombre} {apellido} agregado con prioridad {prioridad}.")

        elif opcion == "2":
            paciente = desencolar(cola)
            if paciente:
                print(f"paciente atendido: prioridad {paciente[0]}, {paciente[1]} {paciente[2]}.")

        elif opcion == "3":
            paciente = frente(cola)
            if paciente:
                print(f"proximo paciente: prioridad {paciente[0]}, {paciente[1]} {paciente[2]}.")

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
