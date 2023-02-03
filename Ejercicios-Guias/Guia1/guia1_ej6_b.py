#Dado un número entero n, imprimir su tabla de multiplicar.
n = int(input('ingresar numero que desea: '))

if n > 0: 

    for i in range (1, 11):

        print(n, 'por', i, 'es igual a', n * i)

else:
    print('el numero no es corrrecto, ingrese nuevamente')
