# a) Escribir una función que devuelva la suma de todos los divisores de un número n, sin
#incluirlo.
# b) Usando la función anterior, escribir una función que imprima los primeros m números
#tales que la suma de sus divisores sea igual a sí mismo (es decir los primeros m números
#perfectos).
# c) Usando la primera función, escribir una función que imprima las primeras m parejas
#de números (a, b), tales que la suma de los divisores de a es igual a b y la suma de los
#divisores de b es igual a a (es decir las primeras m parejas de números amigos).

# d) Proponer optimizaciones a las funciones anteriores para disminuir el tiempo de ejecu-
#ción.

def suma_divisores(n):
    """
    """
    suma = 0
    for i in range(1,n):
        if n % i == 0:
            suma += i
    return suma

#print(suma_divisores(80))
#print(suma_divisores(104))

def numeros_perfectos(m):
    """
    """
    cant_perfectos = 0

    for i in range(1,1000000):
        s = suma_divisores(i)
        if s == i:
            cant_perfectos += 1
            print(i)
        if cant_perfectos == m:
            break
       
#numeros_perfectos(3)


def numeros_amigos(m):

    """
    """
    parejas_primas = 0
    for i in range(1,100000):
        a = suma_divisores(i)
        for x in range(1,10000):
            b = suma_divisores(x)
            if a == x and b == i and a < b:
                print(i,x)
                parejas_primas += 1
            if parejas_primas == m:
                break
numeros_amigos(2)


#no me salio