
#Escribir una función recursiva que reciba un número positivo n y devuelva la
#cantidad de dígitos que tiene.


def contar_digitos(n):
    """ recibe un numero y cuenta los digitos"""
   
    if n // 10 == 0:
        return 1
    else:
        return 1 + contar_digitos(n // 10)

print(contar_digitos(223322))