#10. Crea un programa que cuente cuántas veces aparece una letra específica en
#una cadena de texto ingresada por el usuario.


entrada = str(input("Digite la cadena de texto: ")) # Cadena donde se busca la letra
cuentalaletra = str("e") # La letra que queremos contar
contador = int(0) # Inicializamos el contador
for letra in entrada:
    if letra == cuentalaletra:
        contador += 1 # Sumamos uno al contador si la letra coincide
print(cuentalaletra, ":", contador) # Imprimimos el resultado final
