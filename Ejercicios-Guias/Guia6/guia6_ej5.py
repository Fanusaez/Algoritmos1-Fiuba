#Escribir una función que dada una cadena de caracteres, devuelva:
# a) La primera letra de cada palabra. Por ejemplo, si recibe 'Universal Serial Bus' debe
#devolver 'USB'.
# b) Dicha cadena con la primera letra de cada palabra en mayúsculas. Por ejemplo, si recibe
#'república argentina' debe devolver 'República Argentina'.
# c) Las palabras que comiencen con la letra ‘A’. Por ejemplo, si recibe 'Antes de ayer'
#debe devolver 'Antes ayer'

def imprime_primera_letra(cadena):
    """
    """
    lista = cadena.split(' ')
    primera_letras = ""
    for palabra in lista:
        primera_letras += palabra[0]
    return primera_letras

#print(imprime_primera_letra('Universal Serial Bus'))


def imprime_mayusculas(cadena):
    """
    """
    nueva_cadena = cadena.title()
    return nueva_cadena

#print(imprime_mayusculas('republica argentina'))

def letra_con_a(cadena):

    """
    """
    lista = cadena.split(' ')
    nueva_cadena = " "
    for palabra in lista:
        if palabra[0] == ("a") or palabra[0] == ("A"):
            nueva_cadena += palabra + ' '
    return nueva_cadena

print(letra_con_a('hola aylen Argentina hoy'))
print(letra_con_a('Notienepalabrascondichaletra'))
print(letra_con_a('antesAyer'))






