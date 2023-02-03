#Agregar a ListaEnlazada un método extend que reciba una ListaEnlazada y
#agregue a la lista actual los elementos que se encuentran en la lista recibida.

class _Nodo:

    def __init__(self,dato):
        self.dato = dato        
        self.prox = None


class ListaEnlazada:
    
    def __init__(self):
        self.prim = None
        self.len = 0

    def extend(self,lista):

        self.len += lista.len

        if not lista.prim:
            return
        nodo_aux = lista.prim
        
        if not self.prim:
            self.prim = _Nodo(nodo_aux.dato)
            nodo_aux = lista.prim.prox

        nodo_actual = self.prim

        while nodo_actual.prox:
            nodo_actual = nodo_actual.prox
      
        while nodo_aux:
            nodo_actual.prox = _Nodo(nodo_aux.dato)
            nodo_actual = nodo_actual.prox
            nodo_aux = nodo_aux.prox


