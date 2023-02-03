#Crear una clase PilaConMaximo que soporte las operaciones de Pila (apilar(elemento), 
#desapilar() y ver_tope()), y además incluya el método obtener_maximo() en tiempo 
#constante.

from clases import *

class PilaConMaximo:
    '''
    DOC: Completar
    '''
    def __init__(self):
        self.pila_max = Pila()
        self.pila_todos = Pila()

    def ver_tope(self):
        if self.pila_todos.esta_vacia():
            raise Exception("Pila vacia")
        self.pila_todos.ver_tope()

    def apilar(self, elemento):
        if self.pila_max.esta_vacia():
            self.pila_max.apilar(elemento)
            self.pila_todos.apilar(elemento)
        else:
            self.pila_todos.apilar(elemento)
            valor = self.pila_max.desapilar()
            if type(valor) != type(elemento):
                raise ValueError
            elif valor > elemento:
                self.pila_max.apilar(elemento)
                self.pila_max.apilar(valor)
            else:
                self.pila_max.apilar(elemento)
                self.pila_todos.apilar(elemento)

    def desapilar(self):    
        if self.pila_todos.esta_vacia():
            raise Exception("Pila vacia")
        eliminado = self.pila_todos.desapilar()
        if eliminado == self.pila_max.ver_tope():
            self.pila_max.desapilar()

    def obtener_maximo(self):
        self.pila_max.desapilar()
