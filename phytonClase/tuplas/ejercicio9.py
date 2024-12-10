"""9- Implementa un algoritmo que reciba dos tuplas de cualquier tamaño con valores
enteros y realice las siguientes operaciones:
- Devuelve una nueva tupla con la intersección de elementos (aquellos elementos
comunes a ambas tuplas).
- Devuelve una nueva tupla con la diferencia de elementos de la primera tupla
con respecto a la segunda (aquellos elementos que están en una tupla pero no
la otra)
Ejemplo:

tupla1 = (1, 2, 3, 4, 5)
tupla2 = (3, 4, 5, 6, 7)
# Intersección: (3, 4, 5)
# Diferencia: (1,2,6,7)"""

tupla1 = (1, 2, 3, 4, 5)
tupla2 = (3, 4, 5, 6, 7)

# Calculamos la intersección usando conjuntos
interseccion = tuple(set(tupla1) & set(tupla2))

# Calculamos la diferencia simétrica (elementos únicos en ambas tuplas)
diferencia = tuple(set(tupla1) ^ set(tupla2))


print("Intersección:", interseccion)
print("Diferencia:", diferencia)
