#Escribir funciones que resuelvan los siguientes problemas:
#a) Dados dos números, imprimir la suma, resta, división y multiplicación de ambos.

n1 = int(input('enter a number: '))
n2 = int(input('enter a second number: '))

def operaciones_varias(n1, n2):

    suma = n1 + n2
    resta = n1 - n2
    mult = n1 * n2
    div = n1 % n2

    return suma, resta, mult, div

print(operaciones_varias(n1, n2))
 

