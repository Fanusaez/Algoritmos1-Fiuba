#Escribir una función que reciba dos matrices y devuelva la suma. 
#Las matrices están representadas como listas de listas.

def sumar_matrices(m1, m2):
    """
    """
    m3 = [] 
    for i in range(len(m1)):
        m3.append([])
        for j in range(len(m1[0])):
            m3[i].append(m1[i][j]+ m2[i][j])

    return m3
print(sumar_matrices([[2, 3], [1, 9]], [[5, 7], [2, 1]]))


# multiplicacion de matrices

def multiplicar_matrices(m1,m2):

    m3 = [] 
    for i in range(len(m1)):
        m3.append([])
        for j in range(len(m2[0])):
            m3[i].append(0)

    for i in range(len(m1)):
        for j in range(len(m2[0])):
            for k in range(len(m1[0])):
                m3[i][j] += m1[i][k] * m2[k][j]
    return m3

print(multiplicar_matrices([[2, 3], [1, 9]], [[5, 7], [2, 11]])) 