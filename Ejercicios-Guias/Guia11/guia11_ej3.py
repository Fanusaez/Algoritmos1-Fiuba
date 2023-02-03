#Escribir una función, llamada wc, que dado un archivo de texto, lo procese e
#imprima por pantalla cuántas líneas, cuantas palabras y cuántos caracteres contiene el archivo.

def wc(archivo_de_texto):
    """
    recibe archivo y cuenta saltos de lineas, palabras y caracteres 
    contiene el archivo
    """
    with open(archivo_de_texto) as f:
        lineas = f.readlines()
        print(f'Cantidad de lineas: {len(lineas)}')

        palabras_str = ""
        for palabras in lineas:
            palabras_str += palabras
            lista_palabras = palabras_str.split()
        print(f'Cantidad de palabras: {len(lista_palabras)}')

        palabras_str = ""
        for palabras in lineas:
            palabras_str += palabras   
            lista_palabras = palabras_str.split()
            palabras_str_nospace = "".join(lista_palabras)
        print(f"Cantidad de caracteres: {len(palabras_str_nospace)}")
        

wc('texto.txt')
