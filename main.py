from Lienzo import Lienzo
from Torre import Torre
from Config import *

PIEZAS = [] 
PIEZA_SELECCIONADA = None
LIENZO_GLOBAL = None

def main():
    global LIENZO_GLOBAL
    lienzo = Lienzo(CONSTANTES["ANCHO_TABLERO"], CONSTANTES["ALTO_TABLERO"])

    LIENZO_GLOBAL = lienzo
    
    crear_tablero(lienzo)
    
    # Crear torre negra en a8 (columna 0, fila 0)
    torre_negra1 = Torre(COLOR_PIEZA_NEGRA, 0, 0)
    torre_negra2 = Torre(COLOR_PIEZA_NEGRA, 7, 0)
    

    # Crear torre blanca en h1 (columna 7, fila 7) para probar
    torre_blanca1 = Torre(COLOR_PIEZA_BLANCA, 0, 7)
    torre_blanca2 = Torre(COLOR_PIEZA_BLANCA, 7, 7)
    
    PIEZAS.append(torre_negra1)
    PIEZAS.append(torre_negra2)
    PIEZAS.append(torre_blanca1)
    PIEZAS.append(torre_blanca2)
    
    lienzo.vincular_click(manejar_click)

    actualizar_lienzo(lienzo)

    lienzo.esperar_cierre()




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

def dibujar_piezas(lienzo):
    """Dibuja todas las piezas, incluyendo el estado de selección."""
    for pieza in PIEZAS:
        # Pasa True al método dibujar si la pieza es la seleccionada
        es_seleccionada = (pieza == PIEZA_SELECCIONADA)
        pieza.dibujar(lienzo, es_seleccionada)

def actualizar_lienzo(lienzo):
    """
    Función de control que gestiona la actualización de la interfaz gráfica.
    Patrón: Clear and Redraw.
    """
    lienzo.limpiar()
    crear_tablero(lienzo)
    dibujar_piezas(lienzo)

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

def manejar_click(evento):
    """
    [CONTROLADOR] Gestiona el flujo de movimiento con clicks.
    """
    global PIEZA_SELECCIONADA, LIENZO_GLOBAL
    
    col_click, fila_click = mapear_pixel_a_logico(evento.x, evento.y)

    print(f"Click en la casilla: ({col_click}, {fila_click})")

    pieza_en_casilla = obtener_pieza(col_click, fila_click)

    # === Lógica de la Máquina de Estados ===

    if PIEZA_SELECCIONADA is None:
        # ESTADO 1: Seleccionar Pieza
        if pieza_en_casilla:
            PIEZA_SELECCIONADA = pieza_en_casilla
            print(f"Pieza seleccionada: {PIEZA_SELECCIONADA.color} Torre")
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
                if PIEZA_SELECCIONADA.es_movimiento_valido(col_click, fila_click):
                    print(f"¡Captura! {PIEZA_SELECCIONADA.color} captura a {pieza_en_casilla.color}")
                    PIEZAS.remove(pieza_en_casilla)
                    PIEZA_SELECCIONADA.mover_a(col_click, fila_click)
                    PIEZA_SELECCIONADA = None
                else:
                    print("Movimiento de captura inválido para la Torre.")
        
        else:
            # Caso 2b: Click en casilla vacía (Movimiento de la Pieza)
            
            # TODO: Aquí iría la lógica avanzada de validación de Ajedrez
            # if PIEZA_SELECCIONADA.es_movimiento_valido(col_click, fila_click):
            
            # [Lógica del Negocio] Mover la pieza
            if not PIEZA_SELECCIONADA.es_movimiento_valido(col_click, fila_click):
                print("Movimiento inválido para la Torre.")
                return
            
            PIEZA_SELECCIONADA.mover_a(col_click, fila_click)
            print(f"Movida Torre a: ({col_click}, {fila_click})")
            
            # Volver al Estado 1
            PIEZA_SELECCIONADA = None

    # [Lógica de Presentación] Actualizar la GUI después de cada acción
    actualizar_lienzo(LIENZO_GLOBAL)


if __name__ == '__main__':
    main()