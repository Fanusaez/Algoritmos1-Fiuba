# Escribir una función que reciba las coordenadas de dos vectores en R3
# (x1,y1,z1,x2,#y2,z2) y devuelva las coordenadas 
# del vector diferencia (debe devolver 3 valores numé#ricos).

def resta_de_coordenadas(x1, y1, z1, x2, y2, z2):
    vector_x = x1 - x2
    vector_y = y1 - y2  
    vector_z = z1 - z2
    return vector_x, vector_y, vector_z

print(resta_de_coordenadas(1, 3, 4, 3, 4, 3))
    