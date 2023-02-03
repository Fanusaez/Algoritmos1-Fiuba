
from guia2_ej1 import calcular_ganancia

#Utilizando la función del ejercicio anterior, escribir un programa que le pregunte
#al usuario la cantidad de pesos inicial, la tasa de interés y el número de años y muestre el monto
#final a obtener.

def main():
    pesos = int(input('ingresar pesos iniciales: '))
    tasa_interes = int(input('ingresar tasa interes: '))
    anios = int(input('ingresar anos que dejara en el banco: '))
    return calcular_ganancia(pesos, tasa_interes, anios)

print(main())

