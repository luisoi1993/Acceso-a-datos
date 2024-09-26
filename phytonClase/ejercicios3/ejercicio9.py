#9Para terminar, volvemos al ejercicio número 1, pero esta vez sin librería que nos lo
#facilite.

def es_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True

for num in range(1, 51):
    if es_primo(num):
        print(num)
