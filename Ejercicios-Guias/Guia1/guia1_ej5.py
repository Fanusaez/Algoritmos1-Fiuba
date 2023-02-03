#Escribir una función que, dado un número entero n, permita calcular su factorial.

n = int(input('ingrese un numero entero: '))
result = 1

for i in range(n, 0, -1):
    result = result * i

print('factorial de', n, 'is' , result)

