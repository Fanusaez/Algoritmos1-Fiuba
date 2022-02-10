import tetris

# Si las pruebas se ven mal en tu terminal, probá cambiando el valor
# de esta constante a True para desactivar los colores ANSI.
TERMINAL_SIN_COLOR = False

# Estas constantes no se deben modificar
tetris.ANCHO_JUEGO, tetris.ALTO_JUEGO = 9, 18
IZQUIERDA, DERECHA = -1, 1

def test_trasladar_pieza_al_0_0():
    pieza_inicial = tetris.generar_pieza(tetris.T)
    pieza_trasladada = tetris.trasladar_pieza(pieza_inicial, 0, 0)
    return sorted(pieza_trasladada) == sorted(pieza_inicial)

def test_trasladar_pieza():
    pieza_inicial = ((0, 0), (1, 1))
    pieza_trasladada = tetris.trasladar_pieza(pieza_inicial, 2, 2)
    return sorted(pieza_trasladada) == sorted(((2, 2), (3, 3)))

def test_dimensiones_correctas():
    pieza_inicial = tetris.generar_pieza(tetris.T)
    juego = tetris.crear_juego(pieza_inicial)

    ancho, alto = tetris.dimensiones(juego)
    return ancho == tetris.ANCHO_JUEGO and alto == tetris.ALTO_JUEGO

def test_grilla_esta_vacia_al_iniciar():
    pieza_inicial = tetris.generar_pieza(tetris.T)
    juego = tetris.crear_juego(pieza_inicial)

    ancho, alto = tetris.dimensiones(juego)
    for y in range(alto):
        for x in range(ancho):
            if tetris.hay_superficie(juego, x, y):
                return False

    return True

def test_pieza_inicial_esta_arriba_en_el_medio_al_iniciar():
    pieza_inicial = tetris.generar_pieza(pieza=tetris.T)
    juego = tetris.crear_juego(pieza_inicial)

    pieza_centrada = tetris.trasladar_pieza(pieza_inicial, 
                                           tetris.ANCHO_JUEGO // 2, 
                                           0)

    return sorted(pieza_centrada) == sorted(tetris.pieza_actual(juego))

def test_juego_no_esta_terminado_al_iniciar():
    juego = tetris.crear_juego(tetris.generar_pieza(pieza=tetris.T))

    return not tetris.terminado(juego)

def test_mover_pieza_l_a_derecha():
    juego = tetris.crear_juego(tetris.generar_pieza(pieza=tetris.L))
    pieza_actual = tetris.pieza_actual(juego)

    juego = tetris.mover(juego, DERECHA)

    pieza_trasladada = tetris.trasladar_pieza(pieza_actual, DERECHA, 0)
    return sorted(pieza_trasladada) == sorted(tetris.pieza_actual(juego))

def test_mover_pieza_s_a_derecha():
    juego = tetris.crear_juego(tetris.generar_pieza(pieza=tetris.S))
    pieza_actual = tetris.pieza_actual(juego)

    juego = tetris.mover(juego, DERECHA)

    pieza_trasladada = tetris.trasladar_pieza(pieza_actual, DERECHA, 0)
    return sorted(pieza_trasladada) == sorted(tetris.pieza_actual(juego))

def test_mover_pieza_t_a_izquierda():
    juego = tetris.crear_juego(tetris.generar_pieza(pieza=tetris.T))
    pieza_actual = tetris.pieza_actual(juego)

    juego = tetris.mover(juego, IZQUIERDA)

    pieza_trasladada = tetris.trasladar_pieza(pieza_actual, IZQUIERDA, 0)
    return sorted(pieza_trasladada) == sorted(tetris.pieza_actual(juego))

def test_mover_pieza_i_a_izquierda():
    juego = tetris.crear_juego(tetris.generar_pieza(pieza=tetris.I))
    pieza_actual = tetris.pieza_actual(juego)

    juego = tetris.mover(juego, IZQUIERDA)

    pieza_trasladada = tetris.trasladar_pieza(pieza_actual, IZQUIERDA, 0)
    return sorted(pieza_trasladada) == sorted(tetris.pieza_actual(juego))

