#Escribir un programa que imprima todos los números pares entre dos números
#que se le pidan al usuario.

def pedir_numeros():
    '''  pide dos numeros 
    '''
    primero = int(input('inserte numero: '))
    segundo = int(input('inserte otro numero: '))
    return primero, segundo

def imprimir_pares_rango(inicio, final):
    """ imprime numeros pares del rango indicado
    """
    for i in range(inicio + inicio%2, final, 2):
        print (i)

def main():
    """
    """
    inicio, final = pedir_numeros()
    imprimir_pares_rango(inicio, final) 

main()
    


