from clases import *

class Carta:
    '''
    DOC: Completar
    ''' 
    def __init__(self, palo, valor):
        self.palo = palo 
        self.valor = valor

class Solitario:
    '''
    DOC: Completar
    '''
    def __init__(self):
        self.pila_cartas = Pila()
    
    def apilar(self, carta):
        if self.pila_cartas.esta_vacia() or self.pila_cartas.ver_tope().valor > int(carta.valor):
            self.pila_cartas.apilar(carta)
        elif self.pila_cartas.ver_tope().valor > carta.valor and self.pila_cartas.ver_tope().palo != carta.palo:   
            self.pila_cartas.apilar(carta)
        else:
            raise Exception("Carta inválida")

solitario = Solitario()
solitario.apilar(Carta('Copa', 12))
solitario.apilar(Carta('Oro', 11))
solitario.apilar(Carta('Oro', 10))

solitario.apilar(Carta('Espada', 11))

solitario.apilar(Carta('Copa', 9))

solitario.apilar(Carta('Copa', 10))
