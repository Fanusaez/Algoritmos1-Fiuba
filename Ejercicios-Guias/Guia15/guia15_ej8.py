#Escribir una funcion recursiva que encuentre el mayor elemento de una lista.


def obtener_mayor_elemento(arr):
    '''
    DOC: Completar
    '''
    if len(arr) == 1:
        return arr[0]
    maximo = obtener_mayor_elemento(arr[1:])
    if maximo > arr[0]:
        return maximo
    else:
        return arr[0]
    


print(obtener_mayor_elemento([1,2,3,4,5,4,3,22]))