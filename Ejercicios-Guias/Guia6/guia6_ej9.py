

def pedir_entero(mensaje, min, max):
    """
    """

    numero = int(input('cual es tu numero favorito?: '))
    try: 
        int(numero)
        return True    
    except ValueError:
        return False

    if min <= numero <= max: 
        return numero
    while  numero >= max or numero <= min:
        numero = int(input(mensaje))
    return numero


#mensaje = 'por favor ingrese un numero entre "{}" y "{}"'. format(min, max)
z = print(pedir_entero('por favor ingrese un numero entre [-50, 50]: ', -50, 50))


#no me salio