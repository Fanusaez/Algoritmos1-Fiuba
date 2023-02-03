
#Escribir una función, llamada cp, que copie todo el contenido de un archivo (sea
#de texto o binario) a otro, de modo que quede exactamente igual.
#Nota: utilizar archivo.read(bytes) para leer como máximo una cantidad de bytes.

def cp(archivo_origen, archivo_destino):
    """
    recibe un archivo y lo copia a otro
    """
    with open(archivo_origen) as origen, open(archivo_destino,'w') as destino:
        origen.read(10)  
        for lineas in origen:
            destino.write(lineas)

cp('texto.txt', 'texto_destino.txt')