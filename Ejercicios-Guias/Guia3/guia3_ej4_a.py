#Escribir una función que reciba las coordenadas de un vector en R3
#(x,y,z) y devuelva la norma del vecto

def norma(x, y, z):
    norma = ((x ** 2 + y ** 2 + z ** 2) ** 0.5)
    return norma

print(norma(5, 5, 5))

