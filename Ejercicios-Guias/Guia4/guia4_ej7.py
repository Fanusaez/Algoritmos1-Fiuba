#Escribir un programa que reciba como entrada un entero representando un
#año (por ejemplo 751, 1999, o 2158), y muestre por pantalla el mismo año escrito en números
#romanos.

def conversion_entero_romano(entero):
    numeros = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    numerales = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']

    numeral = ''
    i = 0

    while entero > 0:
        for _ in range(entero // numeros[i]):
            numeral += numerales[i]
            entero -= numeros[i]
        i += 1
    return numeral  

print(conversion_entero_romano(100))
print(conversion_entero_romano(130))