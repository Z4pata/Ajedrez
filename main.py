from Lienzo import Lienzo
from Torre import Torre
from Peon import Peon
from Alfil import Alfil
from Caballo import Caballo
from Reina import Reina
from Rey import Rey
from Config import *

PIEZAS = [] 
PIEZA_SELECCIONADA = None
LIENZO_GLOBAL = None
TURNO = COLOR_PIEZA_BLANCA

def main():
    global LIENZO_GLOBAL, TURNO
    lienzo = Lienzo(CONSTANTES["ANCHO_TABLERO"], CONSTANTES["ALTO_TABLERO"])

    LIENZO_GLOBAL = lienzo
    
    iniciar_juego()
    
    lienzo.vincular_click(manejar_click)
    
    # Crear botón de reinicio
    def accion_reiniciar():
        iniciar_juego()
        
    lienzo.crear_boton("Reiniciar", accion_reiniciar)

    actualizar_lienzo(lienzo)

    lienzo.esperar_cierre()

def iniciar_juego():
    """Inicia el tablero y las variables de estado desde cero"""
    global PIEZAS, PIEZA_SELECCIONADA, TURNO
    PIEZAS = []
    PIEZA_SELECCIONADA = None
    TURNO = COLOR_PIEZA_BLANCA
    
    # Crear torres negras iniciales
    torre_negra1 = Torre(COLOR_PIEZA_NEGRA, 0, 0)
    torre_negra2 = Torre(COLOR_PIEZA_NEGRA, 7, 0)
    alfil_negra1 = Alfil(COLOR_PIEZA_NEGRA, 2, 0)
    alfil_negra2 = Alfil(COLOR_PIEZA_NEGRA, 5, 0)
    caballo_negra1 = Caballo(COLOR_PIEZA_NEGRA, 1, 0)
    caballo_negra2 = Caballo(COLOR_PIEZA_NEGRA, 6, 0)
    reina_negra = Reina(COLOR_PIEZA_NEGRA, 3, 0)
    rey_negra = Rey(COLOR_PIEZA_NEGRA, 4, 0)
    
    # Crear torres blancas iniciales
    torre_blanca1 = Torre(COLOR_PIEZA_BLANCA, 0, 7)
    torre_blanca2 = Torre(COLOR_PIEZA_BLANCA, 7, 7)
    alfil_blanca1 = Alfil(COLOR_PIEZA_BLANCA, 2, 7)
    alfil_blanca2 = Alfil(COLOR_PIEZA_BLANCA, 5, 7)
    caballo_blanca1 = Caballo(COLOR_PIEZA_BLANCA, 1, 7)
    caballo_blanca2 = Caballo(COLOR_PIEZA_BLANCA, 6, 7)
    reina_blanca = Reina(COLOR_PIEZA_BLANCA, 3, 7)
    rey_blanca = Rey(COLOR_PIEZA_BLANCA, 4, 7)
    
    # Agregar piezas al tablero
    # NEGRAS
    agregar_peones(COLOR_PIEZA_NEGRA)
    PIEZAS.append(torre_negra1)
    PIEZAS.append(torre_negra2)
    PIEZAS.append(alfil_negra1)
    PIEZAS.append(alfil_negra2)
    PIEZAS.append(caballo_negra1)
    PIEZAS.append(caballo_negra2)
    PIEZAS.append(reina_negra)
    PIEZAS.append(rey_negra)
    
    
    # BLANCAS
    agregar_peones(COLOR_PIEZA_BLANCA)
    PIEZAS.append(torre_blanca1)
    PIEZAS.append(torre_blanca2)
    PIEZAS.append(alfil_blanca1)
    PIEZAS.append(alfil_blanca2)
    PIEZAS.append(caballo_blanca1)
    PIEZAS.append(caballo_blanca2)
    PIEZAS.append(reina_blanca)
    PIEZAS.append(rey_blanca)
    
    if LIENZO_GLOBAL:
        actualizar_lienzo(LIENZO_GLOBAL)


