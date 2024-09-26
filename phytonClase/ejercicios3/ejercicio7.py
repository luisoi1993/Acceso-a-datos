#7. Implementa las siguientes puertas lógicas:
#AND, OR, NOT

def puerta_and(a, b):
    return a and b

def puerta_or(a, b):
    return a or b

def puerta_not(a):
    return not a

a = True
b = False

print("AND:", puerta_and(a, b))  # False
print("OR:", puerta_or(a, b))    # True
print("NOT A:", puerta_not(a))   # False
print("NOT B:", puerta_not(b))   # True
