# a) Escribir una función que reciba una cadena y devuelva un diccionario con la cantidad
#de apariciones de cada palabra en la cadena. Por ejemplo, si recibe ”Qué lindo día que
#hace hoy” debe devolver: { 'que': 2, 'lindo': 1, 'día': 1, 'hace': 1, 'hoy': 1}.


#Nota: utilizar el módulo random para obtener tiradas aleatorias.


def contar_palabras(cadena):
    """
    """

    replacements = ( # esto es la pedo pero queda
        ("á", "a"),
        ("é", "e"),
        ("í", "i"),
        ("ó", "o"),
        ("ú", "u"),
    )
    for a, b in replacements:
        cadena = cadena.replace(a,b)
        cadena = cadena.lower()
    diccionario = { }
    lista_de_cadenas = cadena.split()
    for i in range(len(lista_de_cadenas)):
        contador = 0
        for j in lista_de_cadenas:
            if lista_de_cadenas[i] == j:
                contador +=1    
        diccionario.setdefault(lista_de_cadenas[i],contador)
    return diccionario

# OTRA MANERA DE HACERLO

def contar_palabras_2(cadena):
    """
    """
    lista_cadena, diccionario  = cadena.lower.split(' '), dict()
    if cadena != " ":
        for palabra in lista_cadena:
            if palabra.lower() not in diccionario:
                diccionario[palabra] = 0
            diccionario[palabra] += 1
    return diccionario


################################################################

# b) Escribir una función que cuente la cantidad de apariciones de cada caracter en una ca-
#dena de texto, y los devuelva en un diccionario.

def contar_caracteres(cadena):
    """
    """
    cadena = cadena.lower( )
    cadena = cadena.replace(" ","")
    lista_aux = []
    
    diccionario = {}
    for i in range(len(cadena)):
        lista_aux.append(cadena[i])
    for i in range(len(lista_aux)):
        contador = 0
        for j in lista_aux:
            if lista_aux[i] == j:
                contador += 1
        diccionario.setdefault(lista_aux[i], contador)
    return diccionario

# OTRA MANERA DE HACERLO

def contar_caracteres_2(cadena):
    """
    """
    diccionario = {}
    cadena = cadena.replace(" ","").lower()
    if cadena != "":
        for letra in cadena:
            if letra not in diccionario:
                diccionario[letra] = 0
            diccionario[letra] += 1
    return diccionario

    
print(contar_caracteres_2('Qué lindo día que hace hoy'))
print(contar_caracteres('Qué lindo día que hace hoy'))

##############################################################################

# c) Escribir una función que reciba una cantidad de iteraciones de una tirada de 2 dados a
# realizar y devuelva la cantidad de veces que se observa cada valor de la suma de los dos
# dados.

import random


def contar_resultados_dados(n):

    """
    recibe una cantidad de veces que debo tirar un dado
    las tira e indica la cantidad de veces que salio cada
    numero
    """
    diccionario = {}
    for _ in range(n*2):
        c = random.randint(1,6)
        if c not in diccionario:
            diccionario[c] = 0
        diccionario[c] += 1
    return diccionario

print(contar_resultados_dados(2))


