#Escribir una función que convierta un valor dado en grados Fahrenheit a grados
#Celsius. Recordar que la fórmula para la conversión es: 
#F = 9\5 C + 32

def convierto_unidades(fahrenheit): 
    grados = (fahrenheit - 32) * 5/9
    return grados

print(convierto_unidades(60))

