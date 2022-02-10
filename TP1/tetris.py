ANCHO_JUEGO, ALTO_JUEGO = 9, 18
IZQUIERDA, DERECHA = -1, 1
CUBO = 0
Z = 1
S = 2
I = 3
L = 4
L_INV = 5
T = 6


PIEZAS = (
    ((0, 0), (1, 0), (0, 1), (1, 1)), # Cubo
    ((0, 0), (1, 0), (1, 1), (2, 1)), # Z (zig-zag)
    ((0, 0), (0, 1), (1, 1), (1, 2)), # S (-Z)
    ((0, 0), (0, 1), (0, 2), (0, 3)), # I (línea)
    ((0, 0), (0, 1), (0, 2), (1, 2)), # L
    ((0, 0), (1, 0), (2, 0), (2, 1)), # -L
    ((0, 0), (1, 0), (2, 0), (1, 1)), # T
)
ACTUAL = 1
CONSOLIDADO = 2

#import pieza.generar_pieza
import random
def generar_pieza(pieza=None):
    """
    Genera una nueva pieza de entre PIEZAS al azar. Si se especelifica el parámetro pieza
    se generará una pieza del tipo indicado. Los tipos de pieza posibles
    están dados por las constantes CUBO, Z, S, I, L, L_INV, T.

    El valor retornado es una tupla donde cada elemento es una posición
    ocupada por la pieza, ubicada en (0, 0). Por ejemplo, para la pieza
    I se devolverá: ( (0, 0), (0, 1), (0, 2), (0, 3) ), indicando que 
    ocupa las posiciones (x = 0, y = 0), (x = 0, y = 1), ..., etc.
    """
    if pieza == None:    
        return PIEZAS[random.randint(0,6)]
    return PIEZAS[pieza]
    

def trasladar_pieza(pieza, dx, dy):
    """
    Traslada la pieza de su posición actual a (posicion + (dx, dy)).

    La pieza está representada como una tupla de posiciones ocupadas,
    donde cada posición ocupada es una tupla (x, y). 
    Por ejemplo para la pieza ( (0, 0), (0, 1), (0, 2), (0, 3) ) y
    el desplazamiento dx=2, dy=3 se devolverá la pieza 
    ( (2, 3), (2, 4), (2, 5), (2, 6) ).
    """
    pieza_moviendose = []
    for i in range(len(pieza)):
        pieza_moviendose.append(tuple([pieza[i][0] + dx, pieza[i][1] + dy]))
   
    return tuple(pieza_moviendose)
    


def crear_juego(pieza_inicial):
    """
    Crea un nuevo juego de Tetris.

    El parámetro pieza_inicial es una pieza obtenida mediante 
    pieza.generar_pieza. Ver documentación de esa función para más información.

    El juego creado debe cumplir con lo siguiente:
    - La grilla está vacía: hay_superficie da False para todas las ubicaciones
    - La pieza actual está arriba de todo, en el centro de la pantalla.
    - El juego no está terminado: terminado(juego) da False

    Que la pieza actual esté arriba de todo signelifica que la coordenada Y de 
    sus posiciones superiores es 0 (cero).
    """
    
    matriz = []
    for _ in range(ALTO_JUEGO):
        lista_aux = []
        for _ in range(ANCHO_JUEGO):
            lista_aux.append(0)
        matriz.append(lista_aux)
    pieza_centrada = trasladar_pieza(pieza_inicial,4,0)
    
    for pieza in pieza_centrada:
        x,y = pieza
        matriz[y][x] = ACTUAL
    return matriz  


def dimensiones(juego):
    """
    Devuelve las dimensiones de la grilla del juego como una tupla (ancho, alto).
    """
    alto = len(juego)
    ancho = len(juego[0])

    return (ancho,alto)


def pieza_actual(juego):
    """ 
    Devuelve una tupla de tuplas (x, y) con todas las posiciones de la
    grilla ocupadas por la pieza actual.

    Se entiende por pieza actual a la pieza que está cayendo y todavía no
    fue consolidada con la superficie.

    La coordenada (0, 0) se refiere a la posición que está en la esquina 
    superior izquierda de la grilla.
    """
    ancho,alto = dimensiones(juego)
    lista = []
    for y in range(alto):
        for x in range(ancho):
            if juego[y][x] == ACTUAL:  
                lista.append((x,y))

    return tuple(lista)

def hay_superficie(juego, x, y):
    """
    Devuelve True si la celda (x, y) está ocupada por la superficie consolidada.
    
    La coordenada (0, 0) se refiere a la posición que está en la esquina 
    superior izquierda de la grilla.
    """
    
    if juego[y][x] == CONSOLIDADO: 
        return True
    
    return False
    

