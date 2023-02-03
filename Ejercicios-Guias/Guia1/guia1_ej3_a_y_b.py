#Calcular el area de un rectángulo dada su base y su altura

base = float(input('insert base length: '))
height = float(input('insert heigth: '))

def area_triangulo(base, height):

    #calcula area triangulo

    area = base * height
    return area

print(area_triangulo(base, height))
