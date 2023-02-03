#Escribir una función que reciba una cadena de unos y ceros (es decir, un número
#en representación binaria) y devuelva el valor decimal correspondiente.

def convertir_a_decimal(binario):

    """
    """
    bits = list(binario)
    valor = 0
    for i in range(len(bits)):
        bit = bits.pop()
        if bit == '1':
            valor += 2 **i
    return valor


print(convertir_a_decimal("1010"))

