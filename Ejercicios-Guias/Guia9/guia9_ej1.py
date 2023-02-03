#Escribir una función que reciba una lista de tuplas, y que devuelva un diccionario
#en donde las claves sean los primeros elementos de las tuplas, y los valores una lista con los
#segundos.

def tuplas_a_diccionarios(lista):
    """
    recibe una lista y devuelve un diccionario 
    """
    diccionario = {}
    for x, y in lista:
        diccionario.setdefault(x, []).append(y)
    return diccionario


print(tuplas_a_diccionarios([ ('Hola', 'don Pepito'), ('Hola', 'don Jose'),
('Buenos', 'días') ])) 