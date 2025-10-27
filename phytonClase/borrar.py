# Crear un nodo como un diccionario
def crear_nodo(dato):
    return {"dato": dato, "siguiente": None}

# Agregar un nodo al final de la lista
def agregar(cabeza, dato):
    nuevo_nodo = crear_nodo(dato)
    if cabeza is None:  # Si la lista está vacía
        return nuevo_nodo
    actual = cabeza
    while actual["siguiente"]:  # Buscar el último nodo
        actual = actual["siguiente"]
    actual["siguiente"] = nuevo_nodo  # Enlazar el nuevo nodo
    return cabeza

# Mostrar todos los datos de la lista
def mostrar(cabeza):
    actual = cabeza
    while actual:  # Recorre cada nodo
        print(actual["dato"], end=" -> ")
        actual = actual["siguiente"]
    print("None")  # Indica el final de la lista

# Eliminar un nodo con un dato específico
def eliminar(cabeza, dato):
    if cabeza is None:  # Lista vacía
        print("La lista está vacía.")
        return None
    if cabeza["dato"] == dato:  # Eliminar la cabeza
        return cabeza["siguiente"]
    actual = cabeza
    while actual["siguiente"] and actual["siguiente"]["dato"] != dato:
        actual = actual["siguiente"]
    if actual["siguiente"]:  # Si encontró el nodo, lo salta
        actual["siguiente"] = actual["siguiente"]["siguiente"]
    else:
        print(f"El dato {dato} no está en la lista.")
    return cabeza

# Ejemplo de uso
if __name__ == "__main__":
    cabeza = None  # Inicia lista vacía

    # Agregar elementos
    cabeza = agregar(cabeza, 10)
    cabeza = agregar(cabeza, 20)
    cabeza = agregar(cabeza, 30)

    print("Lista después de agregar elementos:")
    mostrar(cabeza)

    # Eliminar un elemento
    cabeza = eliminar(cabeza, 20)
    print("Lista después de eliminar el 20:")
    mostrar(cabeza)

    # Intentar eliminar un dato que no existe
    cabeza = eliminar(cabeza, 40)
