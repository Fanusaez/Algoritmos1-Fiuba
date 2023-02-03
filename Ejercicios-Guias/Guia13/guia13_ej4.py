#Implementar el método duplicar(elemento) de ListaEnlazada, que recibe un
#elemento y duplica todas las apariciones del mismo.

class ListaEnlazada:

    def duplicar(self, elem):
        '''
        DOC: Completar
        '''
        if not self.prim:
            return 
        nodo_actual = self.prim
        while nodo_actual.prox:
            if nodo_actual.dato == elem:
                nuevo_nodo = _Nodo(elem,nodo_actual.prox)
                nodo_actual.prox = nuevo_nodo
                nodo_actual = nodo_actual.prox.prox
                self.cant += 1
            else:
                nodo_actual = nodo_actual.prox
        if not nodo_actual.prox and nodo_actual.dato == elem:
            nuevo_nodo = _Nodo(elem)
            nodo_actual.prox = nuevo_nodo

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