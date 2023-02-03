#Escribir una función que dado un número entero devuelva 1 si el mismo
#es impar y 0 si fuera par.


numero = int(input('ingrese numero: '))

def main(numero):
    if numero % 2 == 0 : 
        return 0
    else :  
        return 1

print(main(numero))





