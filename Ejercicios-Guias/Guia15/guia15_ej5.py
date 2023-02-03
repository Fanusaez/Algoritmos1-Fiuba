"""
Escribir dos funciones mutualmente recursivas par(n) e impar(n) que deter-
minen la paridad del numero natural dado, conociendo solo que:

• 1 es impar.
• Si un número es impar, su antecesor es par; y viceversa.
"""

def par(n):
    if n == 1:
        return False   
    if impar(n-1):
        return True
    return False


def impar(n):
    if n == 1:
        return True
    elif par(n-1):
        return True
    return False

print(par(6))
print(par(5))
print(impar(7))
print(impar(6))
