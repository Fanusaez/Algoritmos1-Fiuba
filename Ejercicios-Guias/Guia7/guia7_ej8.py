#Escribir una función que reciba una lista de tuplas (Apellido, Nombre,
#Inicial_segundo_nombre) y devuelva una lista de cadenas donde cada una contenga primero el
#nombre, luego la inicial con un punto, y luego el apellido.


def nombre_completo(lista):
    """
    """
    lista_1 = []
    for i in range(len(lista)):
        for j in range(0,3):
            lista_1.append(lista[i][j])
    lista_1.insert(0,lista_1.pop(1))
    lista_1.insert(1,lista_1.pop(2))
    lista_2 = " ".join(lista_1)
    print(lista_2)
        
nombre_completo([('Turing', 'Alan', 'M')])


#Realizar una función que invierta una lista, pero en lugar de devolver una nueva, #modifique la lista dada, sin usar listas auxiliares.
#Ejemplo:
#>>>lista = ['Di', 'buen', 'dia', 'a', 'papa']
#>>>invertir_lista(lista)
#>>>lista
#['papa', 'a', 'dia', 'buen', 'Di']

def invertir_lista(lista):
    """
    """
    lista = list(reversed(lista))
    return lista

print(invertir_lista(['Di', 'buen', 'dia', 'a', 'papa']))

#o de otra forma, no s eporque no me acepta el campus

def invertir_lista(lista):
    '''
    Documentacion
    '''
    lista_1 = []
    for i in range(len(lista) - 1, -1, -1):
            lista_1.append(lista[i])
    return lista_1

print(invertir_lista(['Di', 'buen', 'dia', 'a', 'papa']))