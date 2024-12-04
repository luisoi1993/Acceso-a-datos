"""2. Semi-triángulo de asteriscos: Crea un programa que dibuje un semi-triángulo de
asteriscos. El usuario debe ingresar la altura por teclado.
Un triángulo de asteriscos de altura 3 sería:

*
**
***
y de altura 5:
*
**
***
****
*****"""

numero_asteriscos = int(input("Digite el numero de asteriscos"))

asterisco = "*"
asteriscoTotal = ""

for i in range (1 , numero_asteriscos + 1):
    asteriscoTotal += asterisco
    print(asteriscoTotal)
    
