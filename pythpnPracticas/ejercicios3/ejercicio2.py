numero = input("Introduce un número entero: ")

suma_digitos = sum(int(digito) for digito in numero)

detalle = " + .".join(numero)
print(f"La suma de los digitos es: {detalle} = {suma_digitos}")
# Pedimos al usuario que ingrese un número entero
numero = input("Introduce un número entero: ")

# Calculamos la suma de los dígitos del número
suma_digitos = sum(int(digito) for digito in numero)

# Mostramos el resultado detallado
detalle = " + ".join(numero)
print(f"La suma de los dígitos es: {detalle} = {suma_digitos}")
