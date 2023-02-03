#Escribir una función que reciba dos números como parámetros, y devuelva cuán-
#tos múltiplos del primero hay, que sean menores que el segundo.

# a) Implementarla utilizando un ciclo for, desde el primer número hasta el segundo.
# b) Implementarla utilizando un ciclo while, que multiplique el primer número hasta que
#sea mayor que el segundo.



def multiplos(a,b):
    """
    """
    cant_multi = 0
    for i in range(a, b):
        if i % a == 0 and i < b:
            cant_multi += 1
    return cant_multi

print(multiplos(3,1300))


def multiplos_2(a,b):
    """
    """ 
   
    cant_numeros = 0
    c = a
    while b > c: 
        if c % a == 0:
            cant_numeros += 1
        c += 1

    return cant_numeros

print(multiplos_2(3, 1300))

