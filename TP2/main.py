
import tetris 
import gamelib
import csv

ESPERA_DESCENDER = 8

#INTERFAZ GRAFICA

def dibujar_grilla(juego):
    """ Dibuja la grilla de juego """
    for i in range(0,271,30):
        gamelib.draw_line(i,0,i,540, fill = 'white', width = 2)
    for j in range(0,541,30):
        gamelib.draw_line(0,j,270,j, fill = 'white', width = 2)
    dibujar_pieza(juego)
    # Dibujo piezas consolidadas
    for y in range(tetris.ALTO_JUEGO):
        for x in range(tetris.ANCHO_JUEGO):
            if juego[y][x] == tetris.CONSOLIDADO:
                gamelib.draw_rectangle(x * 30 + 30, y * 30 + 30, x * 30, y * 30,outline='white', fill='pink')

def dibujar_pieza(juego):
    """Recibe la pieza en movimiento y la dibuja en la grilla """
    pieza = tetris.pieza_actual(juego)
    for posicion in pieza:
        gamelib.draw_rectangle(posicion[0] * 30 + 30, posicion[1] * 30 + 30, posicion[0] * 30, posicion[1] * 30,outline='white', fill='red')
    
def dibujar_siguiente(pieza_siguiente):
    """ Dibuja la siguiente pieza que se mostrara fuera del tablero """

    pieza_siguiente = tetris.trasladar_pieza(pieza_siguiente, 12, 2)
    for posicion in pieza_siguiente:
        gamelib.draw_rectangle(posicion[0] * 30 + 30, posicion[1] * 30 + 30, posicion[0] * 30, posicion[1] * 30, outline='white', fill='orange')

def dibujar_puntaje(puntaje):   
    """ Dibuja el puntaje en la pantalla """

    
def puntajes_en_pantalla():
    "Dibuja los diez mejores puntjaes del juego en pantalla"

    gamelib.draw_text("Mejores Puntajes:",400, 250, size = 30, fill = 'gold')
    with open("puntuaciones.txt") as f:
        csv_reader = csv.reader(f)
        alto = 0
        for linea in csv_reader:
            gamelib.draw_text(f"{linea[0]},{linea[1]}",390, 300 + alto, size = 15, fill = 'gold')
            alto += 20

######Puntajes########

def creador_diccionario():
    """Crea diccionario con los 10 mejores puntajes del juego"""

    dic_puntajes = {}
    with open("puntuaciones.txt") as f:
        csv_reader = csv.reader(f, delimiter = ",")
        for linea in csv_reader:
            dic_puntajes[linea[0]] = int(linea[1])
        if len(dic_puntajes) <= 10:
            return ordenar_puntajes(dic_puntajes)
        else:
            nombre_menor, menor_puntaje = None, 900000000
            for llave, valor in dic_puntajes.items():
                if int(valor) < int(menor_puntaje):
                    nombre_menor, menor_puntaje = llave, valor
            dic_puntajes.pop(nombre_menor)
            return ordenar_puntajes(dic_puntajes)

def puntajes_maximos(puntaje):
    """ Escribe los puntajes en puntuaciones.txt """
    
    with open('puntuaciones.txt', 'a') as puntuaciones:
        nombre = gamelib.input("Ingrese nombre jugador")
        puntuaciones.write(f"{nombre},{puntaje}\n")
    creador_diccionario()
        

def ordenar_puntajes(dic_puntajes):
    """Ordena los puntajes de mayor a menor en putuaciones.txt"""

    with open("puntuaciones.txt","w") as f:
        while len(dic_puntajes) != 0:
            mayor_nombre, mayor_valor = None, 0
            for llave, valor in dic_puntajes.items():
                if int(valor) > int(mayor_valor):
                    mayor_nombre, mayor_valor = llave, valor
            f.write(f"{mayor_nombre},{mayor_valor}\n")
            dic_puntajes.pop(mayor_nombre)
            

#CONTROLES

def diccionario_acciones():
    """ Crea un diccionario de acciones mediante el archivo 'teclas.txt' """
    with open('teclas.txt') as teclas:
        reader = csv.reader(teclas, delimiter = "=")
        diccionario_acciones = {}
        for fila in reader:           
            if fila == []:
                continue
            diccionario_acciones[fila[0].rstrip()] = fila[1].lstrip()
        return diccionario_acciones

DICCIONARIO_ACCIONES = diccionario_acciones()

def tecla_presionada(tecla, juego, puntaje):
    
    if DICCIONARIO_ACCIONES[tecla] == 'DERECHA':  
        tetris.mover(juego, tetris.DERECHA)
    elif DICCIONARIO_ACCIONES[tecla] == 'IZQUIERDA':
        tetris.mover(juego, tetris.IZQUIERDA)
    elif DICCIONARIO_ACCIONES[tecla] == 'DESCENDER':
        tetris.avanzar(juego,tetris.generar_pieza(None))

    elif DICCIONARIO_ACCIONES[tecla] == 'ROTAR':
        tetris.rotar(juego)
    elif DICCIONARIO_ACCIONES[tecla] == 'GUARDAR':
        tetris.guardar_partida(juego,puntaje)

def main():
    # Inicializar el estado del juego
    juego = tetris.crear_juego(tetris.generar_pieza(None))
    puntaje = 0
    pieza_siguiente = tetris.generar_pieza(None)
    dibujar_siguiente(pieza_siguiente)
    gamelib.resize(550, 550)
    timer_bajar = ESPERA_DESCENDER
    while gamelib.loop(fps=20):
        #Si el juego termino,que llame a puntajes_maximos
        if tetris.terminado(juego):
            puntajes_en_pantalla()  
            puntajes_maximos(puntaje)
            return
        # Dibujar la pantalla
        gamelib.draw_begin()

        if tetris.verificador_pieza_por_consolidar(juego):
            tetris.avanzar(juego, pieza_siguiente)
            pieza_siguiente = tetris.generar_pieza(None)
        
        dibujar_siguiente(pieza_siguiente)
        dibujar_grilla(juego)
        dibujar_puntaje(puntaje)

        gamelib.draw_end()

        for event in gamelib.get_events():
            if not event:
                break
            if event.type == gamelib.EventType.KeyPress:
                tecla = event.key
                if tecla == "s":
                    puntaje += 10
                if tecla == "c":
                    juego, puntaje = tetris.cargar_partida()
                
              # Actualizar el juego, según la tecla presionada
                tecla_presionada(tecla,juego, puntaje)
        
        timer_bajar -= 1
        if timer_bajar == 0:
            timer_bajar = ESPERA_DESCENDER
            # Descender la pieza automáticamente
            tecla_presionada('s',juego, puntaje)
            puntaje+= 10
gamelib.init(main)
