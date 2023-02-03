#Escribir funciones que dada una cadena de caracteres:
# a) Devuelva solamente las letras consonantes. Por ejemplo, si recibe 'algoritmos' o
#'logaritmos' debe devolver 'lgrtms'.
#b) Devuelva solamente las letras vocales. Por ejemplo, si recibe 'sin consonantes' debe
#devolver 'i ooae'.
# c) Reemplace cada vocal por su siguiente vocal. Por ejemplo, si recibe 'vestuario' debe
#devolver 'vistaerou'.

# d) Indique si se trata de un palíndromo. Por ejemplo, 'anita lava la tina' es un pa-
#líndromo (se lee igual de izquierda a derecha que de derecha a izquierda).



def imprime_sin_consonantes(cadena):
    """
    """
    nueva_cadena = ""
    
    for letra in cadena:
        if letra not in ('a', 'e', 'i', 'o', 'u'):
            nueva_cadena += letra
    return nueva_cadena

#print(imprime_sin_consonantes('logaritmos'))



def imprime_consonantes(cadena):
    """
    """
    nueva_cadena = ""
    
    for letra in cadena:
        if letra  in ('a', 'e', 'i', 'o', 'u'," "):
            nueva_cadena += letra
    return nueva_cadena

#print(imprime_consonantes('sin consonantes'))


def intercambia_vocales(cadena):
    """
    """
    nueva_cadena = ''
    vocales = ['a', 'e', 'i', 'o', 'u']
    reemplazo = ['e', 'i', 'o', 'u', 'a']

    for letra in cadena:
        for i in range(0,5):
            if letra in vocales[i]:
                nueva_cadena += reemplazo[i]
                break
        else:
            nueva_cadena += letra
                
    return nueva_cadena


#print(intercambia_vocales('vestuario'))

def es_palindromo(cadena):
    """
    """
    cadena = cadena.lower() 
    cadena = cadena.replace(' ', '')
    longitud = len(cadena)
    if longitud % 2 == 0:
        izquierda = cadena[:longitud // 2]
        derecha = cadena[longitud//2 :]
        
    else:
        izquierda = cadena[:longitud // 2]
        derecha = cadena[longitud//2 + 1:]
    
    return derecha == izquierda[::-1] 


print(es_palindromo('anita lava la tina'))
print(es_palindromo('1001'))