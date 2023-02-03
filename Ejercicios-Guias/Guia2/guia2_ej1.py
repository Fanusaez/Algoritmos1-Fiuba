#Escribir una función que reciba una cantidad de pesos, una tasa de interés y un
#número de años y devuelva el monto final a obtener. La fórmula a utilizar es:
#Donde C es el capital inicial, x es la tasa de interés y n es el número de años a calcular.

def calcular_ganancia(pesos, tasa_interes, anios):
    ganancia = pesos * (1 + tasa_interes /100) ** anios
    return ganancia 






