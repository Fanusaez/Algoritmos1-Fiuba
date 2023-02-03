# a) Escribir una función es_potencia_de_dos que reciba como parámetro un número na-
#tural, y devuelva True si el número es una potencia de 2, y False en caso contrario.

# b) Escribir una función que, dados dos números naturales pasados como parámetros,
#devuelva la suma de todas las potencias de 2 que hay en el rango formado por
#esos números (0 si no hay ninguna potencia de 2 entre los dos). Utilizar la función
#es_potencia_de_dos, descripta en el punto anterior.

def es_potencia_de_dos(n):
    while n > 1 and n % 2 == 0:
        n = n / 2
    return n == 1
    
#print(es_potencia_de_dos(9))
#print(es_potencia_de_dos(8))
#print(es_potencia_de_dos(2))    


def funcion(n1, n2):
    suma = 0
    for i in range(n1, n2 + 1):
        if es_potencia_de_dos(i):
            
            suma = suma + i
    return suma

print(funcion(1, 8))

