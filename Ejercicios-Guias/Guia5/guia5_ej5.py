# a) Implementar el algoritmo de Euclides para calcular el máximo común divisor de dos
#números n y m, dado por los siguientes pasos.
#1. Teniendo n y m, se obtiene r, el resto de la división entera de m/n.
#2. Si r es cero, n es el mcd de los valores iniciales.
#3. Se reemplaza m ← n, n ← r, y se vuelve al primer paso.

# b) Hacer un seguimiento del algoritmo implementado para los siguientes pares de núme-
#ros: (15, 9); (9, 15); (10, 8); (12, 6).

def find_mcd(n,m):
    if m % n == 0:
        return n
    while m % n != 0:
        r = m % n
        m = n
        n = r 
    return r 
   
print(find_mcd(2, 2))
print(find_mcd(60, 48))