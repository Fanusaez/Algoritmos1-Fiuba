#Escribir una implementación propia de la función abs, que devuelva el valor ab-
#soluto de cualquier valor que reciba.

def absoluto(n):
    if n >= 0:
        return 'the absolute value is: ',n  
    else:  
        return 'the absolute value is: ', n * -1  

print(absoluto(5))
print (absoluto(-3))