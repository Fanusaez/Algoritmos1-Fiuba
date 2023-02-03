#Dada una lista de números enteros, escribir una función que:
# a) Devuelva una lista con todos los que sean primos
# b) Devuelva la sumatoria y el promedio de los valores.
# c) Devuelva una lista con el factorial de cada uno de esos números.

def filtra_primos(numeros):
    """
    """
    p = []
    for num in numeros: 
        if num == 1:
            continue
        for i in range(2,num):
            if num % i == 0:
                break
        else:
            p.append(num)
    return p

#print(filtra_primos([1, 4 ,2, 7, 17, 89, 97, 83, 9]))   


def sumatoria(numeros):
    """
    """
    total = 0
    for num in numeros:
        if num < 0 or num > 10:
            break
        total += num
    promedio = total / len(numeros)
    return total, promedio
    

#print(sumatoria([10, 10, 10, 10, -1000,]))
#print(sumatoria([6, 9, 8, 7, 7, 7, 9, 4, 10, 9, 3]))

def devuelve_factoriales(enteros):
    """
    """
    factorial = []
    
    for num in enteros:
        mult = 1
        for i in range(1,num+1):
            mult *= i
        factorial.append(mult)
    return factorial
print(devuelve_factoriales([10, 15]))
print(devuelve_factoriales([1, 2, 3, 4, 5]))



