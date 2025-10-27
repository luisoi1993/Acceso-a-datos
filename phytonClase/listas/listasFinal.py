# listas enlazadas, doblemente enlazadas, circulares enlazadas y circulares doblemente enlazadas

def lista_vacia(lista):
    # devuelve True si la lista está vacía, False en caso contrario
    return len(lista) == 0

def crear_nodo(valor):
    # crea un nodo con el valor dado
    return {"valor": valor, "siguiente": None, "anterior": None}

def insertar_inicio(lista, nodo):
    # Inserta un nodo al inicio de la lista
    if lista_vacia(lista):
        lista.append(nodo)
    else:
        nodo["siguiente"] = lista[0]
        lista[0]["anterior"] = nodo
        lista.insert(0, nodo)

def insertar_final(lista, nodo):
    # Inserta un nodo al final de la lista
    if lista_vacia(lista):
        lista.append(nodo)
    else:
        ultimo = lista[-1]
        ultimo["siguiente"] = nodo
        nodo["anterior"] = ultimo
        lista.append(nodo)

def insertar_nodo(lista, nodo_nuevo, valor_existente, posicion="despues"):
    # Inserta un nodo nuevo antes o después de un nodo existente
    for nodo in lista:
        if nodo["valor"] == valor_existente:
            if posicion == "despues":
                nodo_nuevo["siguiente"] = nodo["siguiente"]
                if nodo["siguiente"]:
                    nodo["siguiente"]["anterior"] = nodo_nuevo
                nodo["siguiente"] = nodo_nuevo
                nodo_nuevo["anterior"] = nodo
            elif posicion == "antes":
                nodo_nuevo["anterior"] = nodo["anterior"]
                if nodo["anterior"]:
                    nodo["anterior"]["siguiente"] = nodo_nuevo
                nodo["anterior"] = nodo_nuevo
                nodo_nuevo["siguiente"] = nodo
            lista.insert(lista.index(nodo) + (1 if posicion == "despues" else 0), nodo_nuevo)
            break

def contar_nodos(lista):
    # Devuelve la cantidad de nodos en la lista
    return len(lista)

def eliminar_nodo(lista, valor):
    # Elimina un nodo de la lista por su valor
    for nodo in lista:
        if nodo["valor"] == valor:
            if nodo["anterior"]:
                nodo["anterior"]["siguiente"] = nodo["siguiente"]
            if nodo["siguiente"]:
                nodo["siguiente"]["anterior"] = nodo["anterior"]
            lista.remove(nodo)
            break

def imprimir_valor_lista(lista):
    # Imprime solo los valores de los nodos
    for nodo in lista:
        print(nodo["valor"], end=" -> ")
    print("None")

def imprimir_lista_completa(lista):
    # Imprime el valor y las conexiones de cada nodo
    for nodo in lista:
        print(f"Nodo: {nodo['valor']}, Siguiente: {nodo['siguiente']['valor'] if nodo['siguiente'] else None}, Anterior: {nodo['anterior']['valor'] if nodo['anterior'] else None}")

def imprimir_reves(lista):
    # Imprime la lista desde el final al principio
    for nodo in reversed(lista):
        print(nodo["valor"], end=" <- ")
    print("None")

def buscar_nodo(lista, valor):
    # Busca un nodo por su valor
    for nodo in lista:
        if nodo["valor"] == valor:
            return nodo
    return None

def copiar_lista(lista, tipo):
    # Copia la lista en un archivo según el tipo de lista
    nombre_archivo = f"lista_{tipo}.txt"
    with open(nombre_archivo, "w") as archivo:
        for nodo in lista:
            archivo.write(f"Nodo: {nodo['valor']}, Siguiente: {nodo['siguiente']['valor'] if nodo['siguiente'] else None}, Anterior: {nodo['anterior']['valor'] if nodo['anterior'] else None}\n")
    print(f"Lista copiada en {nombre_archivo}")

# Ejemplo de uso con las cuatro listas
def ejemplo():
    # Lista enlazada
    lista_enlazada = []
    nodo1 = crear_nodo(1)
    nodo2 = crear_nodo(2)
    nodo3 = crear_nodo(3)
    insertar_inicio(lista_enlazada, nodo1)
    insertar_final(lista_enlazada, nodo2)
    insertar_nodo(lista_enlazada, nodo3, 1, "despues")
    print("\nLista Enlazada:")
    imprimir_valor_lista(lista_enlazada)
    imprimir_lista_completa(lista_enlazada)
    
    # Lista doblemente enlazada
    lista_doble = []
    nodo1 = crear_nodo(1)
    nodo2 = crear_nodo(2)
    nodo3 = crear_nodo(3)
    insertar_inicio(lista_doble, nodo1)
    insertar_final(lista_doble, nodo2)
    insertar_nodo(lista_doble, nodo3, 1, "antes")
    print("\nLista Doble Enlazada:")
    imprimir_valor_lista(lista_doble)
    imprimir_lista_completa(lista_doble)
    
    # Lista circular enlazada
    lista_circular = []
    nodo1 = crear_nodo(1)
    nodo2 = crear_nodo(2)
    nodo3 = crear_nodo(3)
    insertar_inicio(lista_circular, nodo1)
    insertar_final(lista_circular, nodo2)
    insertar_nodo(lista_circular, nodo3, 1, "despues")
    lista_circular[-1]["siguiente"] = lista_circular[0]  # Hacerla circular
    print("\nLista Circular Enlazada:")
    imprimir_valor_lista(lista_circular)

    # Lista circular doblemente enlazada
    lista_circular_doble = []
    nodo1 = crear_nodo(1)
    nodo2 = crear_nodo(2)
    nodo3 = crear_nodo(3)
    insertar_inicio(lista_circular_doble, nodo1)
    insertar_final(lista_circular_doble, nodo2)
    insertar_nodo(lista_circular_doble, nodo3, 1, "antes")
    lista_circular_doble[-1]["siguiente"] = lista_circular_doble[0]  # Circular
    lista_circular_doble[0]["anterior"] = lista_circular_doble[-1]
    print("\nLista Circular Doble Enlazada:")
    imprimir_lista_completa(lista_circular_doble)


ejemplo()

