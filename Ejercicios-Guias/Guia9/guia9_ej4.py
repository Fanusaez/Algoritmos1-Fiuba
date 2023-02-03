#Escribir una función que reciba un texto y para cada caracter presente en el texto
#devuelva la cadena más larga en la que se encuentra ese caracter.

def obtener_cadenas_largas_por_caracter(texto):
    """
    Obtiene una cadena y le asigna a cada caracter la palabra mas larga
    en la cual se encuentran
    """
    diccionario = {}
    lista_aux = texto.lower().split()
    for i in range(len(lista_aux)):
        for j in range(len(lista_aux[i])):
            if lista_aux[i][j] not in diccionario:
                diccionario[lista_aux[i][j]] = lista_aux[i]
            elif len(diccionario[lista_aux[i][j]]) < len(lista_aux[i]):
                diccionario[lista_aux[i][j]] = lista_aux[i]
    return diccionario

print(obtener_cadenas_largas_por_caracter('Pero que hermoso dia hay'))
    


