"""La siguiente práctica consiste en implementar en Python un programa que
permita crear listas mediante la simulación de punteros.
Tendrá que permitir crear las siguientes opciones:
1- Listas enlazadas
2- Listas doblemente enlazadas
3- Listas circulares enlazadas
4- Listas circulares doblemente enlazadas
Los valores (datos) de las listas serán todos números enteros comprendidos
entre el 1 y el 98.
Se deberán implementa al menos las siguientes funciones:
Lista_Vacia
Función que devuelve si la lista está vacía o no.
crear_nodo
Función que crea la estructura de datos de un nodo y su contenido.
insertar_inicio
Función que añade un nuevo nodo al inicio de la lista. Si la lista está vacía, la
crea con el valor correspondiente.
insertar_nodo
Función que añade un nodo nuevo entre otros dos nodos ya existentes, por lo
que se deberá indicar detrás o delante de qué nodo debe insertarse.
insertar_final
Función que añade un nodo al final de la lista. Si la lista está vacía, no podrá
insertar ningún nodo.
contar_nodos
Función que devuelve el número de nodos de una lista
eliminar_nodo
Función que le pide al usuario un nodo y si está, se elimina de la lista.
imprimir_valor_lista
Función que imprime el valor de cada nodo por pantalla.

imprimir_lista_completa
Función que imprime todos los campos de cada nodo, por lo que mostrará por
pantalla para cada nodo, el dato que almacena y los nodos con los que está
conectado.
imprimir_reves
Función que imprime la lista desde el final al principio.
buscar_nodo
Función que busca un nodo dentro de la lista
copiar_lista.
Función que copia una lista (con toda la información de sus nodos) a un fichero
llamado "lista_tipo.txt", de forma que "tipo" puede tomar los siguientes valores
en función del tipo de lista que es:
enlazada en este caso el fichero se llamará "lista_enlazada.txt"
enlazada_d en este caso el fichero se llamará "lista_enlazada_d.txt"
circular en este caso el fichero se llamará "lista_circular.txt"
circular_d. en este caso el fichero se llamará "lista_circular_d.txt"
El formato en el que se copian y se visualizan los nodos tendrá que ser de
forma que los usuarios entiendan la relación entre nodos y su valor."""


# representación de nodos mediante diccionarios
def crear_nodo(valor):
    return {"valor": valor, "siguiente": None, "anterior": None}

# función para verificar si la lista está vacía
def lista_vacia(lista):
    return lista == []

# insertar al inicio de la lista
def insertar_inicio(lista, valor):
    nuevo_nodo = crear_nodo(valor)
    if lista_vacia(lista):
        lista.append(nuevo_nodo)
    else:
        nuevo_nodo["siguiente"] = lista[0]
        lista[0]["anterior"] = nuevo_nodo
        lista.insert(0, nuevo_nodo)

# insertar al final de la lista
def insertar_final(lista, valor):
    if lista_vacia(lista):
        print("La lista está vacía. Usa insertar_inicio para agregar el primer nodo.")
    else:
        nuevo_nodo = crear_nodo(valor)
        ultimo = lista[-1]
        ultimo["siguiente"] = nuevo_nodo
        nuevo_nodo["anterior"] = ultimo
        lista.append(nuevo_nodo)

# insertar un nodo detrás de un valor específico
def insertar_nodo(lista, valor, referencia):
    nuevo_nodo = crear_nodo(valor)
    for nodo in lista:
        if nodo["valor"] == referencia:
            siguiente = nodo["siguiente"]
            nodo["siguiente"] = nuevo_nodo
            nuevo_nodo["anterior"] = nodo
            if siguiente:
                siguiente["anterior"] = nuevo_nodo
            nuevo_nodo["siguiente"] = siguiente
            lista.insert(lista.index(nodo) + 1, nuevo_nodo)
            return
    print(f"El nodo con valor {referencia} no se encontró.")

# contar nodos de la lista
def contar_nodos(lista):
    return len(lista)

# eliminar un nodo por valor
def eliminar_nodo(lista, valor):
    for nodo in lista:
        if nodo["valor"] == valor:
            anterior = nodo["anterior"]
            siguiente = nodo["siguiente"]
            if anterior:
                anterior["siguiente"] = siguiente
            if siguiente:
                siguiente["anterior"] = anterior
            lista.remove(nodo)
            return
    print(f"El nodo con valor {valor} no se encontró.")

# imprimir los valores de la lista
def imprimir_valor_lista(lista):
    for nodo in lista:
        print(nodo["valor"], end=" -> ")
    print("None")

# imprimir la lista completa con las conexiones
def imprimir_lista_completa(lista):
    for nodo in lista:
        anterior = nodo["anterior"]["valor"] if nodo["anterior"] else None
        siguiente = nodo["siguiente"]["valor"] if nodo["siguiente"] else None
        print(f"Nodo: {nodo['valor']}, Anterior: {anterior}, Siguiente: {siguiente}")

# imprimir la lista en orden inverso
def imprimir_reves(lista):
    for nodo in reversed(lista):
        print(nodo["valor"], end=" <- ")
    print("None")

# buscar un nodo por valor
def buscar_nodo(lista, valor):
    for nodo in lista:
        if nodo["valor"] == valor:
            return nodo
    return None

# copiar la lista en un archivo
def copiar_lista(lista, tipo):
    nombre_archivo = f"lista_{tipo}.txt"
    with open(nombre_archivo, "w") as archivo:
        for nodo in lista:
            anterior = nodo["anterior"]["valor"] if nodo["anterior"] else None
            siguiente = nodo["siguiente"]["valor"] if nodo["siguiente"] else None
            archivo.write(f"Nodo: {nodo['valor']}, Anterior: {anterior}, Siguiente: {siguiente}\n")
    print(f"Lista copiada en el archivo {nombre_archivo}.")

# ejemplo de uso
mi_lista = []
insertar_inicio(mi_lista, 10)
insertar_inicio(mi_lista, 20)
insertar_final(mi_lista, 5)
insertar_nodo(mi_lista, 15, 10)
imprimir_valor_lista(mi_lista)
imprimir_lista_completa(mi_lista)
print("Nodos en la lista:", contar_nodos(mi_lista))
eliminar_nodo(mi_lista, 10)
imprimir_valor_lista(mi_lista)
imprimir_reves(mi_lista)
copiar_lista(mi_lista, "enlazada")
