from Pieza import Pieza
from Config import *

class Torre(Pieza):
    def __init__(self, color, columna, fila):
        super().__init__(color, columna, fila)

    def dibujar(self, lienzo, es_seleccionada=False):
        # 1. Transformación de Coordenadas Lógicas a Píxeles (Mapping)
        x_pixel = self.col * TAMANO_CELDA
        y_pixel = self.fila * TAMANO_CELDA
        
        margen = 10 
        
        base_x1 = x_pixel + margen
        base_y1 = y_pixel + margen + 15 
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

        # DIBUJAR BASE
        lienzo.crear_rectangulo(base_x1, base_y1, base_x2, base_y2, color_relleno, color_borde)

        # DIBUJAR CACHOS
        ancho_cacho = (base_x2 - base_x1) / 5
        
        for i in range(3): 
            cacho_x1 = base_x1 + (i * 2 * ancho_cacho) 
            cacho_y1 = base_y1 - 10 
            cacho_x2 = cacho_x1 + ancho_cacho
            cacho_y2 = base_y1
            
            lienzo.crear_rectangulo(cacho_x1, cacho_y1, cacho_x2, cacho_y2, color_relleno, color_borde)
    
    def mover_a(self, nueva_col, nueva_fila):
        self.col = nueva_col
        self.fila = nueva_fila
    
    def es_movimiento_valido(self, nueva_col, nueva_fila):
        # Movimiento válido para torre: misma columna o misma fila
        return (self.col == nueva_col) or (self.fila == nueva_fila)
    
    def es_captura_valida(self, nueva_col, nueva_fila):
        # Movimiento válido para torre: misma columna o misma fila
        return (self.col == nueva_col) or (self.fila == nueva_fila)
    
    
