#Implementar el método __str__ de ListaEnlazada, para que se genere una
#salida legible de lo que contiene la lista, similar a las listas de python.



#Implementar el método pop(i) de ListaEnlazada, que elimina de la lista el nodo 
#correspondiente al índice i, y devuelve su dato.
#Si i está fuera de rango, debe levantar la excepción IndexError.
#Si no se recibe la posición, elimina el último elemento.



#Implementar el método insert(i, x) de ListaEnlazada, 
#que inserta el elemento x en la posición i. 



#Implementar el método remove(x) de ListaEnlazada, 
#que elimina la primera aparición del valor x en la lista.
#Si x no está en la lista, levanta ValueError.



class ListaEnlazada:

    def __str__(self):
        '''
        DOC: Completar
        '''
        actual = self.prim
        lista = ""
        while self.prim:
            lista+= actual.dato + ","
            actual = actual.prox
            
        return f"[{lista}]"

    def pop(self, i=None):
        '''
        DOC: Completar
        '''
        if i is None:
            i = self.cant - 1

        if i < 0 or i >= self.cant:
            raise IndexError("Fuera de rango")

        if i == 0:
            # Caso particular: saltear la cabecera de la lista
            dato = self.prim.dato
            self.prim = self.prim.prox
        else:
            # Buscar los nodos en las posiciones (i-1) e (i)
            n_ant = self.prim
            n_act = self.prim.prox  
            for _ in range(1,i):
                n_ant = n_act    
                n_act = n_ant.prox
            # Guardar el dato y descartar el nodo
            dato = n_act.dato   
            n_ant.prox = n_act.prox
        self.cant -= 1
        return dato

    def insert(self, i, x):
        '''
        DOC: Completar
        '''
        if i < 0 or i > self.cant:
            raise IndexError("Fuera de rango breo")

        nuevo = _Nodo(x)

        if i == 0:
            # Caso particular: insertar al principio
            nuevo.prox = self.prim   
            self.prim = nuevo
        else:
            # Buscar el nodo anterior a la posición deseada
            n_ant = self.prim       
            for _ in range(1,i):
                n_ant = n_ant.prox  
            # Intercalar el nuevo nodo
            nuevo.prox = n_ant.prox
            n_ant.prox = nuevo
        self.cant += 1

    def remove(self, x):
        '''
        DOC: Completar
        '''
        if self.prim.dato == x:
        # Caso particular: saltear la cabecera de la lista
            self.prim = self.prim.prox
        else:
        # Buscar el nodo anterior al que contiene a x (n_ant)
            n_ant = self.prim  
            n_act = self.prim.prox     
            while n_act and n_act.dato != x:
                n_ant = n_act       
                n_act = n_ant.prox
            if n_act == None:
                raise ValueError("El valor no esta en la lista")
            # Descarto el nodo
            n_ant.prox = n_act.prox  

        self.cant -= 1

####################################################################

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
