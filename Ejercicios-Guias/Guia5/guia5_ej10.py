#Escribir una función que reciba un número natural e imprima todos los números
#primos que hay hasta ese número.




    
def imprime_primos():
    """
    """

    n = int(input('ingrese un numero:'))

    while n <= 1:
        print('numero debe ser mayor a uno')
        n = int(input('ingrese un numero:'))

    for i in range (2,n):
        creciente = 2
        es_primo = True

        while es_primo and creciente < i:

            if i % creciente == 0:
                es_primo = False
            else:
                creciente +=1

        if es_primo:
            print(i, 'es numero primo')
                
imprime_primos()
