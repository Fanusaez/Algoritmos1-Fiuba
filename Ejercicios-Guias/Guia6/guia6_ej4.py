#Escribir una función que reciba una numero que contiene un largo número en-
#tero y devuelva una numero con el número y las separaciones de miles. Por ejemplo, si recibe
#'1234567890', debe devolver '1.234.567.890'.

def separar_en_miles(numero):

    """
    """
    frecuencia = 3
    caracter = '.'
    cifra = ''
    contador = 0
    for numero in numero[:: -1]:
        if contador == frecuencia:
            cifra += caracter
            contador = 0
        contador += 1
        cifra += numero 
    
    return (cifra[::-1])

print(separar_en_miles('1223243534653'))

#otra solucion

def sep_miles(numero):
    """
    """
    nuevo_numero = ""
    numero = numero[::-1]
    for i in range(len(numero)):
        if i != 0 and i % 3 == 0:
            nuevo_numero +=  '.' + numero[i] 
        else:
            nuevo_numero += numero[i]

    return (nuevo_numero[::-1])
print(sep_miles('34352535353'))











