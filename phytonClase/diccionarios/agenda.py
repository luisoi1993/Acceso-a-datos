
"""- Escribe un programa en Python que permita gestionar una utilizando un diccionario.
El programa debe ofrecer al usuario un menú con las siguientes opciones:: Permite añadir un nuevo contacto a la agenda. 
El usuario debe ingresar el nombre, el número de teléfono y su email. Si el nombre ya existe en la agenda, se debe mostrar un mensaje
indicando que el contacto ya existe.: Permite buscar el número de teléfono de un contacto ingresando su nombre. Si el contacto no existe,
se debe mostrar un mensaje indicándolo.: Permite modificar el número de teléfono de un contacto existente. Si el contacto no existe,
se debe mostrar un mensaje indicándolo.: Permite eliminar un contacto de la agenda. Si el contacto no existe, se debe mostrar un mensaje 
indicándolo.: Muestra una lista de todos los contactos en la agenda con sus respectivos números de teléfono.: Termina la ejecución del programa."""


def mostrar_menu():
    print("\n--- Menú de la Agenda ---")
    print("1. Añadir contacto")
    print("2. Buscar contacto")
    print("3. Modificar contacto")
    print("4. Eliminar contacto")
    print("5. Mostrar todos los contactos")
    print("6. Salir")

def añadir_contacto(agenda):
    nombre = input("Introduce el nombre del contacto: ").strip()
    if nombre in agenda:
        print("El contacto ya existe.")
    else:
        telefono = input("Introduce el número de teléfono: ").strip()
        email = input("Introduce el email: ").strip()
        agenda[nombre] = {"teléfono": telefono, "email": email}
        print(f"Contacto '{nombre}' añadido correctamente.")

def buscar_contacto(agenda):
    nombre = input("Introduce el nombre del contacto a buscar: ").strip()
    if nombre in agenda:
        print(f"Teléfono: {agenda[nombre]['teléfono']}, Email: {agenda[nombre]['email']}")
    else:
        print("El contacto no existe.")

def modificar_contacto(agenda):
    nombre = input("Introduce el nombre del contacto a modificar: ").strip()
    if nombre in agenda:
        nuevo_telefono = input("Introduce el nuevo número de teléfono: ").strip()
        agenda[nombre]["teléfono"] = nuevo_telefono
        print(f"Teléfono de '{nombre}' actualizado correctamente.")
    else:
        print("El contacto no existe.")

def eliminar_contacto(agenda):
    nombre = input("Introduce el nombre del contacto a eliminar: ").strip()
    if nombre in agenda:
        del agenda[nombre]
        print(f"Contacto '{nombre}' eliminado correctamente.")
    else:
        print("El contacto no existe.")

def mostrar_contactos(agenda):
    if agenda:
        print("\n--- Lista de contactos ---")
        for nombre, datos in agenda.items():
            print(f"{nombre}: Teléfono: {datos['teléfono']}, Email: {datos['email']}")
    else:
        print("La agenda está vacía.")

# Programa principal
agenda = {}
while True:
    mostrar_menu()
    opcion = input("Selecciona una opción: ").strip()
    if opcion == "1":
        añadir_contacto(agenda)
    elif opcion == "2":
        buscar_contacto(agenda)
    elif opcion == "3":
        modificar_contacto(agenda)
    elif opcion == "4":
        eliminar_contacto(agenda)
    elif opcion == "5":
        mostrar_contactos(agenda)
    elif opcion == "6":
        print("Saliendo del programa. ¡Hasta luego!")
        break
    else:
        print("Opción no válida. Inténtalo de nuevo.")
