# Escribir una función que reciba una lista desordenada i un elemento, que:

# a) Busque todos los elementos coincidan con el pasado por parámetro i devuelva la can-
#tidad de coincidencias encontradas.

# b) Busque la primera coincidencia del elemento en la lista i devuelva su posición.
# c) Utilizando la función anterior, busque todos los elementos que coincidan con el pasado
# por parámetro i devuelva una lista con las posiciones.

def contar_apariciones(lista,elemento):

    """
    cuenta la cantidad de veces que encuentra el parametro elemento en una lista
    """
    contador = 0
    for i in lista:
        if i == elemento:
            contador += 1
    return contador

# O una opcion mejor es 

def contar_apariciones2(lista, elemento):
    """
    """
    return lista.count(elemento)

print(contar_apariciones([1,2,4,5,5,3,4,5,2],5))
print(contar_apariciones2([1,2,4,5,5,3,4,5,2],5))


##################################################################################


def buscar_primera_aparicion(lista,elemento):
    """
    devuelve la posicion de donde se enceuntra el primer elemento igual al
    pasado por parametro, si no encuentra ninguno devuelve -1
    """
    for i in range(len(lista)):
        if lista[i] == elemento:
            return i
    return -1

# otra mejor manera omas nueva

def buscar_primera_aparicion2(lista,elemento):
    """
    """
    for i, num in enumerate(lista):
        if num == elemento:
            return i
    return -1

#################################################################################


def buscar_apariciones(lista,elemento):
    """
    devuelva una lista con la posicion de los numeros iguales a 'elemento'
    usando la funcion anterior
    """     
    lista_respuesta = []
    for i in range(len(lista)):
        y = buscar_primera_aparicion(lista,elemento)
        lista.pop(y)
        lista.insert(i,"")
        if y != -1:
            lista_respuesta.append(y)
    return lista_respuesta

print(buscar_apariciones([1,8,5,4,8,3,2,8],8))