def test_mover_l_contra_pared_derecha():
    pieza_inicial = tetris.generar_pieza(tetris.L)
    juego = tetris.crear_juego(pieza_inicial)

    for _ in range(tetris.ANCHO_JUEGO + 5):
        juego = tetris.mover(juego, DERECHA)
    
    pieza_trasladada = tetris.trasladar_pieza(pieza_inicial, tetris.ANCHO_JUEGO - 2, 0)
    return sorted(pieza_trasladada) == sorted(tetris.pieza_actual(juego))

def test_mover_l_contra_pared_izquierda():
    pieza_inicial = tetris.generar_pieza(tetris.L)
    juego = tetris.crear_juego(pieza_inicial)

    for _ in range(tetris.ANCHO_JUEGO + 5):
        juego = tetris.mover(juego, IZQUIERDA)
    
    return sorted(pieza_inicial) == sorted(tetris.pieza_actual(juego))

def test_avanzar_baja_la_pieza_una_posicion():
    siguiente_pieza = tetris.generar_pieza(pieza=tetris.T)
    juego = tetris.crear_juego(tetris.generar_pieza(tetris.L))
    pieza_actual = tetris.pieza_actual(juego)

    juego, _ = tetris.avanzar(juego, siguiente_pieza)

    pieza_trasladada = tetris.trasladar_pieza(pieza_actual, 0, 1)
    return sorted(pieza_trasladada) == sorted(tetris.pieza_actual(juego))

def test_avanzar_consolida_la_superficie_al_llegar_al_fondo():
    siguiente_pieza = tetris.generar_pieza(pieza=tetris.T)
    juego = tetris.crear_juego(tetris.generar_pieza(tetris.L))

    llego_al_piso = False
    # Avanzar n veces hasta que la pieza L esté justo antes de tocar el piso
    for _ in range(tetris.ALTO_JUEGO):
        pieza_actual = tetris.pieza_actual(juego)
        if any(py == tetris.ALTO_JUEGO-1 for _, py in pieza_actual):
            llego_al_piso = True
            break

        juego, cambiar_pieza = tetris.avanzar(juego, siguiente_pieza)
        if cambiar_pieza == True: # Si se consolidó antes hay un bug.
            return False
    
    if not llego_al_piso:
        return False # Iteramos tetris.ALTO_JUEGO veces y la pieza nunca llegó al piso
    
    pieza_actual = tetris.pieza_actual(juego)
    juego, cambiar_pieza = tetris.avanzar(juego, siguiente_pieza)

    if not cambiar_pieza:
        return False # La pieza tenía que consolidarse y no lo hizo  

    # Debe haber superficie en todos los puntos que ocupaba la pieza actual antes de 
    # consolidarse.
    superficie = []
    for py in range(tetris.ALTO_JUEGO):
        for px in range(tetris.ANCHO_JUEGO):
            if tetris.hay_superficie(juego, px, py):
                superficie.append((px, py))
    
    return sorted(superficie) == sorted(pieza_actual)

