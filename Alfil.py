from Pieza import Pieza
from Config import *

class Alfil(Pieza):
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

        # DIBUJAR CUERPO (Delgado y alto)
        ancho_base = base_x2 - base_x1
        cuerpo_x1 = base_x1 + (ancho_base * 0.35)
        cuerpo_x2 = base_x2 - (ancho_base * 0.35)
        cuerpo_y1 = base_y1 - 18 
        cuerpo_y2 = base_y1
        lienzo.crear_rectangulo(cuerpo_x1, cuerpo_y1, cuerpo_x2, cuerpo_y2, color_relleno, color_borde)

        # DIBUJAR CABEZA (Círculo grande)
        centro_x = x_pixel + (TAMANO_CELDA // 2)
        radio = (ancho_base * 0.25) 
        centro_y = cuerpo_y1 
        
        lienzo.crear_circulo(centro_x, centro_y, radio, color_relleno, color_borde)

        # DIBUJAR DETALLE SUPERIOR (Círculo pequeño)
        radio_detalle = radio * 0.4
        centro_y_detalle = centro_y - radio 
        lienzo.crear_circulo(centro_x, centro_y_detalle, radio_detalle, color_relleno, color_borde)
    
    def mover_a(self, nueva_col, nueva_fila):
        self.col = nueva_col
        self.fila = nueva_fila
    
    def es_movimiento_valido(self, nueva_col, nueva_fila, piezas):
        # 1. Geometría: Diagonal
        diff_col = abs(nueva_col - self.col)
        diff_fila = abs(nueva_fila - self.fila)
        
        if diff_col != diff_fila:
            return False
            
        # 2. Trayectoria: No saltar piezas
        return self.camino_libre(nueva_col, nueva_fila, piezas)
    
    
    def es_captura_valida(self, nueva_col, nueva_fila, piezas):
        # Igual al movimiento normal para el Alfil
        return self.es_movimiento_valido(nueva_col, nueva_fila, piezas)
            
    
    
