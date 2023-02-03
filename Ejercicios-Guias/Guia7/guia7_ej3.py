# a) Escribir una función que reciba una tupla con nombres, y para cada nombre imprima
#el mensaje Estimado <nombre>, vote por mí.
# b) Escribir una función que reciba una tupla con nombres, una posición de origen p y una
#cantidad n, e imprima el mensaje anterior para los n nombres que se encuentran a partir
#de la posición p.
# c) Modificar las funciones anteriores para que tengan en cuenta el género del destinatario,
#para ello, deberán recibir una tupla de tuplas, conteniendo el nombre y el género.


def redacta_nota(nombre):
    """
    Esta funcion recinbe una tupla con nombres e imprime un mensaje con el 
    nombre de cada uno
    """
    for i in range(len(nombre)):
        print(f'Estimado {nombre[i]} ,vote por mi')

#redacta_nota(('francico', 'rodri', 'fanu', 'giova', 'mauri', 'fer'))

def imprimir_mensajes(nombres,p,n):
    """
    imprime mensaje a partir de la posicion 'p' que se le asigne
    """

    for i in range(0,n):
        
        
        if p > len(nombres):
            return
        if i >= p:
            print(f'Estimado {nombres[i]}, vote por mi.')
    
        
imprimir_mensajes(('barbara', 'fer',  , 'coco'), 3, 4)




