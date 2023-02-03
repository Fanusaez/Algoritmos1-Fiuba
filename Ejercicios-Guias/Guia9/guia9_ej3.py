#Escribir un programa que vaya solicitando al usuario que ingrese nombres.
#a) Si el nombre se encuentra en la agenda (implementada con un diccionario), debe mostrar
#el teléfono y, opcionalmente, permitir modificarlo si no es correcto.
#b) Si el nombre no se encuentra, debe permitir ingresar el teléfono correspondiente.
#El usuario puede utilizar la cadena ”*”, para salir del programa.


def agenda():
    """
    usuario escribe un nombre, si no esta le pide que ingrese un numero
    si esta, le da el numero, si esta mal, lo puede cambiar
    """
    diccionario = {}
    nombre = ""
    while True:
        nombre = str(input('Ingrese un nombre, o "*" para salir: '))
        if nombre == '*':
            return False
        elif nombre in diccionario:
            print(f'telefono de {nombre} es {diccionario[nombre]}')
            nuevo_numero = int(input(f'ingrese nuevo numero para {nombre}: '))  
            if nuevo_numero == " ":
                continue
            diccionario[nombre] = nuevo_numero
            print(f'Telefono actulizado para {nombre}, {diccionario[nombre]}')
            continue
        elif nombre not in diccionario: 
            print('Persona no agendada')
            numero = int(input(f'ingrese el telefono para {nombre}: '))
            if numero == " ":
                continue
            diccionario.setdefault(nombre, numero)
            print(f'Nuevo telefono registrado para {nombre}, {numero}')
            continue
    return 
            
agenda()