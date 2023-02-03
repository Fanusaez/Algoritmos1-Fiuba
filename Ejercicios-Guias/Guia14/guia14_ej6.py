#Escribir una función que recibe una expresión matemática (en forma de cadena)
#y devuelve True si los paréntesis ('()'), corchetes ('[]') y llaves ('{}') están correctamente
#balanceados, False en caso contrario. Ejemplos:

"""
Ejercicio 14.6. Escribir una función que recibe una expresión matemática (en forma de cadena)
y devuelve True si los paréntesis ('()'), corchetes ('[]') y llaves ('{}') están correctamente
balanceados, False en caso contrario. Ejemplos:
"""
from clases import *
def validar(ecuacion):
    desapilan = {")":"(","]":"[","}":"{","?":"¿"}
    apilan = set(desapilan.values())
    print(apilan)
    pila = Pila()
    for carac in ecuacion:

        if pila.esta_vacia() and carac in desapilan:
            return False

        elif carac in apilan:
            pila.apilar(carac)
        
        if carac in desapilan and desapilan[carac] != pila.desapilar():
            return False

    return pila.esta_vacia()

print(validar('¿x+y? / 8'))
print(validar('[8*4(x+y)]+{2/5}'))
print(validar('(x+y]/2'))
print(validar('([1+)2](+3)'))
