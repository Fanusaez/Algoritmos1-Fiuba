#Implementar el método filter(f) de ListaEnlazada, que recibe una función y
#devuelve una nueva lista enlazada con los elementos para los cuales 
#la aplicación de f devuelve
#True. La nueva lista debe ser construida recorriendo los nodos una sola vez (es decir, no se
#puede llamar a append



class ListaEnlazada:

    def filter(self, f):
        '''
        DOC: Completar
        '''
        nueva_lista = ListaEnlazada()
        nodo_actual = self.prim

        while nodo_actual and not f(nodo_actual.dato):
            nodo_actual = nodo_actual.prox      

        if not nodo_actual: 
        # Caso en que no haya lista_original o no pase la filtracion ningun elemento
            return nueva_lista
        
        nueva_lista.prim = _Nodo(nodo_actual.dato) # Primer elemento de mi nueva lista
        nodo_actual_nuevo = nueva_lista.prim
        nodo_actual = nodo_actual.prox
        nueva_lista.cant += 1
        while nodo_actual:
            if f(nodo_actual.dato):
                nodo_actual_nuevo.prox = _Nodo(nodo_actual.dato)
                nodo_actual_nuevo = nodo_actual_nuevo.prox
                nueva_lista.cant += 1
            nodo_actual = nodo_actual.prox
        return nueva_lista




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