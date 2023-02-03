#Escribir un método de la clase ListaEnlazada que invierta el orden de la lista
#(es decir, el primer elemento queda como último y viceversa).

class ListaEnlazada:

    def invertir(self):
        '''
        DOC: Completar
        '''
        nodo_anterior = nodo_siguiente = None
        while self.prim:    
            nodo_siguiente = self.prim.prox
            self.prim.prox = nodo_anterior
            nodo_anterior = self.prim    
            self.prim = nodo_siguiente
        self.prim = nodo_anterior


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