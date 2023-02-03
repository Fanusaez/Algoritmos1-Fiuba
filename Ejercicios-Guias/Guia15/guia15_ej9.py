"""
Escribir una función recursiva para replicar los elementos de una lista una can-
tidad n de veces. Por ejemplo:
"""

def replicar(arr, n):
    '''
    DOC: Completar
    '''
    if len(arr) == 0:
        return arr
    return replicar(arr[:-1],n) + [arr[-1]] * (n)

print(replicar([1,2,3], 2))