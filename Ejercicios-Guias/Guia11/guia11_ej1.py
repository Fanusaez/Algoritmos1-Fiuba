#Escribir una función, llamada head que reciba un archivo y un número N e im-
#prima las primeras N líneas del archivo.

def head(archivo,n):
    """
    recibe un archivo e imprime las primeras n lineas
    """
    with open(archivo) as f: #si voy a read no hace falta el 'r'
        contador = 0
        for linea in f:
            print(linea, end='')
            contador += 1
            if contador >= n:
                break

head('texto.txt', 9)
