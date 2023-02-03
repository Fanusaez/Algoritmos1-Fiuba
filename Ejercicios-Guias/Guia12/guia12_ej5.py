#Crear las clases Materia y Carrera, que se comporten según el siguiente ejemplo:

class Carrera:
    """ Crea la clase Carrera """

    def __init__(self,lista_materias):
        """ Inicializa la clase Carrera """

        self.lista_materias = lista_materias
        self.materias_aprobadas = {}

    def aprobar(self,codigo,nota):
        """ Aprueba la materia inidicada """

        if codigo not in self.codigo:
            raise Exception(f"La materia {codigo} no es parte del plan de estudios")
        self.materias_aprobadas[codigo] = nota

    def __str__(self):
        contador = 0
        for codigo in self.materias_aprobadas:
            contador += self.materias_aprobadas[codigo]  
        promedio = contador / len(self.materias_aprobadas) 

        print(f"Creditos: {(self.creditos)} -- Promedio:{promedio} -- Materias aprobadas: {self.materias_aprobadas}  ")

class Materia:
    "crea la clase materia"
    
    def __init__(self,codigo,nombre,creditos):
        """Iniciliza la clase materia"""

        self.codigo = codigo        
        self.nombre = nombre        
        self.creditos = creditos
        
