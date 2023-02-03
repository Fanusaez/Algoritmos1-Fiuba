#Las raíces (reales o complejas) de un polinomio de segundo grado.
#Nota: validar que las operaciones puedan efectuarse antes de realizarlas (no dividir por
#cero, ni calcular la raíz de un número negativo).\
a = 0
b = 0
c = 0

def valores(a,b,c):
    a = int(input("ingrese valor de a distinto de cero: "))
    while a == 0:
         a = int(input("ingrese valor de a distinto de cero: "))
    b = int(input("ingrese valor de b: "))
    c = int(input("ingrese valor de c: "))
    return a, b, c

a, b, c = valores(a, b, c)

def raices(a, b, c):   
    x1 = (- b *(b**2 - 4 * a * c) ** 0.5 ) / 2 * a
    x2 = (- b * -(b**2 - 4 * a * c) ** 0.5 ) / 2 * a
    return 'primera raiz:', x1, 'la segunda raiz:', x2

print(raices(a, b, c))

