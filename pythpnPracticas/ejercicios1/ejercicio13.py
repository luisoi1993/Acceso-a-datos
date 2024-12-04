#6.13. Conversión de moneda: Escribe un programa que convierta una cantidad de
#dólares a euros. El tipo de cambio debe ser ingresado por el usuario.

dolares = float(input("Digite el total de dolares a convertir: "))
cambio = float(input("Digite el cambio a convertir: "))

resultado = dolares * cambio 

print(f"El resutado en euros es: {resultado}")