def mover(juego, direccion):
    """
    Mueve la pieza actual hacia la derecha o izquierda, si es posible.
    Devuelve un nuevo estado de juego con la pieza movida o el mismo estado 
    recibido si el movimiento no se puede realizar.

    El parámetro direccion debe ser una de las constantes DERECHA o IZQUIERDA.
    """
    ancho,_ = dimensiones(juego)
    if direccion == DERECHA:
        posicion_ficha = pieza_actual(juego)
        for posicion in posicion_ficha:
            if posicion[0] >= ancho - 1:
                return juego
        return mover_pieza(juego,trasladar_pieza(posicion_ficha,DERECHA,0))
    
    elif direccion == IZQUIERDA:
        posicion_ficha = pieza_actual(juego)
        for posicion in posicion_ficha:
            if posicion[0] == 0:
                return juego
        return mover_pieza(juego,trasladar_pieza(posicion_ficha,IZQUIERDA,0))


def mover_pieza(juego, posicion_nueva):
    """
    recibe juego  actual y mueve la ficha a la posicion que se le da 
    """
    ancho,alto = dimensiones(juego)
    for y in range(alto):
        for x in range(ancho):
            if juego[y][x] == ACTUAL:
                juego[y][x] = 0

    for posicion in posicion_nueva:
        x,y = posicion
        juego[y][x] = ACTUAL
    return juego
    
def avanzar(juego, siguiente_pieza):
    """
    Avanza al siguiente estado de juego a partir del estado actual.
    
    Devuelve una tupla (juego_nuevo, cambiar_pieza) donde el primer valor
    es el nuevo estado del juego y el segundo valor es un booleano que indica
    si se debe cambiar la siguiente_pieza (es decir, se consolidó la pieza
    actual con la superficie).
    
    Avanzar el estado del juego signelifica:
     - Descender una posición la pieza actual.
     - Si al descender la pieza no colisiona con la superficie, simplemente
       devolver el nuevo juego con la pieza en la nueva ubicación.
     - En caso contrario, se debe
       - Consolidar la pieza actual con la superficie.
       - Eliminar las líneas que se hayan completado.
       - Cambiar la pieza actual por siguiente_pieza.

    Si se debe agregar una nueva pieza, se utilizará la pieza indicada en
    el parámetro siguiente_pieza. El valor del parámetro es una pieza obtenida 
    llamando a generar_pieza().

    **NOTA:** Hay una simplelificación respecto del Tetris real a tener en
    consideración en esta función: la próxima pieza a agregar debe entrar 
    completamente en la grilla para poder seguir jugando, si al intentar 
    incorporar la nueva pieza arriba de todo en el medio de la grilla se
    pisara la superficie, se considerará que el juego está terminado.

    Si el juego está terminado (no se pueden agregar más piezas), la funcion no hace nada, 
    se debe devolver el mismo juego que se recibió.
    """ 
    ancho,alto = dimensiones(juego)
    posicion_ficha = pieza_actual(juego)
     # caso en donde hay una ficha en juego y la voy a mover
    for posicion in posicion_ficha:
        x,y = posicion
        if ((y) == (alto - 1)) or hay_superficie(juego, x, y + 1):   
            juego = consolidar_ficha(juego)

            # ver si una fila entera es 2 y eliminrla
            eliminar_filas_consolidadas(juego) 
            
            if not terminado(juego): # centrar la ficha que recibo y ubircarla en el juego
                pieza_centrada = trasladar_pieza(siguiente_pieza,ancho // 2,0)
                for posicion in pieza_centrada:
                    x,y = posicion
                    juego[y][x] = ACTUAL
            return juego, True
    juego = mover_pieza(juego,trasladar_pieza(posicion_ficha,0,1))
    return juego, False

def eliminar_filas_consolidadas(juego):
    """
    Elimina filas consolidadas y agrega nueva fila vacia en lo mas alto del juego
    """
    ancho,alto = dimensiones(juego)
    for y in range(alto):
        fila_completa = [2] * ancho
        if fila_completa == juego[y]:
            juego.pop(y)
            fila_a_insertar = [0] * ancho
            juego.insert(0,fila_a_insertar)                     
    return juego
            
def consolidar_ficha(juego):
    """
    consolida la ficha y lo representa con un 2 
    """
    ancho,alto = dimensiones(juego)
    for y in range(alto):
        for x in range(ancho):
            if juego[y][x] == ACTUAL:
                juego[y][x] = CONSOLIDADO
    return juego



def terminado(juego):
    """
    Devuelve True si el juego terminó, es decir no se pueden agregar
    nuevas piezas, o False si se puede seguir jugando.
    """
    ancho,_ = dimensiones(juego)
    for pieza in PIEZAS:
        pieza_centrada =  trasladar_pieza(pieza,ancho // 2,0)
        for posicion in pieza_centrada:
            if juego[posicion[1]][posicion[0]] == CONSOLIDADO:
                return True
    return False
