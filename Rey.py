from Pieza import Pieza
from Config import *

class Rey(Pieza):
    def __init__(self, color, columna, fila):
        super().__init__(color, columna, fila)

    def dibujar(self, lienzo, es_seleccionada=False):
        # 1. Transformación de Coordenadas Lógicas a Píxeles (Mapping)
        x_pixel = self.col * TAMANO_CELDA
        y_pixel = self.fila * TAMANO_CELDA
        
        margen = 10 
        
        base_x1 = x_pixel + margen
        base_y1 = y_pixel + margen + 23 
        base_x2 = x_pixel + TAMANO_CELDA - margen
        base_y2 = y_pixel + TAMANO_CELDA - margen

        # Usamos los colores definidos en Config
        if self.color == "black":
            color_relleno = COLOR_PIEZA_NEGRA
            color_borde = COLOR_BORDE_NEGRO
        else:
            color_relleno = COLOR_PIEZA_BLANCA
            color_borde = COLOR_BORDE_BLANCO
        
        # Resaltado visual para la selección
        if es_seleccionada:
            color_borde = "red"
            # Creamos un rectángulo de resaltado detrás de la pieza
            lienzo.crear_rectangulo(x_pixel, y_pixel, 
                                    x_pixel + TAMANO_CELDA, y_pixel + TAMANO_CELDA, 
                                    "", "#00FF00") # Resaltado verde

        # DIBUJAR REY
        
        # 1. Base (Rectángulo)
        lienzo.crear_rectangulo(base_x1, base_y1, base_x2, base_y2, color_relleno, color_borde)

        # 2. Cuerpo (Más robusto)
        ancho_base = base_x2 - base_x1
        cuerpo_x1 = base_x1 + (ancho_base * 0.25)
        cuerpo_x2 = base_x2 - (ancho_base * 0.25)
        cuerpo_y1 = base_y1 - 9
        cuerpo_y2 = base_y1
        lienzo.crear_rectangulo(cuerpo_x1, cuerpo_y1, cuerpo_x2, cuerpo_y2, color_relleno, color_borde)
        
        # 3. Cabeza (Parte superior antes de la cruz)
        cabeza_x1 = base_x1 + (ancho_base * 0.3)
        cabeza_x2 = base_x2 - (ancho_base * 0.3)
        cabeza_y1 = cuerpo_y1 - 6
        cabeza_y2 = cuerpo_y1
        lienzo.crear_rectangulo(cabeza_x1, cabeza_y1, cabeza_x2, cabeza_y2, color_relleno, color_borde)

        # 4. Cruz (Característica del Rey)
        centro_x = x_pixel + (TAMANO_CELDA // 2)
        
        # Palo vertical
        cruz_ancho_v = 4
        cruz_alto_v = 12
        
        cruz_v_x1 = centro_x - (cruz_ancho_v // 2)
        cruz_v_x2 = centro_x + (cruz_ancho_v // 2)
        cruz_v_y1 = cabeza_y1 - cruz_alto_v
        cruz_v_y2 = cabeza_y1
        lienzo.crear_rectangulo(cruz_v_x1, cruz_v_y1, cruz_v_x2, cruz_v_y2, color_relleno, color_borde)
        
        # Palo horizontal
        cruz_ancho_h = 10
        cruz_alto_h = 4
        cruz_h_x1 = centro_x - (cruz_ancho_h // 2)
        cruz_h_x2 = centro_x + (cruz_ancho_h // 2)
        cruz_h_y1 = cruz_v_y1 + 3 # Cerca del top del palo vertical
        cruz_h_y2 = cruz_h_y1 + cruz_alto_h
        lienzo.crear_rectangulo(cruz_h_x1, cruz_h_y1, cruz_h_x2, cruz_h_y2, color_relleno, color_borde)
    
    def mover_a(self, nueva_col, nueva_fila):
        self.col = nueva_col
        self.fila = nueva_fila
    
    def es_movimiento_valido(self, nueva_col, nueva_fila, piezas):
        # Movimiento válido para rey: 1 casilla en cualquier dirección
        diff_col = abs(nueva_col - self.col)
        diff_fila = abs(nueva_fila - self.fila)
        
        # El rey se mueve máximo 1 casilla en cualquier eje, pero debe moverse al menos algo
        es_movimiento_un_paso = (max(diff_col, diff_fila) == 1)
        
        if not es_movimiento_un_paso:
            return False
            
        return self.camino_libre(nueva_col, nueva_fila, piezas) 
    
    def es_captura_valida(self, nueva_col, nueva_fila, piezas):
        # El Rey captura igual que se mueve: 1 casilla en cualquier dirección
        return self.es_movimiento_valido(nueva_col, nueva_fila, piezas)
            
    
    
