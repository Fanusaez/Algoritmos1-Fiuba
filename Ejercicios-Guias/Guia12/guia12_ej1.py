# a) Implementar la clase Intervalo(desde, hasta) que representa un intervalo entre dos
#instantes de tiempo (números enteros expresados en segundos), con la condición desde
#< hasta.

class Intervalo:


    def __init__(self, desde, hasta):
        """
        """ 
        self.desde = desde  
        self.hasta = hasta      


#b) Implementar el método duracion que devuelve la duración en segundos del intervalo.


    def duracion(self):
        """ 
        """
        return self.hasta - self.desde 

# c) Implementar el método interseccion que recibe otro intervalo y devuelve un nuevo in-
#tervalo resultante de la intersección entre ambos, o lanzar una excepción si la intersección
#es nula.

    def interseccion(self,segundo_intervalo):
        """
        """
        lista1 = []
        lista2 = []
        lista_interseccion = []
        for i in range(self.desde,self.hasta + 1):
            lista1.append(i)
        for j in range(segundo_intervalo.desde,segundo_intervalo.hasta + 1):
            lista2.append(j)
        for i in lista1:
            for j in lista2:
                if i == j:
                    lista_interseccion.append(i)
        if lista_interseccion == []:
            raise Exception("Interseccion entre intervalos es nula.")
        return Intervalo(int(lista_interseccion[0]), int(lista_interseccion[-1]))

#d) Implementar el método union que recibe otro intervalo. Si los intervalos no son adya-
#centes ni intersectan, debe lanzar una excepción. En caso contrario devuelve un nuevo
#intervalo resultante de la unión entre ambos.

    def union(self, segundo_intervalo):
        '''
        DOC: Completar
        '''
        lista1 = []
        lista2 = []
        lista_union = []
        for i in range(self.desde, self.hasta + 1):
            lista1.append(i)
        for j in range(segundo_intervalo.desde, segundo_intervalo.hasta + 1):
            lista2.append(j)
        for i in lista1:
            for j in lista2:
                if i == j or i+1 == j or i - 1 == j:
                    lista_union = lista1 + lista2   
                    lista_union = list(set(lista_union))
        if lista_union == []:
            raise Exception("Intervalos no son adyacentes.")
        return Intervalo(lista_union[0],lista_union[-1])

#####################################################################################



class Intervalo:
    """ Crea la clase 'intervalo' """ 

    def __init__(self, desde, hasta):
        """
        Inicia la clase "Intervalo". El parámetro "desde" debe ser
        extrictamente menor que "hasta". De lo contrario se lanza una excepcion
        que lo indica.
        """ 
        if desde < hasta:
            self.desde = desde  
            self.hasta = hasta      
        else:
            raise Exception("'Desde' debe ser menor que 'Hasta'.")


    def duracion(self):
        """ 
        Este metodo resta el valor de "desde" al valor de "hasta" para devolver
        la diferencia entre ellos, pues asi se entiende como la duracion del
        intervalo que representan.
        """
        return self.hasta - self.desde 

    def interseccion(self, segundo_intervalo):
        '''
        Este metodo recibe otro intervalo y lo compara con el primero para ver
        si se intersectan. De ser asi, devuelve dicha interseccion en un nuevo
        intervalo, sino lanza una excepcion.
        '''
        if self.desde < segundo_intervalo.desde < self.hasta:
            return Intervalo(segundo_intervalo.desde, self.hasta
        if self.desde < segundo_intervalo.hasta < self.hasta:
            return Intervalo(self.desde, segundo_intervalo.hasta)

        raise Exception("Interseccion entre intervalos es nula.")

    def union(self, segundo_intervalo):
        '''
        Este metodo recibe otro intervalo y lo compara con el primero para ver
        si se pueden unir. De ser asi, devuelve la union entre los intervalos
        como uno nuevo.

        Se entiende como parametros validos que los dos intervalos se
        intersecten o que sean adyacentes.
        '''
        if self.desde < segundo_intervalo.desde < self.hasta or segundo_intervalo.desde == self.hasta:
            return Intervalo(self.desde, segundo_intervalo.hasta)

        if self.desde < segundo_intervalo.hasta < self.hasta or self.desde == segundo_intervalo.hasta:
            return Intervalo(segundo_intervalo.desde, self.hasta)

        raise Exception("Intervalos no son adyacentes.")


    def __repr__(self):
        '''
        Metodo auxiliar hecho para que los intervalos aparezcan en la consola
        en formato "[desde ; hasta]"
        '''
        return f'[{self.desde} ; {self.hasta}]'
