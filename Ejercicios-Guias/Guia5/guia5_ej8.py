#Escribir un programa que le pida al usuario que ingrese una sucesión de números
#naturales (primero uno, luego otro, y así hasta que el usuario ingrese ’-1’ como condición de
#salida). Al final, el programa debe imprimir cuántos números fueron ingresados, la suma total
#de los valores y el promedio.

def imprimir_promediar_numeros(num):
    """
    """
    suma = 0
    num = 0
    total_num = 0
    while num != -1: 
        num = int(input('ingrese numero: '))
        if num != -1:
            suma += num
            total_num += 1  
        if num == -1:
            print('La suma de todos los numeros es:',suma)
            print('El total de numeros ingresados es:', total_num)
            print('El promedio de loa numeros ingresados es:', suma /total_num)
            break

imprimir_promediar_numeros('')