import gamelib
import chase


LINEAS_VERTICALES = 630
LINEAS_HORIZONTALES = 550
LADO_CUADRADO = 30
ANCHO_PANTALLA = 600
ALTO_PANTALLA = 540
GROSOR_TEXTO = 70
POS_DESEMPENO_ANCHO = 300
POS_DESEMPENO_ALTO = 200

def dibujar_grilla(juego):
    """ Dibuja la grilla de juego """

    for i in range(0, LINEAS_VERTICALES, LADO_CUADRADO):
        gamelib.draw_line(i, 0, i, ALTO_PANTALLA, fill = 'white', width = 2)
    for j in range(0, LINEAS_HORIZONTALES, LADO_CUADRADO):
        gamelib.draw_line(0, j, ANCHO_PANTALLA, j, fill = 'white', width = 2)
    for y in range(chase.ALTO_JUEGO):
        for x in range(chase.ANCHO_JUEGO):
            if juego[y][x] == chase.ROBOTS:
                gamelib.draw_image('Chase_Robots/robot.gif', x * LADO_CUADRADO, y * LADO_CUADRADO)
            elif juego[y][x] == chase.ESCOMBROS:
                gamelib.draw_image('Chase_Robots/escombros.gif', x * LADO_CUADRADO, y * LADO_CUADRADO)
            elif juego[y][x] == chase.JUGADOR:
                gamelib.draw_image('Chase_Robots/jugador.gif', x * LADO_CUADRADO, y * LADO_CUADRADO)
    

def avanzar(partida, accion):
    """ Recibe la accion ingresada por el jugador y la ejecta """
    accion = accion.lower()
    if accion == "q":
        partida.mover_jugador(chase.DIAGONAL_IZQ_ARR)
    elif accion == "w":
       partida.mover_jugador(chase.ARRIBA)
    elif accion == "e":
        partida.mover_jugador(chase.DIAGONAL_DER_ARR)
    elif accion == "a":
        partida.mover_jugador(chase.IZQUIERDA)
    elif accion == "s":
        partida.mover_jugador(chase.ABAJO)
    elif accion == "d":
        partida.mover_jugador(chase.DERECHA)
    elif accion == "z":
        partida.mover_jugador(chase.DIAGONAL_IZQ_ABA)
    elif accion == "c":
        partida.mover_jugador(chase.DIAGONAL_DER_ABA)
    elif accion == "t":
        partida.teletransportacion_jugador()

def mostrar_pantalla_desempeño(nombre, estado):
    """ Escribe el nombre del jugador en pantalla """
    if estado:
        gamelib.draw_text(f'Ganaste!: {nombre}',POS_DESEMPENO_ANCHO, POS_DESEMPENO_ALTO, size = GROSOR_TEXTO, fill = 'red')
    else:
        gamelib.draw_text(f'Perdiste!: {nombre}',POS_DESEMPENO_ANCHO, POS_DESEMPENO_ALTO, size = GROSOR_TEXTO, fill = 'yellow')

def main():
    nombre_jugador = gamelib.input("Ingrese nombre jugador")
    partida = chase.EstadoJuego()
    gamelib.resize(ANCHO_PANTALLA, ALTO_PANTALLA)

    while not partida.perdido:
        
        gamelib.draw_begin()
        dibujar_grilla(partida.juego)
        event = gamelib.wait(gamelib.EventType.KeyPress)
        tecla = event.key   
        if tecla.lower() not in ["w", "q", "e", "a", "s", "d", "z", "c", "t"]:
            continue
        avanzar(partida, tecla)
        partida.mover_robots()
        
        gamelib.draw_end()
        
        if partida.perdido:
            while gamelib.loop(fps=1):
                mostrar_pantalla_desempeño(nombre_jugador, False)

        elif partida.partida_ganado():
            while gamelib.loop(fps=1):
                mostrar_pantalla_desempeño(nombre_jugador, True)
               
        elif partida.siguiente_nivel():
            partida.nivel += 1
            partida.crear_juego(chase.NIVELES[f"{partida.nivel}"][0], chase.NIVELES[f"{partida.nivel}"][1])


gamelib.init(main)

