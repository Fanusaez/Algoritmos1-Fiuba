#Escribir una función que reciba una lista de números no ordenada, que:
# a) Devuelva el valor máximo.
# b) Devuelva una tupla que incluya el valor máximo y su posición.
# c) ¿Qué sucede si los elementos son cadenas de caracteres?

def maximo(numeros):
    """
    devuelve el valor maximo de una lista
    """
    max = 0
    if numeros == []:
        max = None
        return max
    for i in numeros:
        if i > max:
            max = i
    return max

print(maximo([101,1,5,3,2,5,6,8,100]))
print(maximo([]))


###############################################################################


def maximo_y_posicion(numeros):
    """
    de una lista de numeros devuelve el valor maximo y su posicion
    """
    max = 0
    if numeros == []:
        lista_respuesta = []
        lista_respuesta.append(None)
        lista_respuesta.append(-1)
        return tuple(lista_respuesta)
    for _, num in enumerate(numeros):
        lista_respuesta = []
        if num > max:
            max = num
    lista_respuesta.append(max)
    lista_respuesta.append(numeros.index(max))
    return tuple(lista_respuesta)
        
print(maximo_y_posicion([99,1,4,5,3,5,6,9]))
print(maximo_y_posicion([]))


# otra manera MUCHO MEJOR de hacer la segunda parte

def maximo_y_posicion2(numeros):

    for i, num in enumerate(numeros):
        if num == maximo(numeros):
            return num, i
    return None , -1

print(maximo_y_posicion2([99,1,4,5,3,5,6,9]))
print(maximo_y_posicion2([]))