def test_avanzar_cambia_pieza_actual_al_consolidar_superficie():
    siguiente_pieza = tetris.generar_pieza(pieza=tetris.T)
    juego = tetris.crear_juego(tetris.generar_pieza(tetris.L))

    llego_al_piso = False
    # Avanzar n veces hasta que la pieza L esté justo antes de tocar el piso
    for _ in range(tetris.ALTO_JUEGO):
        pieza_actual = tetris.pieza_actual(juego)
        if any(py == tetris.ALTO_JUEGO-1 for _, py in pieza_actual):
            llego_al_piso = True
            break

        juego, cambiar_pieza = tetris.avanzar(juego, siguiente_pieza)
        if cambiar_pieza == True: # Si se consolidó antes hay un bug.
            return False
    
    if not llego_al_piso:
        return False # Iteramos tetris.ALTO_JUEGO veces y la pieza nunca llegó al piso
    
    pieza_actual = tetris.pieza_actual(juego)
    juego, cambiar_pieza = tetris.avanzar(juego, siguiente_pieza)

    if not cambiar_pieza:
        return False # La pieza tenía que consolidarse y no lo hizo  
    
    pieza_centrada = tetris.trasladar_pieza(siguiente_pieza, tetris.ANCHO_JUEGO // 2, 0)
    return sorted(pieza_centrada) == sorted(tetris.pieza_actual(juego))

def test_juego_termina_si_no_se_puede_agregar_mas_piezas():
    pieza_i = tetris.generar_pieza(pieza=tetris.I)
    juego = tetris.crear_juego(pieza_i)

    # Está calculado que si tetris.ALTO_JUEGO es 18 se debe avanzar 35 veces
    # (incorporando únicamente nuevas piezas I) hasta perder el juego.
    for _ in range(35):
        juego, _ = tetris.avanzar(juego, pieza_i)
        if tetris.terminado(juego):
            return False # El juego se perdió antes
    
    juego, _ = tetris.avanzar(juego, pieza_i)
    return tetris.terminado(juego)

def test_juego_terminado_sigue_terminado_al_avanzar():
    pieza_i = tetris.generar_pieza(pieza=tetris.I)
    juego = tetris.crear_juego(pieza_i)

    for _ in range(35):
        juego, _ = tetris.avanzar(juego, pieza_i)
        if tetris.terminado(juego):
            return False # El juego se perdió antes
    
    ultimo_juego, _ = tetris.avanzar(juego, pieza_i)
    if not tetris.terminado(ultimo_juego):
        return False # El juego no terminó cuando debía
    
    for _ in range(10):
        if tetris.avanzar(ultimo_juego, pieza_i) != (ultimo_juego, False):
            return False
        
    return True

def _ubicar_piezas_I(juego, min_x, max_x, ultima_pieza):
    '''
    Función auxiliar para las pruebas
    Ubica piezas I en las columnas del rango [min_x, max_x).
    '''
    pieza_i = tetris.generar_pieza(pieza=tetris.I)
    piezas_siguientes = [pieza_i for x in range(min_x, max_x - 1)] + [ultima_pieza]
    for dx, proxima_pieza in zip(range(min_x, max_x), piezas_siguientes):
        # Mover dx veces
        for _ in range(abs(dx)):
            juego = tetris.mover(juego, IZQUIERDA if dx < 0 else DERECHA)
        
        # Bajar la pieza hasta consolidarla
        juego, cambiar_pieza = tetris.avanzar(juego, proxima_pieza)
        while not cambiar_pieza and not tetris.terminado(juego):
            juego, cambiar_pieza = tetris.avanzar(juego, proxima_pieza)
        
        if tetris.terminado(juego):
            return None
    
    return juego

def test_eliminar_todas_las_lineas():
    pieza_i = tetris.generar_pieza(pieza=tetris.I)
    juego = tetris.crear_juego(pieza_i)

    # Acomodar todas piezas I y verificar que se eliminan todas
    # las líneas
    juego = _ubicar_piezas_I(juego, -4, 5, pieza_i)
    
    if not juego: # El juego terminó antes de poder ubicar las I.
        return False

    # Revisar que no haya superficie en ningún lado
    ancho, alto = tetris.dimensiones(juego)
    for x in range(ancho):
        for y in range(alto):
            if tetris.hay_superficie(juego, x, y):
                return False
    
    return True

def test_eliminar_lineas_baja_las_lineas_superiores():
    pieza_i = tetris.generar_pieza(pieza=tetris.I)
    juego = tetris.crear_juego(pieza_i)

    # Generar esta superficie:
    #   T
    # T T T
    # I I I I I I I
    # I I I I I I I
    # I I I I I I I
    # I I I I I I I
    # 
    # Y verificar que al poner la última I queda así:
    #   T
    # T T T
    pieza_t = tetris.generar_pieza(pieza=tetris.T)
    juego = _ubicar_piezas_I(juego, -4, -1, pieza_t)
    if not juego:
        print('primer retu')
        return False
    
    # Ubicar la T
    for _ in range(4):
        juego = tetris.mover(juego, IZQUIERDA)
    
    # Bajar la T hasta consolidarla
    juego, cambiar_pieza = tetris.avanzar(juego, pieza_i)
    while not cambiar_pieza and not tetris.terminado(juego):
        juego, cambiar_pieza = tetris.avanzar(juego, pieza_i)
    
    if tetris.terminado(juego):
        print('segundo retu')
        return False

    # Ubicar el resto de las I
    juego = _ubicar_piezas_I(juego, -1, 5, pieza_i)
    if not juego:
        print('tercer retu')
        return False
    
    # Revisar que no haya superficie en ningún lado excepto en
    # donde está la T
    ancho, alto = tetris.dimensiones(juego)

    pieza_t = tetris.generar_pieza(pieza=tetris.T)
    pieza_t = tetris.trasladar_pieza(pieza_t, 0, alto - 2)
    print(alto)

    for x in range(ancho):
        for y in range(alto):
            if tetris.hay_superficie(juego, x, y) and not (x, y) in pieza_t:
                print(f'f en {(x, y)}')
    
                return False
    
    for x, y in pieza_t:
        if not tetris.hay_superficie(juego, x, y):
            print('no pieza t')
        
            return False
    
    return True

TESTS = (
    test_trasladar_pieza_al_0_0,
    test_trasladar_pieza,
    test_dimensiones_correctas,
    test_grilla_esta_vacia_al_iniciar,
    test_pieza_inicial_esta_arriba_en_el_medio_al_iniciar,
    test_juego_no_esta_terminado_al_iniciar,
    test_mover_pieza_l_a_derecha,
    test_mover_pieza_s_a_derecha,
    test_mover_pieza_t_a_izquierda,
    test_mover_pieza_i_a_izquierda,
    test_mover_l_contra_pared_derecha,
    test_mover_l_contra_pared_izquierda,
    test_avanzar_baja_la_pieza_una_posicion,
    test_avanzar_consolida_la_superficie_al_llegar_al_fondo,
    test_avanzar_cambia_pieza_actual_al_consolidar_superficie,
    test_juego_termina_si_no_se_puede_agregar_mas_piezas,
    test_juego_terminado_sigue_terminado_al_avanzar,
    test_eliminar_todas_las_lineas,
    test_eliminar_lineas_baja_las_lineas_superiores
)

COLOR_OK = '\033[1m\033[92m'
COLOR_ERR = '\033[1m\033[91m'
COLOR_RESET = '\033[0m'

def print_color(color: str, *args, **kwargs):
    if TERMINAL_SIN_COLOR:
        print(*args, **kwargs)
    else:
        print(color, end='')
        print(*args, **kwargs)
        print(COLOR_RESET, end='')

def main():
    test_fallido = False

    for i, test in enumerate(TESTS):
        print(f'Prueba {i + 1 :02} - {test.__name__}: ', end='', flush=True)
        if not test():
            test_fallido = True
            print_color(COLOR_ERR, '[ERROR]')
        else:
            print_color(COLOR_OK, '[OK]')
            
            
    if not test_fallido:
        print()
        print_color(COLOR_OK, '###########')
        print_color(COLOR_OK, '# TODO OK #')
        print_color(COLOR_OK, '###########')
        print()
    else:
        print()
        print_color(COLOR_ERR, '###########')
        print_color(COLOR_ERR, '# ¡ERROR! #')
        print_color(COLOR_ERR, '###########')
        print()

main()