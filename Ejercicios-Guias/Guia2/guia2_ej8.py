#Escribir un programa que tome una cantidad m de valores ingresados por el usua-
#rio, a cada uno le calcule el factorial (utilizando la función escrita en el ejercicio 1.5) e imprima
#el resultado junto con el número de orden correspondiente.

def calcular_factoriales(numero): 
    factorial = 1
    for i in range(1, numero + 1):
        factorial = factorial * i 
    return factorial

def imprimir_factoriales(cantidad):
    for i in range(cantidad): 
        numero = int(input('ingrese el numero a calcular: '))
        print(calcular_factoriales(numero), i, sep= ' - ')

imprimir_factoriales(200)
