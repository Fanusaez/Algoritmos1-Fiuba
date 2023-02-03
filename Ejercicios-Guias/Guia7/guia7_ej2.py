# a) Escribir una función que indique si dos fichas de dominó encajan o no. Las fichas son
#recibidas en dos tuplas, por ejemplo: (3,4) y (5,4)
# b) Escribir una función que indique si dos fichas de dominó encajan o no. Las fichas son
#recibidas en una cadena, por ejemplo: 3-4 2-5. Nota: utilizar la función split de las
#cadenas.

def verifica_encaje(tupla_1,tupla_2):
    """
    indican si dos fichas de domino encajan o no
    """
    if tupla_1[0] in tupla_2:
        return True 
    if tupla_1[1] in tupla_2:
        return True
    else: 
        return False


print(verifica_encaje((3,2),(4,3)))  
print(verifica_encaje((3,4),(5,7)))

#otra forma

def encajan(ficha1, ficha2):
    """
    indican si dos fichas de domino encajan o no
    """

    for i in range(len(ficha1)):
        if ficha1[i] == ficha2[0] or ficha1[i] == ficha2[1]: 
            return True
    return False

print(encajan((2,2),(3,5)))



def fichas_encajan(fichas):
    """
    indica si una ficha dadas en forma de cadena encajan
    """

    lista = fichas.split()
    
    for i in lista:
        if lista.index(i) == 2:    
            return True
    return False

lista = ('32 41')   
lista2 = lista.split("")
print(lista2)
#no pude, preguntar