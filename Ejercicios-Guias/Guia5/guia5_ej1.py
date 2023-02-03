#Escribir un programa que permita al usuario ingresar un conjunto de notas, pre-
#guntando a cada paso si desea ingresar más notas, e imprimiendo el promedio correspondiente.

def promedio():
    cant_notas = 0
    suma_notas = 0
    while True:
        
        nota = int(input('ingrese su nota: '))
        if not 0<= nota <= 10:
            continue
        cant_notas += 1
        suma_notas += nota  

        opc = input('desea ingresar mas notas ? [y/n]: ')
        if opc == 'n':
            break   
       
    print(suma_notas / cant_notas)

promedio()
