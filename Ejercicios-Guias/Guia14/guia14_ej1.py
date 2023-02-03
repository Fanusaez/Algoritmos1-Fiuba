from clases import Cola
from clases import _Nodo

class TorreDeControl:

    def __init__(self):
        """ Inicializa la clase con dos colas """
        self.arrivos = Cola()
        self.partidas = Cola()

    def nuevo_arribo(self,avion):
        """
        """
        self.arrivos.encolar(avion)
    
    def nueva_partida(self,avion):
        """
        """
        self.partidas.encolar(avion)

    def ver_estado(self):
        aviones_arrivos = ''
        aviones_partidas = ''
        self.arrivos.encolar('*')
        self.partidas.encolar('*')
        
        while self.arrivos.ver_frente() != '*':  
            avion = self.arrivos.desencolar()
            self.arrivos.encolar(avion)
            aviones_arrivos += avion + ", "
        self.arrivos.desencolar()
        while self.partidas.ver_frente() != '*':
            avion = self.partidas.desencolar()
            self.partidas.encolar(avion)
            aviones_partidas += avion + ", "
        self.partidas.desencolar()
        arrivos = "Vuelos esperando para aterrizar: " + aviones_arrivos
        partidas = "Vuelos esperando para despegar: " + aviones_partidas
        print(f'{arrivos[0:-2]}')
        print(f'{partidas[0:-2]}')

    def asignar_pista(self):
        if self.arrivos.esta_vacia() is False:
            print(f"El vuelo {self.arrivos.desencolar()} aterrizó con éxito")   
        elif not self.partidas.esta_vacia():
            print(f"El vuelo {self.partidas.desencolar()} despegó con éxito")
        else: 
            print("No hay vuelos en espera.")
        
torre = TorreDeControl()
torre.nuevo_arribo('AR156')
torre.nueva_partida('KLM1267')
torre.nuevo_arribo('AR32')
torre.ver_estado()