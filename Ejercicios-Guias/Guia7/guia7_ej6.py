# Dada una lista de números enteros y un entero k, escribir una función que:
# a) Devuelva tres listas, una con los menores, otra con los mayores y otra con los iguales a k.
# b) Devuelva una lista con aquellos que son múltiplos de k.


def mayores_menosres_iguales_k(numeros, k):
    """
    """
    mayores = []
    menores = []
    iguales = []
    for num in numeros:
        if num > k:
            mayores.append(num)
        if num < k:
            menores.append(num)
        if num == k:
            iguales.append(num)
    return menores, mayores, iguales 

menores, mayores, iguales = mayores_menosres_iguales_k([1, 3, 2, 6, 7, 4, 3], 4)

print(menores)
print(mayores)
print(iguales)




def num_multiplos_de_k(enteros,k):
    """
    """
    multiplos = []
    for num in enteros:
        if num % k == 0:
            multiplos.append(num)
    return multiplos





