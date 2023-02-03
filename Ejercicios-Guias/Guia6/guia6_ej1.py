#Escribir funciones que dada una cadena de caracteres:
# a) Imprima los dos primeros caracteres.
# b) Imprima los tres últimos caracteres.
# c) Imprima dicha cadena cada dos caracteres. Ej.: 'recta' debería imprimir 'rca'
# d) Dicha cadena en sentido inverso. Ej.: 'hola mundo!' debe imprimir '!odnum aloh'
# e) Imprima la cadena en un sentido y en sentido inverso. Ej: 'reflejo' imprime
#'reflejoojelfer'.


def imprimir_los_dos_primeros_caracteres(cadena):
    print(cadena[0:2])

#imprimir_los_dos_primeros_caracteres('hola')


def imprimir_los_ultimos_3(cadena):
    """
    """
    print(cadena[-3:])

#imprimir_los_ultimos_3('hola')
#imprimir_los_ultimos_3('hola como estas')


def imprimir_al_revez(cadena):
    """
    """
    print(cadena[::-1])

#imprimir_al_revez('hola man')
#imprimir_al_revez('hola como estas')

def imprimir_cada_dos(cadena):
    """
    """
    print(cadena[::2])


imprimir_cada_dos('holabebesita')




def en_un_sentido_y_otro(cadena):
    """
    """
    print(cadena[::], cadena[::-1], sep = "")

#en_un_sentido_y_otro('refejo')


