#Utilizando las funciones anteriores, escribir una función que reciba las coordenadas de
#3 puntos en R3 y devuelva el área del triángulo que conforman.

from guia3_ej4_a import norma
from guia3_ej4_b import resta_de_coordenadas
from guia3_ej4_c import producto_vectorial


def area_triangulo(x1, y1, z1, x2, y2, z2, x3, y3, z3):
    vector_1_x, vector_1_y, vector_1_z = resta_de_coordenadas(x1, y1, z1, x2, y2, z2)
    vector_2_x, vector_2_y, vector_2_z = resta_de_coordenadas(x3, y3, z3, x2, y2, z2)
    producto_i, producto_j, producto_k = producto_vectorial(vector_1_x, vector_1_y, vector_1_z, vector_2_x, vector_2_y, vector_2_z)
    return norma(producto_i, producto_j, producto_k) * 0.5

print(area_triangulo(5, 8, -1, -2, 3, 4, -3, 3, 0))

