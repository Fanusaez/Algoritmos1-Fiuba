#Utilizando la función randrange del módulo random, escribir un programa que
#obtenga un número aleatorio secreto, y luego permita al usuario ingresar números y le indique
#si son menores o mayores que el número a adivinar, hasta que el usuario ingrese el número
#correcto.

import random

def guess_number():
    """
    """
    n = random.randrange(0,20)
    number = ''
    while number != n:
        number = int(input('write a number: '))
        if n < number:
            print('your number is grater than the one you seek')
            
        if n > number:
            print('your number is smaller than theone you seek')
            
        if n == number:
            print('correct!')

guess_number()

    
