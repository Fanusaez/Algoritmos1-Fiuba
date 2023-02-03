from clases import *

def promedio_espera(eventos):
    '''
    DOC: Completar
    '''

    cola = Cola()
    sumatoria = 0
    personas = 0
    

    for tupla in eventos:
        if len(tupla) == 2:
            cola.encolar(tupla[0])
            personas += 1
        elif len(tupla) == 3:
            contador = tupla[2]
            while contador != 0 and not cola.esta_vacia():
                tiempo_persona = cola.desencolar()
                tiempo_subir = tupla[0] 
                sumatoria += (tiempo_subir - tiempo_persona)
                contador -= 1

    promedio  = sumatoria / personas
    return promedio

print(promedio_espera([(35,'p'), (43,'p'), (80,'c',1), (98,'p'), (142,'c',2)]))