def crear_tablero(lienzo):
    for fila in range(8):
        for col in range(8):
            x1 = col * TAMANO_CELDA
            y1 = fila * TAMANO_CELDA
            x2 = x1 + TAMANO_CELDA
            y2 = y1 + TAMANO_CELDA
            
            # Lógica de color alternado (par + impar = negro)
            es_blanco = (fila + col) % 2 == 0
            color = COLOR_CASILLA_CLARA if es_blanco else COLOR_CASILLA_OSCURA # Colores clásicos de ajedrez
            
            lienzo.crear_rectangulo(x1, y1, x2, y2, color, "black")
    

def agregar_peones(color):
    for i in range(8):
        if color == COLOR_PIEZA_NEGRA:
            fila = 1
        else:
            fila = 6
        peon_negro = Peon(color, i, fila)
        PIEZAS.append(peon_negro)

def dibujar_piezas(lienzo):
    """Dibuja todas las piezas, incluyendo el estado de selección."""
    for pieza in PIEZAS:
        # Pasa True al método dibujar si la pieza es la seleccionada
        es_seleccionada = (pieza == PIEZA_SELECCIONADA)
        pieza.dibujar(lienzo, es_seleccionada)

def dibujar_turno(lienzo):
    """Dibuja un letrero indicando de quién es el turno."""
    turno = "BLANCO" if TURNO == COLOR_PIEZA_BLANCA else "NEGRO"
    texto = f"Turno: {turno}"
    color_texto = "black"
    
    # Dibujar en la zona inferior
    # Usamos ANCHO_TABLERO / 2 para centrar horizontalmente
    x = CONSTANTES["ANCHO_TABLERO"] // 2
    y = CONSTANTES["ALTO_TABLERO"] - 25
    
    lienzo.crear_texto(x, y, texto, color_texto, fuente=("Arial", 16, "bold"))

def actualizar_lienzo(lienzo):
    """
    Función de control que gestiona la actualización de la interfaz gráfica.
    """
    lienzo.limpiar()
    crear_tablero(lienzo)
    dibujar_piezas(lienzo)
    dibujar_turno(lienzo)

def obtener_pieza(col, fila):
    """Devuelve la pieza en una coordenada lógica dada, o None."""
    for pieza in PIEZAS:
        if pieza.col == col and pieza.fila == fila:
            return pieza
    return None

def mapear_pixel_a_logico(x_pixel, y_pixel):
    """
    Convierte coordenadas de píxel a coordenadas lógicas del tablero.
    """
    col = x_pixel // TAMANO_CELDA
    fila = y_pixel // TAMANO_CELDA
    return col, fila

def obtener_rey(color):
    """Devuelve la instancia del Rey del color especificado."""
    for pieza in PIEZAS:
        if isinstance(pieza, Rey) and pieza.color == color:
            return pieza
    return None

def esta_en_jaque(color, piezas_tablero):
    """
    Verifica si el Rey del color dado está siendo atacado por alguna pieza enemiga.
    """
    rey = obtener_rey(color)
    if not rey: return False
    
    color_enemigo = COLOR_PIEZA_BLANCA if color == COLOR_PIEZA_NEGRA else COLOR_PIEZA_NEGRA
    
    for pieza in piezas_tablero:
        if pieza.color == color_enemigo:
            # Verificar si esta pieza enemiga puede capturar al rey
            if pieza.es_captura_valida(rey.col, rey.fila, piezas_tablero):
                return True
    return False

def es_jaque_mate(color, piezas_tablero):
    """
    Determina si el color está en Jaque Mate.
    Condición: Está en Jaque Y no tiene movimientos legales para salir de él.
    """
    if not esta_en_jaque(color, piezas_tablero):
        return False
    
    # Si está en jaque, verificamos si tiene alguna salvación
    if tiene_movimientos_validos(color, piezas_tablero):
        return False
    
    return True

