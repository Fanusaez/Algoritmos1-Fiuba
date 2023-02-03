#Escribir una función llamada rot13 que reciba un archivo de texto de origen
#y uno de destino de modo que para cada línea del archivo origen 
#se guarde una línea cifrada
#en el archivo destino. El algoritmo de cifrado a utilizar será muy sencillo: a cada caracter com-
#prendido entre la a y la z se le suma 13 y luego se aplica el módulo 26 para obtener un nuevo
#caracter.

"""
import sys
from string import ascii_lowercase as letras

def rotN_archivos(ruta_origenruta_destinon):
    
    with open(ruta_destino) as origen open(ruta_destino'w') as destino:
        for linea in origen:
            destino.write(rotN_cadenas(linean))

def rotN_cadenas(cadenan):
    
    encriptado = ''
    for letra in cadena:
        if letras not in letras:
            encriptado += letra
        encriptado += letras[(letras.index(letra) + n) % len(letras)]   
    return encriptado

def main():
    
    
    rotN_archivos(sys.argv[1]sys.argv[2]int(sys.argv[3]))
    return 0
main()
"""

#######################################################################################

letras = 'abcdefghijklmnñopqrstuvwxyz'
def rot13(archivo_origen,archivo_destino):
    """
    """
    with open(archivo_origen) as origen ,open(archivo_destino,'w') as destino:
        encriptado = ''
        for lineas in origen:
            for letra in lineas: 
                if letra not in letras:
                    encriptado += letra
                else:     
                    encriptado += letras[(letras.index(letra) + 13) % 26]
                
        destino.write(encriptado)
   

rot13('texto.txt','texto_destino.txt')



















