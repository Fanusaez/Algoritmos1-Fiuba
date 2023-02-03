#Escribir una función que reciba un dígito y un número natural, y decida numé-
#ricamente si el dígito se encuentra en la notación decimal del segundo.

def digitos():
    """
    """
    d = int(input('ingresa un solo digito: '))
    n = int(input('ingresa un numero natural: '))

    if str(d) in str(n):
        return True
    else:
        return False
    
print(digitos())
