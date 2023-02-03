"""
Escribir una función recursiva que reciba 2 enteros n y b y devuelva True si n es
potencia de b.
Ejemplos:
es_potencia(8, 2) -> True
es_potencia(64, 4) -> True
es_potencia(70, 10) -> False
"""

def es_potencia(n, b):
    
    if n == b:
        return True
    elif n > b:
        return es_potencia(n // b, b)
    else:
        return False

print(es_potencia(10, 3))
print(es_potencia(70, 10))
print(es_potencia(64, 4))
