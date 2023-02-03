#Escribir una función, llamada grep, que reciba una cadena y un archivo e imprima
#las líneas del archivo que contienen la cadena recibida.


def grep(cadena,archivo):
    """ Imprime la linea que contenga la cadena ingreasada"""
    
    with open(archivo) as f:
        lista_cadena = cadena.split()
        for linea in f:
            lista_linea = linea.split()
            contador = 0
            for i in range(len(lista_cadena)):
                if lista_cadena[i] in lista_linea:
                    contador += 1
            if contador == len(lista_cadena):
                print(linea, end="")
            
grep('hola como estas','texto.txt')


