def crear_nodo(valor):
    # crea un nodo con un valor y sin hijos
    return {"valor": valor, "izquierdo": None, "derecho": None}

def es_vacio(arbol):
    # verifica si el arbol no tiene hijos (es una hoja)
    return arbol is None

def insertar(arbol, valor):
    if es_vacio(arbol):
        # si el arbol está vacío, se crea el nodo raíz
        return crear_nodo(valor)
    if valor < arbol["valor"]:
        # si el valor es menor, va al subarbol izquierdo
        arbol["izquierdo"] = insertar(arbol["izquierdo"], valor)
    elif valor > arbol["valor"]:
        # si el valor es mayor, va al subarbol derecho
        arbol["derecho"] = insertar(arbol["derecho"], valor)
    return arbol

def imprimir_arbol(arbol, nivel=0):
    if not es_vacio(arbol):
        # imprime el subarbol derecho
        imprimir_arbol(arbol["derecho"], nivel + 1)
        # imprime el nodo actual con indentación
        print("   " * nivel + f"{arbol['valor']}")
        # imprime el subarbol izquierdo
        imprimir_arbol(arbol["izquierdo"], nivel + 1)

def contar_nodos(arbol):
    if es_vacio(arbol):
        return 0
    # cuenta el nodo actual más los nodos de los subarboles
    return 1 + contar_nodos(arbol["izquierdo"]) + contar_nodos(arbol["derecho"])

# probando el árbol con los datos indicados
datos = [45, 23, 67, 12, 34, 56, 78, 10, 25, 50, 60, 70, 80, 15]
arbol = None

for dato in datos:
    arbol = insertar(arbol, dato)

print("Árbol Binario de Búsqueda:")
imprimir_arbol(arbol)

print("\nNúmero total de nodos:", contar_nodos(arbol))
