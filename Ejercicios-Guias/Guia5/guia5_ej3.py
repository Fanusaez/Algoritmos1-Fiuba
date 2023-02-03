#Manejo de contraseñas

# a) Escribir un programa que contenga una contraseña inventada, que le pregunte al usua-
#rio la contraseña, y no le permita continuar hasta que la haya ingresado correctamente.

# b) Modificar el programa anterior para que solamente permita una cantidad fija de inten-
#tos.

# c) Modificar el programa anterior para que después de cada intento agregue una pausa
#cada vez mayor, utilizando la función sleep del módulo time.

# d) Modificar el programa anterior para que sea una función que devuelva si el usuario
#ingresó o no la contraseña correctamente, mediante un valor booleano (True o False).

def check_password(password):
    """
    """

    password = 'papermac'
    entry = input('write your password: ')
    while entry != password:
        print('wrong password, try again')
        entry = input('ingrese su password: ')
        
        
    print('access granted')

#check_password('')

import time 

def check_password2(entry, password):
    """
    """
    password = 'papermac'

    for i in range(5):
        entry = input('write your password: ')
        if entry == password:
            print('access granted')
            break
        print('wrong password, try again')
        time.sleep(i + 1)
        
    


#check_password2('','')


def check_password3(entry, password):
    """
    """
    password = 'papermac'

    for i in range(5):
        entry = input('write your password: ')
        if entry == password:
            print('access granted')
            return True
        time.sleep(i + 1)
    return False

print(check_password3('', ""))
     