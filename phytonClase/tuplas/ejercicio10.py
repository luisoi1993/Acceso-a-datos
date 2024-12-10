"""10. Dada una tupla de tuplas que contiene valores de distintas ciudades y sus
temperaturas en los últimos días, crea un programa que busque si una ciudad específica
está en la tupla y devuelva la media de todas las temperaturas registradas para esa
ciudad.
Ejemplo:
ciudades_temperaturas = (("Madrid", (30, 32, 31)), ("Barcelona", (20, 26, 21)), ("Valencia", (28, 29, 27)))
Barcelona -> 22,3"""


ciudades_temperaturas = (
    ("Madrid", (30, 32, 31)),
    ("Barcelona", (20, 26, 21)),
    ("Valencia", (28, 29, 27))
)

ciudad_buscada = input("Introduce el nombre de la ciudad: ")

# Buscamos la ciudad en la tupla
encontrada = False
for ciudad, temperaturas in ciudades_temperaturas:
    if ciudad.lower() == ciudad_buscada.lower():  # Comparamos sin distinguir entre mayúsculas y minúsculas
        encontrada = True
        media = sum(temperaturas) / len(temperaturas)
        print(f"La media de las temperaturas en {ciudad} es: {media:.1f}")
        break

if not encontrada:
    print(f"La ciudad '{ciudad_buscada}' no está en la lista.")
