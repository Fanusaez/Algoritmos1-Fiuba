#Escribir una función empaquetar para una lista, donde empaquetar significa indicar
#la repetición de valores consecutivos mediante una tupla (valor, cantidad de repeticiones). Debe devolver una lista de tuplas.
#Ejemplo:
#>>>empaquetar([1, 1, 1, 3, 5, 1, 1, 3, 3])
#[(1, 3), (3, 1), (5, 1), (1, 2), (3, 2)]

def empaquetar2(lista):
    """
    """
    lista_nueva = []
    contador = 0
    n = 0
    for i in range(0, len(lista)):
        i+=contador
        lista_aux = []
        contador = 0
        while lista[i] == lista[i + n]:
            contador += 1
            n += 1
        lista_aux.append(lista[i])
        lista_aux.append(contador)    
        lista_nueva.append(tuple(lista_aux))
        n = 0

    return lista_nueva

print(empaquetar2([1, 1, 1, 3, 5, 1, 1, 3, 3]))