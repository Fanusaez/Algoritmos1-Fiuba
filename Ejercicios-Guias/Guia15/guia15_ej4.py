"""
Escribir una funcion recursiva que reciba como parámetros dos cadenas a y b, y
devuelva una lista con las posiciones en donde se encuentra b dentro de a.
Ejemplo:
posiciones_de("Un tete a tete con Tete", "te") -> [3, 5, 10, 12, 21]
"""

def posiciones_de(a, b):
    posiciones = [] 
    contador = 0
    return _posiciones_de(a,b,posiciones,contador)

def _posiciones_de(a, b, posiciones,contador):
    if len(a) < len(b):
        return posiciones.append(contador)

    if a[0:2] == b: #and (a[1] and a[0] != " "):
        contador+=1
        posiciones.append(contador)
        _posiciones_de(a[2:0],b , posiciones, contador)

    if a[0] or a[1] == " ":   
        contador += 1
        _posiciones_de(a[1:0], b, posiciones, contador)

    else:
        contador += 1
        _posiciones_de(a[2:0], b, posiciones, contador)
    
print(posiciones_de("Un tete a tete con Tete", "te"))




