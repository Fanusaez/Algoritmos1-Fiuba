#a) Crear una clase Fraccion, que cuente con dos atributos: dividendo y divisor, que se
#asignan en el constructor, y se imprimen como X/Y en el método __str__.

class Fraccion:

    "crea la clase 'Fraccion'"

    def __init__(self,dividendo, divisor):
        """ Inicia la clase Fraccion """
        self.dividendo = dividendo        
        self.divisor = divisor 

    def __str__(self): 

        """ Imprime como fraccion la division"""

        return f"{self.dividendo} / {self.divisor}"

# b) Implementar el método __add__ que recibe otra fracción y devuelve una nueva fracción
#con la suma de ambas.

    def simplificar(self):  

        """ Simplidica fracciones"""

        mcd = 1
        for i in range(2, min(self.dividendo, self.divisor)+1):
            if self.dividendo % i == 0 and self.divisor % i == 0:
                mcd = i
        return Fraccion(int(self.dividendo/mcd), int(self.divisor/mcd))

    def __add__(self, otro):

        """ Suma fracciones, devuelve otra fraccion"""

        nuevo_divisor = self.divisor * otro.divisor
        nuevo_dividendo = self.dividendo * otro.divisor + otro.dividendo * self.divisor
        return Fraccion(nuevo_dividendo, nuevo_divisor).simplificar()

    def __mul__(self, otro):

        """ multiplica fracciones y las retorna simpificadas"""

        nuevo_dividendo = self.dividendo * otro.dividendo       
        nuevo_divisor = self.divisor * otro.divisor
        return Fraccion(nuevo_dividendo, nuevo_divisor).simplificar()


f = Fraccion(4,4)
o = Fraccion(4,4)
print(f * o)