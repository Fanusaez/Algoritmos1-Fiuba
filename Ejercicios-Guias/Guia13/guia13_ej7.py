#Una lista circular es una lista cuyo último nodo está ligado al primero, de modo
#que es posible recorrerla infinitamente. Escribir la clase ListaCircular, 
#incluyendo los métodos insert, append, remove y pop.


class ListaCircular:

    def append(self, dato):
        '''
        DOC: Completar
        '''
        nuevo_nodo = _Nodo(dato)
        if not self.prim:
            self.prim = nuevo_nodo
        else:

            i = self.prim
            while self.prim:
                self.prim = self.prim.prox
            self.prim.prox = nuevo_nodo
            nuevo_nodo.prox = i

    def pop(self, i=None):
        '''
        DOC: Completar
        '''
        
        if i == None:
            i = self.cant - 1

        if i < 0 or i >= self.cant:
            raise ValueError

        if i == 0:
            self.prim = self.prim.prox      
            i = self.prim
            while self.prim:
                self.prim = self.prim.prox      
            self.prim.prox = i
        else:
            nodo_anterior = self.prim
            nodo_siguiente = self.prim.prox
            
            for _ in range(1,i):
                nodo_anterior = nodo_siguiente
                nodo_siguiente = nodo_siguiente.prox
            dato = nodo_siguiente.dato
            nodo_anterior.prox = nodo_siguiente.prox
            i = self.prim
            while nodo_siguiente:
                nodo_siguiente = nodo_siguiente.prox
            nodo_siguiente.prox = i
        self.cant -= 1
        return dato



    def __len__(self):
        return self.cant

    def __init__(self):
        # prim es un _Nodo o None
        self.prim = None
        self.cant = 0

class _Nodo:
    def __init__(self, dato, prox=None):
        self.dato = dato
        self.prox = prox