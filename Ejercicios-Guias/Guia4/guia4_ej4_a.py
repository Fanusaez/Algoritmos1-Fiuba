#Escribir funciones que permitan encontrar:
# a) El máximo o mínimo de un polinomio de segundo grado 
#"dados los coeficientes a, b y c", indicando si es un máximo o un mínimo.

def max_y_min(a,b,c):
    x = - b / (2 * a)
    y = (4 * a * c - b**2) / (4 * a)
    if a > 0:
        print('el valor minimo es: ', x , y )
    else:
        print('el valor maximo es: ', x, y)

max_y_min(-1, -2, 3)