def tiene_movimientos_validos(color, piezas_tablero):
    """
    Verifica si existe AL MENOS UN movimiento legal para cualquier pieza del color dado.
    Fuerza bruta optimizada: Probamos mover cada pieza a cada casilla.
    """
    # Filtramos las piezas del color
    piezas_propias = [p for p in piezas_tablero if p.color == color]
    
    for pieza in piezas_propias:
        # Probamos mover a todas las casillas del tablero (0..7, 0..7)
        for fila in range(8):
            for col in range(8):
                # 1. ¿Es un movimiento geométricamente válido?
                # Nota: Para simplificar la verificación de captura vs movimiento,
                # podemos chequear ambos. Si hay pieza enemiga es captura, si no es movimiento.
                
                es_valido = False
                pieza_destino = obtener_pieza(col, fila) # Ojo: esto usa PIEZAS global, cuidado
                
                # Casilla vacía -> Movimiento
                if pieza_destino is None:
                    if pieza.es_movimiento_valido(col, fila, piezas_tablero):
                        es_valido = True
                # Casilla enemiga -> Captura
                elif pieza_destino.color != color:
                    if pieza.es_captura_valida(col, fila, piezas_tablero):
                        es_valido = True
                
                if es_valido:
                    # 2. ¿Evita el jaque?
                    if not movimiento_deja_en_jaque(pieza, col, fila, pieza_destino):
                        return True # Encontramos una salvación!
                        
    return False # No se encontró ningún movimiento salvador

def movimiento_deja_en_jaque(pieza_a_mover, col_destino, fila_destino, pieza_capturada=None):
    """
    Simula un movimiento para ver si deja al propio Rey en jaque.
    Retorna True si el movimiento es ILEGAL (deja en jaque).
    """
    # 1. Guardar estado original
    col_origen = pieza_a_mover.col
    fila_origen = pieza_a_mover.fila
    
    # 2. Simular movimiento
    pieza_a_mover.col = col_destino
    pieza_a_mover.fila = fila_destino
    
    if pieza_capturada:
        PIEZAS.remove(pieza_capturada)
        
    # 3. Verificar Jaque
    en_jaque = esta_en_jaque(pieza_a_mover.color, PIEZAS)
    
    # 4. Restaurar estado
    pieza_a_mover.col = col_origen
    pieza_a_mover.fila = fila_origen
    
    if pieza_capturada:
        PIEZAS.append(pieza_capturada)
        
    return en_jaque

