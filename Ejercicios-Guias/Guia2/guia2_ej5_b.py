#Escribir una función que dado un número entero devuelva 0 si el mismo es impar y 1 si
#fuera par.

numero = int(input('inserte numero: '))

def discriminar(numero):
    if numero % 2 != 0 :
        return 0
    if numero % 2 == 0 :
        return 1

print(discriminar(numero))


