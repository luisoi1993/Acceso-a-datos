#8- Desempaqueta el valor de cada respuesta almacenada en la tupla del ejercicio
#anterior.
#Desempaquetar significa sustituir el bucle for del ejercicio anterior que imprimía el
#contenido de la tupla, por una función que utilice la siguiente sintaxis:

#def desempaquetar_tupla(tupla):
#(a, x), (b, y), (c, z) = tupla
#print(f"El valor {a} vale {x}")
#print(f"El valor {b} vale {y}")
#print(f"El valor {c} vale {z}")

#de forma que recibe una tupla e imprime por pantalla el contenido de cada par
#de elementos que contiene la tupla.

# tupla de las respuestas del ejersicio anterior
# aqui tenemos 3 pares de valores 
respuestas = (("A", 10), ("B", 20), ("C", 30))

# funcion para sacar cada valor de la tupla sin usar el for
def desempaquetar_tupla(tupla):
    # esto desempaca cada par de valores en la tupla
    (a, x), (b, y), (c, z) = tupla
    # imprime los valores para cada par 
    print(f"El valor {a} vale {x}")
    print(f"El valor {b} vale {y}")
    print(f"El valor {c} vale {z}")

# llamamos a la funcion con la tupla que creamos arriba 
desempaquetar_tupla(respuestas)
