#Escribir funciones que dadas dos cadenas de caracteres:
# a) Indique si la segunda cadena es una subcadena de la primera. Por ejemplo, 'cadena'
#es una subcadena de 'subcadena'.
# b) Devuelva la que sea anterior en orden alfábetico. Por ejemplo, si recibe 'kde' y 'gnome'
#debe devolver 'gnome'.


def indentifica_subconjunto(cadena, subcadena):
    """
    """ 
    if cadena.endswith(subcadena):
        return True
    else:
        return False
    
#print(indentifica_subconjunto('subcadena', 'caddsdsena'))

#print(indentifica_subconjunto('subcadena', 'cadena'))


def orden_alfabetico(cadena1, cadena2):
    """
    """
    lista = [cadena1, cadena2]

    return min(lista)

orden_alfabetico('hola', 'b')

