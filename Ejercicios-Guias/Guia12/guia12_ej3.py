class Vector:
    """ Crea la clase vector """

    def __init__(self,coordenadas):
        self.coordenadas = coordenadas

    def __str__(self):
        """ imprime en formato [x,y,z] el vector"""
        coordenada = str(self.coordenadas)
        coordenada = coordenada.replace(" ","")
        return coordenada


    def __add__(self,otro):

        """ suma vectores de igual dimension"""

        if len(self.coordenadas) != len(otro.coordenadas):
            raise Exception("Vectores no tienen la misma cantidad de elementos.")
        nuevas_coordenadas = []
        for i in range(len(self.coordenadas)):
            nuevas_coordenadas.append(self.coordenadas[i] + otro.coordenadas[i])
        return Vector(nuevas_coordenadas)

    def __mul__(self,numero):

        """ multiplica un numero por un vector """

        nuevo_vector = []
        for i in range(len(self.coordenadas)):
            nuevo_vector.append(self.coordenadas[i] * numero)
        return Vector(nuevo_vector)