#Escribir una función que reciba una lista ordenada y un elementoento. Si el elementoento
#se encuentra en la lista, debe encontrar su posición mediante búsqueda binaria y devolverlo. Si
#no se encuentra, debe agregarlo a la lista en la posición correcta y devolver esa nueva posición.
#(No utilizar lista.sort().)

def busqueda_binaria(lista,elemento):
    """
    """
    izq = 0
    der = len(lista) - 1
    while izq <= der:
        med = (izq + der) // 2
        if lista[med] == elemento:
            return med      
        if lista[med] < elemento:
            izq = med + 1
        else:
            der = med - 1
    lista.insert(izq,elemento)
    return izq

