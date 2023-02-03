
#Escribir una función llamada tail que recibe un archivo y un número N e 
#imprime las últimas N líneas del archivo. Durante el transcurso de la 
#función no puede haber más de N líneas en memoria.


from clases import *

def tail(nombre_archivo, N):
    '''
    DOC: Completar
    '''
    cola = Cola()
    contador = 0
    with open(nombre_archivo) as archivo:
        for linea in archivo:
            if contador < N:
                cola.encolar(linea)
                contador += 1
            else:
                cola.desencolar()
                cola.encolar(linea)
        while not cola.esta_vacia():
            print(f"{cola.desencolar()}", end= "")


tail('lineas.txt', 4)