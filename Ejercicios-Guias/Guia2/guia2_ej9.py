#Escribir un programa que imprima por pantalla todas las fichas de dominó, de
#una por línea y sin repetir.

tamanio_domino = 10

def imprimir_fichas(n):
    for derecho in range(n):
        for izquierdo in range(derecho, n):
            print(izquierdo, derecho, sep = ' - ')

imprimir_fichas(tamanio_domino)


 


