#Dado un número entero n, indicar si es par o no

def numero_par(n):
    if (n % 2 == 0):
        return 'este numero es par'
    else:   
        return 'este numero no es par'

    return 

print(numero_par(7))

def numero_primo(num):
    if num < 1:
        return 'number must be greater than 1'
    elif  num == 2:
        return 'this number is prime'
    else:
        for i in range(2, num):
            if num % i == 0:
                return ' this number is not prime'
        return 'this number is prime'

#print(numero_primo(-4))

def damos_numero():
    num = int(input('insert a number: '))
    return numero_primo(num)

print(damos_numero())

