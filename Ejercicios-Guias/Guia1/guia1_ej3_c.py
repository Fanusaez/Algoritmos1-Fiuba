#Calcular el área de un rectángulo (alineado con los ejes x e y) dadas sus coordenadas
#x1, x2, y1, y2.

x1 = int(input('primer coordenada en i: '))
y1 = int(input('primera coordenada en j: '))
x2 = int(input('segunda coordenada en i: '))
y2 = int(input('segunda coordenada en j: '))

def diferencia(x1, y1, x2, y2):

#"""Recibe las coordenadas de dos vectores en R3 y devuelve su diferencia"""

    base = x1 - x2
    altura = y1 - y2

    return (base * altura) * 0.5

print(diferencia(x1, y1, x2, y2))






