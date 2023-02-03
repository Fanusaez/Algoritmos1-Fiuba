#Escribir una función que reciba las coordenadas de dos vectores en R3 y devuelva las
#coordenadas del producto vectorial,

def producto_vectorial(x1, y1, z1, x2, y2, z2):
    producto_i = (y1 * z2 - z1 * y2) 
    producto_j = (x2 * z1 - x1 * z2)
    producto_k = (x1 * y2 - y1 * x2)
    return producto_i, producto_j, producto_k

print(producto_vectorial(1, 3, 2, 4, 3, 4))