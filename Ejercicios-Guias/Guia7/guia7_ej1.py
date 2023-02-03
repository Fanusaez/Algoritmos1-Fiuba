#Escribir una función que reciba una tupla de elementos e indique si se encuentran
#ordenados de menor a mayor o no.

def indica_menor_a_mayor(tupla):
    """
    """
    lista = list(tupla)
    if lista == sorted(tupla):
        return True
    else:
        return False


print(indica_menor_a_mayor((1,2,3,4)))
print(indica_menor_a_mayor((3,2,45)))
print(indica_menor_a_mayor(()))
print(indica_menor_a_mayor(('hola','aoo')))