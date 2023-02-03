#Implementar el método remover_todos(elemento) de ListaEnlazada, que re-
#cibe un elemento y remueve de la lista todas las apariciones del mismo,
#devolviendo la cantidad
#de elementos removidos. La lista debe ser recorrida una sola vez.


class ListaEnlazada:

    def remover_todos(self, elem):
        '''
        DOC: Completar
        ''' 
        removidos = 0
        while self.prim and self.prim.dato == elem:
            self.prim = self.prim.prox
            removidos += 1
            self.cant -= 1
        if not self.prim:
            return removidos
        nodo_ant = self.prim
        nodo_act = self.prim.prox
        
        while nodo_act:
            if nodo_act.dato == elem:
                while nodo_act and nodo_act.dato == elem:
                    nodo_act = nodo_act.prox
                    removidos += 1
                    self.cant -= 1
                nodo_ant.prox = nodo_act
            else:
                nodo_ant.prox = nodo_act
                nodo_ant = nodo_act
                nodo_act = nodo_act.prox
           
        return removidos

    def __init__(self):
        # prim es un _Nodo o None
        self.prim = None
        self.cant = 0


    def append(self, dato):
        nuevo = _Nodo(dato)
        if not self.prim:
            self.prim = nuevo
        else:
            act = self.prim
            while act.prox:
                act = act.prox
            # act es el ultimo nodo
            act.prox = nuevo
        self.cant += 1

    def __len__(self):
        return self.cant

class _Nodo:
    def __init__(self, dato, prox=None):
        self.dato = dato
        self.prox = prox