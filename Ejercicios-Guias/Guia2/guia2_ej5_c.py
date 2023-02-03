#Escribir una función que dado un número entero devuelva el dígito de las unidades. Por
#ejemplo, para 153 debe devolver 3.

number = int(input('ingrese numero: '))

def devolver_ult(number):
    if (number >= 1000): 
        return 'the last digit of the number is: ' + str(((number % 1000) % 100) % 10)

    elif (number >= 100):
        return 'the last digit of the number is: ' + str((number % 100) % 10 )

    elif (number >= 10):
        return ' the last digit of your number is: ' + str(number % 10)

    else:
        return number


print(devolver_ult(number))




