#Escribir una función que reciba un número entero k e imprima su descomposición
#en factores primos.

def imprimir_descomposicion_primos(k):
    '''
    '''

    while k > 1:
        for i in range(2,k + 1):
            if k % i == 0:
                print(i,end="")
                if k != i:
                    print(' * ', end = '')
                k = k // i 
                break
        

imprimir_descomposicion_primos(20)
print()
imprimir_descomposicion_primos(155)
print()
imprimir_descomposicion_primos(5)
print()