def manejar_click(evento):
    """
    [CONTROLADOR] Gestiona el flujo de movimiento con clicks.
    """
    global PIEZA_SELECCIONADA, TURNO, LIENZO_GLOBAL
    
    col_click, fila_click = mapear_pixel_a_logico(evento.x, evento.y)

    print(f"Click en la casilla: ({col_click}, {fila_click})")

    pieza_en_casilla = obtener_pieza(col_click, fila_click)

    # === Lógica de la Máquina de Estados ===

    if PIEZA_SELECCIONADA is None:
        # ESTADO 1: Seleccionar Pieza
        if pieza_en_casilla:
            PIEZA_SELECCIONADA = pieza_en_casilla
            print(f"Pieza seleccionada: {PIEZA_SELECCIONADA.color}")
        else:
            print("Casilla vacía. No hay pieza para seleccionar.")
    
    else:
        # ESTADO 2: Seleccionar Destino
        if PIEZA_SELECCIONADA == pieza_en_casilla:
            # Deselección: click en la misma pieza
            PIEZA_SELECCIONADA = None
            print("Pieza deseleccionada.")
        
        elif pieza_en_casilla:
            # Caso 2a: Click en una pieza diferente (captura o re-selección)
            if PIEZA_SELECCIONADA.color == pieza_en_casilla.color:
                # Mismo color: Re-seleccionar
                PIEZA_SELECCIONADA = pieza_en_casilla
                print(f"Pieza re-seleccionada: {PIEZA_SELECCIONADA.color}")
            else:
                # Diferente color: Intentar Captura
                if PIEZA_SELECCIONADA.es_captura_valida(col_click, fila_click, PIEZAS):
                    # VALIDAR SI DEJA EN JAQUE AL PROPIO REY
                    if movimiento_deja_en_jaque(PIEZA_SELECCIONADA, col_click, fila_click, pieza_en_casilla):
                        print("¡Movimiento ilegal! Dejaría al rey en jaque.")
                        return
                    
                    if TURNO != PIEZA_SELECCIONADA.color:
                        print("¡Movimiento ilegal! No es tu turno.")
                        return
                    
                    if isinstance(pieza_en_casilla, Rey):
                        print("¡Movimiento ilegal! No puedes capturar al rey.")
                        return

                    print(f"¡Captura! {PIEZA_SELECCIONADA.color} captura a {pieza_en_casilla.color}")
                    PIEZAS.remove(pieza_en_casilla)
                    PIEZA_SELECCIONADA.mover_a(col_click, fila_click)
                    
                    # Verificar si pusimos en jaque al enemigo
                    if esta_en_jaque(pieza_en_casilla.color, PIEZAS):
                        if es_jaque_mate(pieza_en_casilla.color, PIEZAS):
                            mensaje = f"¡JAQUE MATE! Ganan {PIEZA_SELECCIONADA.color}"
                            print(mensaje)
                            actualizar_lienzo(LIENZO_GLOBAL)
                            LIENZO_GLOBAL.mostrar_aviso("Fin del Juego", mensaje)
                        else:
                            print("¡JAQUE!")

                    # Limpiar la selección
                    PIEZA_SELECCIONADA = None

                    # Cambiar de turno
                    TURNO = COLOR_PIEZA_BLANCA if TURNO == COLOR_PIEZA_NEGRA else COLOR_PIEZA_NEGRA
                else:
                    print("Movimiento de captura inválido.")
        
        else:
            # Caso 2b: Click en casilla vacía (Movimiento de la Pieza)
            
            # Validar movimiento
            if not PIEZA_SELECCIONADA.es_movimiento_valido(col_click, fila_click, PIEZAS):
                print("Movimiento inválido")
                return
            
            # Validar turno
            if TURNO != PIEZA_SELECCIONADA.color:
                print("¡Movimiento ilegal! No es tu turno.")
                return
            
            # VALIDAR SI DEJA EN JAQUE AL PROPIO REY
            if movimiento_deja_en_jaque(PIEZA_SELECCIONADA, col_click, fila_click):
                print("¡Movimiento ilegal! Dejaría al rey en jaque.")
                return
            

            # Mover la pieza
            PIEZA_SELECCIONADA.mover_a(col_click, fila_click)
            print(f"Movida {PIEZA_SELECCIONADA.color} a: ({col_click}, {fila_click})")
            
            # Verificar si pusimos en jaque al enemigo
            color_enemigo = COLOR_PIEZA_BLANCA if PIEZA_SELECCIONADA.color == COLOR_PIEZA_NEGRA else COLOR_PIEZA_NEGRA
            if esta_en_jaque(color_enemigo, PIEZAS):
                if es_jaque_mate(color_enemigo, PIEZAS):
                    mensaje = f"¡JAQUE MATE! Ganan {PIEZA_SELECCIONADA.color}"
                    print(mensaje)
                    # Actualizar GUI antes del aviso para ver el mate
                    actualizar_lienzo(LIENZO_GLOBAL)
                    LIENZO_GLOBAL.mostrar_aviso("Fin del Juego", mensaje)
                else:
                    print("¡JAQUE!")

            # Limpiar la selección
            PIEZA_SELECCIONADA = None

            # Cambiar de turno
            TURNO = COLOR_PIEZA_BLANCA if TURNO == COLOR_PIEZA_NEGRA else COLOR_PIEZA_NEGRA

    # Actualizar el tablero
    actualizar_lienzo(LIENZO_GLOBAL)


if __name__ == '__main__':
    main()