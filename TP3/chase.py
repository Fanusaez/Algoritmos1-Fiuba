import random
import csv


ALTO_JUEGO = 18
ANCHO_JUEGO = 20

VACIO = 0
ZERO = 0
JUGADOR = 1
ROBOTS = 2
ESCOMBROS = 3

ARRIBA , ABAJO= [0, -1], [0, 1]
DERECHA , IZQUIERDA = [1, 0], [-1, 0]
DIAGONAL_DER_ARR, DIAGONAL_DER_ABA = [1, -1], [1, 1]
DIAGONAL_IZQ_ARR, DIAGONAL_IZQ_ABA = [-1, -1], [-1, 1]

X, Y = 0, 1

class EstadoJuego:

    def __init__(self):
        """ Inicializa estado de juego con los atributos y crea el juego en el
            primer nivel """

        self.perdido = False
        self.posicion_jugador = []
        self.posicion_robots = []
        self.juego = []
        self.nivel = 1

        self.crear_juego(NIVELES[f"{self.nivel}"][0], NIVELES[f"{self.nivel}"][1])


    def crear_juego(self, robots, escombros): 
        """Crea la matriz o grilla en donde se desarrollara el juego 20 x 20, 
        actualiza elatributo 'juego' y llama al metodo 'agregar_elemento'"""

       
        matriz = [[0 for _ in range(ANCHO_JUEGO)] for _ in range(ALTO_JUEGO)]

        self.juego = matriz
        self.agregar_elemeto(ROBOTS, robots)
        self.agregar_elemeto(ESCOMBROS, escombros)
        self.agregar_elemeto(JUGADOR, 1)

    def agregar_elemeto(self, elemento, n):
        """Agrega un elemento determiando n cantidad de veces en la matriz 'juego'
        actualiza los atributos 'juego', 'posicion_elemento' """

        pos_elemento = []
        juego = self.juego
        for _ in range(int(n)):  
            x = random.randint(0,ANCHO_JUEGO - 1)
            y = random.randint(0, ALTO_JUEGO - 1)
            juego[y][x] = elemento
            pos_elemento.append([x,y])
        if elemento == ROBOTS:
            self.posicion_robots = pos_elemento

        elif elemento == JUGADOR:
            self.posicion_jugador = pos_elemento[0]

        self.juego = juego 

    def trasladar_elemento(self, posicion, dx, dy):
        """ Traslada en la grilla a cualquier elemento una posicion dx, dy dada"""

        elemento_trasladado = [posicion[X] + dx, posicion[Y] + dy]
        return elemento_trasladado


    def mover_jugador(self, direccion):

        """Mueve el jugador en la direccion dada si es posible y llama al metodo
            'actualizar_juego_jugador' que se encarga de mover la posicion del jugador nueva """
        
        posicion = self.posicion_jugador
        posicion_nueva = []

        if direccion == DERECHA:
            if posicion[X] < ANCHO_JUEGO - 1 :
                posicion_nueva = self.trasladar_elemento(posicion, DERECHA[X], ZERO)

        elif direccion == IZQUIERDA:
            if posicion[X] > 0:
                posicion_nueva = self.trasladar_elemento(posicion, IZQUIERDA[X], ZERO)

        elif direccion == ARRIBA:
            if posicion[Y] > 0:
                posicion_nueva = self.trasladar_elemento(posicion, ZERO, ARRIBA[Y])

        elif direccion == ABAJO:
            if posicion[Y] < ALTO_JUEGO - 1 :
                posicion_nueva = self.trasladar_elemento(posicion, ZERO, ABAJO[Y])

        elif direccion == DIAGONAL_DER_ARR:
            if posicion[X] < ANCHO_JUEGO -1 and posicion[Y] > 0:
                posicion_nueva = self.trasladar_elemento(posicion, DERECHA[X], ARRIBA[Y])

        elif direccion == DIAGONAL_DER_ABA:
            if posicion[X] < ANCHO_JUEGO -1 and posicion[1] < ALTO_JUEGO -1:
                posicion_nueva = self.trasladar_elemento(posicion, DERECHA[X], ABAJO[Y])

        elif direccion == DIAGONAL_IZQ_ARR:
            if posicion[X] and posicion[Y] > 0:
                posicion_nueva = self.trasladar_elemento(posicion,  IZQUIERDA[X], ARRIBA[Y])  

        elif direccion == DIAGONAL_IZQ_ABA:
            if posicion[X] > 0 and posicion[Y] < ALTO_JUEGO - 1:
                posicion_nueva = self.trasladar_elemento(posicion,  IZQUIERDA[X], ABAJO[Y])

        if len(posicion_nueva) != 0:
            self.actualizar_juego_jugador(posicion_nueva)



    def mover_robots(self): 
        """Obtiene la poscion de cada robot trasladada en la direccion del jugador,
        al final llama al metodo 'actualizar_juego_robots' """

        posiciones = self.posicion_robots
        posicion_jug = self.posicion_jugador
        posiciones_rob_nueva = []
        
        for i in range(len(posiciones)):
            posiciones_rob = posiciones[i]
            
            if posiciones_rob[X] == posicion_jug[X] and posiciones_rob[Y] > posicion_jug[Y]:
                posicion_rob_nueva = self.trasladar_elemento(posiciones_rob, ZERO, ARRIBA[Y])
            
            elif posiciones_rob[X] == posicion_jug[X] and posiciones_rob[Y] < posicion_jug[Y]:
                posicion_rob_nueva = self.trasladar_elemento(posiciones_rob, ZERO, ABAJO[Y])

            elif posiciones_rob[X] > posicion_jug[X] and posiciones_rob[Y] == posicion_jug[Y]:
                posicion_rob_nueva = self.trasladar_elemento(posiciones_rob, IZQUIERDA[X], ZERO)

            elif posiciones_rob[X] < posicion_jug[X] and posiciones_rob[Y] == posicion_jug[Y]:
                posicion_rob_nueva = self.trasladar_elemento(posiciones_rob, DERECHA[X], ZERO)

            elif posiciones_rob[X] > posicion_jug[X] and posiciones_rob[Y] > posicion_jug[Y]:
                posicion_rob_nueva = self.trasladar_elemento(posiciones_rob, IZQUIERDA[X], ARRIBA[Y])

            elif posiciones_rob[X] < posicion_jug[X] and posiciones_rob[Y] < posicion_jug[Y]:
                posicion_rob_nueva = self.trasladar_elemento(posiciones_rob, DERECHA[X], ABAJO[Y])

            elif posiciones_rob[X] > posicion_jug[X] and posiciones_rob[Y] < posicion_jug[Y]:
                posicion_rob_nueva = self.trasladar_elemento(posiciones_rob, IZQUIERDA[X], ABAJO[Y])

            elif posiciones_rob[X] < posicion_jug[X] and posiciones_rob[Y] > posicion_jug[Y]:
                posicion_rob_nueva = self.trasladar_elemento(posiciones_rob, DERECHA[X], ARRIBA[Y])

            if posicion_rob_nueva != []:
                posiciones_rob_nueva.append(posicion_rob_nueva)
        
        if posiciones_rob_nueva != []:
            self.actualizar_juego_robots(posiciones_rob_nueva)


    
    def actualizar_juego_jugador(self, posicion_nueva):
        """ Actualiza el atributo 'juego' segun las posiciones nuevas, tambien 'posicion_jugador'
            si el jugador se movio a un lugar prohibido, el atributo 'perdido' se cambiara a  false"""

        juego = self.juego
        posicion_vieja = self.posicion_jugador
        juego[posicion_vieja[Y]][posicion_vieja[X]] = VACIO
        
        if juego[posicion_nueva[Y]][posicion_nueva[X]] == ROBOTS:
            self.perdido = True

        # Casos en que hay un escombro en la posicion nueva del jugador

        elif juego[posicion_nueva[Y]][posicion_nueva[X]] == ESCOMBROS:
            movimiento = [posicion_nueva[X] - posicion_vieja[X], posicion_nueva[Y] - posicion_vieja[Y]]
            posicion_nueva_escombro = [posicion_nueva[X] + movimiento[X], posicion_nueva[Y] + movimiento[Y]]
            self.mover_escombros(posicion_nueva, posicion_nueva_escombro, posicion_vieja)

        else:
            juego[posicion_nueva[Y]][posicion_nueva[X]] = JUGADOR
            self.posicion_jugador = posicion_nueva
        self.juego = juego

    def mover_escombros(self, posicion_jugador, posicion_escombro, posicion_jugador_vieja):
        """Mueve los escombros a la posicion dada, y actualiza los atributos 'juego', 'posicion_jugador'
        'posicion_robots' """

        juego = self.juego
        if posicion_escombro[X] >= ANCHO_JUEGO or posicion_escombro[Y] >= ALTO_JUEGO or posicion_escombro[X] < 0 or posicion_escombro[Y] < 0:
            juego[posicion_jugador_vieja[Y]][posicion_jugador_vieja[X]] = JUGADOR

        elif juego[posicion_escombro[Y]][posicion_escombro[X]] != ESCOMBROS:
                
            if posicion_escombro[Y] <= ALTO_JUEGO - 1 and posicion_escombro[X] <= ANCHO_JUEGO - 1: 
                juego[posicion_jugador[Y]][posicion_jugador[X]] = JUGADOR   
                self.posicion_jugador = posicion_jugador
                juego[posicion_escombro[Y]][posicion_escombro[X]] = ESCOMBROS
                posicion_robots = self.posicion_robots

                if [posicion_escombro[X],posicion_escombro[Y]] in posicion_robots:
                        posicion_robots.remove([posicion_escombro[X],posicion_escombro[Y]])
                        self.posicion_robots = posicion_robots
        else:
            juego[posicion_jugador_vieja[Y]][posicion_jugador_vieja[X]] = JUGADOR

        self.juego = juego

    def actualizar_juego_robots(self, posiciones_nuevas):
        """ Actualiza el atributo 'juego' segun las posiciones nuevas y viejas de los robots, 
            tambien actualiza 'posiciones_robots' """
        juego = self.juego
        posiciones_viejas = self.posicion_robots
        posiciones_robots_nueva = []

        # para no ordenar 
        for i in range(len(posiciones_viejas)):
            posicion_vieja = posiciones_viejas[i]
            juego[posicion_vieja[Y]][posicion_vieja[X]] = VACIO

        for i in range(len(posiciones_nuevas)):
            posicion_nueva = posiciones_nuevas[i]

            if juego[posicion_nueva[Y]][posicion_nueva[X]] == ROBOTS:  
                juego[posicion_nueva[Y]][posicion_nueva[X]] = ESCOMBROS
                if [posicion_nueva[X],posicion_nueva[Y]] in posiciones_robots_nueva:
                    posiciones_robots_nueva.remove([posicion_nueva[X],posicion_nueva[Y]])

            elif juego[posicion_nueva[Y]][posicion_nueva[X]] == JUGADOR:
                juego[posicion_vieja[Y]][posicion_vieja[X]] = ESCOMBROS
                self.perdido = True 

            elif juego[posicion_nueva[Y]][posicion_nueva[X]] == VACIO:
                juego[posicion_nueva[Y]][posicion_nueva[X]] = ROBOTS
                posiciones_robots_nueva.append([posicion_nueva[X],posicion_nueva[Y]])

        self.posicion_robots = posiciones_robots_nueva
        self.juego = juego    

    def teletransportacion_jugador(self):
        """ Al usar esta funcion el jugador se teletransportara a un lugar al azar de
            la grilla, si aterriza sobre escombro o un robot, el juego terminara, 
            actualiza los atributos 'juego' y 'posicion_jugador' """ 

        juego = self.juego
        posicion_jugador = self.posicion_jugador
        juego[posicion_jugador[Y]][posicion_jugador[X]] = VACIO

        posicion_nueva = [random.randint(0,ANCHO_JUEGO - 1),random.randint(0,ALTO_JUEGO - 1)]

        if juego[posicion_nueva[Y]][posicion_nueva[X]] == ESCOMBROS or juego[posicion_nueva[1]][posicion_nueva[0]] == ROBOTS:
            self.perdido = True
        else:  
            juego[posicion_nueva[Y]][posicion_nueva[X]] = JUGADOR
            self.posicion_jugador = posicion_nueva
        
        self.juego = juego      

    def siguiente_nivel(self):
        """ Devuelve un booleano si el jugador paso al sigueinte nivel"""

        if not self.perdido and len(self.posicion_robots) == 0:
            return True
        return False

    def partida_ganado(self):
        """ Devuelve true si el juego fue superado en su totalidad, de lo contrario false """

        if len(NIVELES) == self.nivel and self.siguiente_nivel():
            return True
        return False

def definir_niveles():
    """ Escribe los niveles deseados en 'niveles.txt' """

    with open("niveles.txt", "w") as f:
        nivel = 1
        robots = 2
        escombros = 4
        for _ in range(5):
            f.write(f"{nivel},{robots},{escombros}\n")
            nivel += 1
            robots *= 2
            escombros += 1


def diccionario_niveles():
    """ Crea un diccionario con los niveles guardados en 'niveles.txt'  y lo devuelve"""

    with open("niveles.txt", "r+") as f:
        dic_niveles = {}
        csv_reader = csv.reader(f, delimiter = ",")
        for linea in csv_reader:
            dic_niveles[linea[0]] = [linea[1], linea[2]]
        return dic_niveles

NIVELES = diccionario_niveles()