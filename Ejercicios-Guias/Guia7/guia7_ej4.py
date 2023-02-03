# a) Escribir una función que reciba dos vectores y devuelva su producto escalar.
# b) Escribir una función que reciba dos vectores y devuelva si son o no ortogonales.
# c) Escribir una función que reciba dos vectores y devuelva si son paralelos o no.
# d) Escribir una función que reciba un vector y devuelva su norma.

def multiplica_vectores(vec1, vec2):
    """
    """
    answer = 0
    x = 0
    for n in vec1:
        answer += n * vec2[x]
        x += 1
    return answer

#print(multiplica_vectores((1,4,2,1), (2,2,3,1)))

def decide_ortogonalidad(vector1,vector2):
    """
    """
    answer = multiplica_vectores(vector1,vector2)
    if answer == 0:
        return True
    else:
        return False

#print(decide_ortogonalidad((2, 3, 6), (-4, 5, -1)))


def norma_vector(vector):
    """ 
    """
    rta = 0
    for n in vector:
        rta += n ** 2
    return (rta) ** 0.5



