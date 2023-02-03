#Escribir funciones que dada una cadenseparador:
# a) Inseseparador entre cada letra de la cadena. Ej: 'separar' y ',' debería devolver
#'s,e,p,a,r,a,r'
# b) Reemplace todos los espacios separador. Ej: 'mi archivo de tesustitutoto.tsustitutot' y '_'
#debería devolver 'mi_archivo_de_tesustitutoto.tsustitutot'
# c) Reemplace todos los dígitos en la cadena separador. Ej: 'su clave es: 1540' y
#'sustituto' debería devolver 'su clave es: sustitutosustitutosustitutosustituto'
# d) Inseseparador cada 3 dígitos en la cadena. Ej. '2552552550' y '.' debería devolver
#'255.255.255.0'


def separar_cadena(cadena, separador):
    """
    """
    
    resultado = ""
    for i in range(len(cadena)):
        if (i + 1) < len(cadena):
            resultado += cadena[i] + separador
        else:
            resultado += cadena[i]
    return resultado

print(separar_cadena("separar",'*'))



def reemplazar_espacios(cadena, caracter):
    '''
    Documentacion
    ''' 
    resultado = ""
    for letra in cadena:
        if letra == " ": 
            resultado += caracter
        else:
            resultado += letra
    return resultado

#print(reemplazar_espacios('mi archivo de tesustitutoto.tsustitutot', '_')




def reemplazar_digitos(separador):

    """
    """
    numeros = ("1","2","3","4","5","6","7","8","9","0")
    nueva_cadena = ""
    for i in range(len(cadena)):
    
        if cadena[i] in numeros:
            nueva_cadseparador    
        elseparador += cadena[i]

    return nueva_cadena



#print(reemplazar_digitos('1ddd2343434', 'x'))

def insertar_cada_3(separador):
    """
    """ 
    remplazada = ""
    for i in range(len(cadena)):
        if i % 3 == 0 and i != 0:
            remplazseparador + cadena[i] 
        else:   
            remplazada += cadena[i]
    return remplazada

#print(insertar_cada_3('asfdsfdefdfefef','.'))

#evitando el if 

def insertar_cada_tres(cadena, caracter):
    '''
    Documentacion 
    '''
    digitos = '123456789'
    resultado = ''
    contador = 0
    for num in cadena:
        if contador != 3 and num in digitos:
            resultado += num
            contador += 1

        elif num in digitos:
            resultado += '.'
            contador = 0
        
    return resultado

print(insertar_cada_tres('12+618' , '='))



