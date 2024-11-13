#9- Implementa un algoritmo que reciba dos tuplas de cualquier tamaño con valores
#enteros y realice las siguientes operaciones:
#- Devuelve una nueva tupla con la intersección de elementos (aquellos elementos
#comunes a ambas tuplas).
#- Devuelve una nueva tupla con la diferencia de elementos de la primera tupla
#con respecto a la segunda (aquellos elementos que están en una tupla pero no
#la otra)
#Ejemplo:

#tupla1 = (1, 2, 3, 4, 5)
#tupla2 = (3, 4, 5, 6, 7)
# Intersección: (3, 4, 5)
# Diferencia: (1,2,6,7)

# funcion ke recibe dos tuplas y devuelve la interseccion y diferencia entre ellas
def operaciones_tuplas(tupla1, tupla2):
    # convertimos las tuplas a conjuntos pa hacer operaciones mas facil
    conjunto1 = set(tupla1)
    conjunto2 = set(tupla2)
    
    # Interseccion: saca los elementos ke estan en las dos tuplas
    interseccion = tuple(conjunto1.intersection(conjunto2))
    
    # Diferencia simetrica: toma los elementos ke estan en una pero no en la otra
    diferencia = tuple(conjunto1.symmetric_difference(conjunto2))
    
    # devuelve los resultados en forma de tuplas
    return interseccion, diferencia

# Ejemplo de uso
tupla1 = (1, 2, 3, 4, 5)  # primera tupla con algunos valores
tupla2 = (3, 4, 5, 6, 7)  # segunda tupla con otros valores

# llamamos a la funcion y guardamos los resultados en variables
resultado_interseccion, resultado_diferencia = operaciones_tuplas(tupla1, tupla2)

# imprimimos la interseccion, osea los elementos comunes de las dos tuplas
print("Intersección:", resultado_interseccion)

# imprimimos la diferencia, los elementos unicos ke no coinciden
print("Diferencia:", resultado_diferencia)
