n1 = int(input('enter a number: '))
n2 = int(input('enter a second number: '))

def suma(n1, n2):
    suma = n1 + n2
    return suma

print('la suma de los dos numeros es', suma(n1, n2))

def resta(n1, n2):
    resta = n1 - n2
    return resta

print('la resta de los dos numeros es', resta(n1, n2))

def mult(n1, n2):
    mult = n1 * n2
    return mult

print('la multiplicacion de estos numeros es', mult(n1, n2))

def div(n1, n2):
    div = n1 / n2
    return div

print('la division de esos numeros es', div(n1, n2))
