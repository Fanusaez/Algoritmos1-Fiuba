#Escribir una función que reciba por parámetro una dimensión n, e imprima la
#matriz identidad correspondiente a esa dimensión.
def matriz(fila,columna):
    for c in range(columna):
        for f in range(fila):
            if f == c: 
                print(1, end='')
            else: 
                print(0, end='')
        print()

matriz(3,3)
 
    