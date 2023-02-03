#Escribir una función que, dados cuatro números, devuelva el mayor producto de
#dos de ellos. Por ejemplo, si recibe los números 1, 5, -2, -4 debe devolver 8, que es el producto
#más grande que se puede obtener entre ellos (8 = −2 × −4).

def mayor_par(a, b, c, d):

    if (a * b) > ((a * c) and (a * d) and (b * c) and (b * d) and (c * d)):
        return  (a * b)
    elif (a * c) > ((a * b) and (a * d) and (b * c) and (b * d) and (c * d)):
        return (a * c)
    elif (a * d) > ((a * b) and (b * c) and (b * d) and (c * d) and (a * c)):
        return (a * d)
    elif (b * c) > ((a * b) and (a * c) and (a * d) and (b * d) and (c * d)):
        return (b * c)
    elif (b * d) > ((a * b) and (a * c) and (a * d) and (b * c) and (c * d)):
        return (b * d)
    else: 
        return (c * d)


print(mayor_par(1, 1, 8, 3))

