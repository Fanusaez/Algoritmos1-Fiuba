"""
Escribir una funcion recursiva que dada una cadena determine si en la misma
hay más letras A o letras E.
"""

def hay_mas_a_que_e(cadena):
    a = 0
    e = 0
    return _hay_mas_a_que_e(a, e, cadena)

def _hay_mas_a_que_e(a, e, cadena):
    if not len(cadena): return a > e
    if cadena[0] == 'a': a += 1
    if cadena[0] == 'e': e += 1
    return _hay_mas_a_que_e(a,e, cadena[1:])

