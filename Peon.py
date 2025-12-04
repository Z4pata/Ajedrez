from Pieza import Pieza
from Config import *

class Peon(Pieza):
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

        # DIBUJAR CABEZA (usando circulo)
        centro_x = x_pixel + (TAMANO_CELDA // 2)
        # El radio será un cuarto del ancho de la celda aprox
        radio = (base_x2 - base_x1) // 3
        
        # La cabeza va encima de la base (base_y1 es el top de la base)
        centro_y = base_y1 - (radio // 2)

        lienzo.crear_circulo(centro_x, centro_y, radio, color_relleno, color_borde)
    
    def mover_a(self, nueva_col, nueva_fila):
        self.col = nueva_col
        self.fila = nueva_fila
    
    def es_movimiento_valido(self, nueva_col, nueva_fila):
        # Movimiento válido para peon: 1 casilla al frente en la misma columna
        if self.color == COLOR_PIEZA_NEGRA:
            # Negras bajan (fila aumenta)
            return (self.col == nueva_col) and (nueva_fila == self.fila + 1)
        else:
            # Blancas suben (fila disminuye)
            return (self.col == nueva_col) and (nueva_fila == self.fila - 1)
    
    def es_captura_valida(self, nueva_col, nueva_fila):
        # Captura válida: 1 casilla en diagonal hacia el frente
        diferencia_col = abs(nueva_col - self.col)
        
        if self.color == COLOR_PIEZA_NEGRA:
            return (diferencia_col == 1) and (nueva_fila == self.fila + 1)
        else:
            return (diferencia_col == 1) and (nueva_fila == self.fila - 1)
            
    
    
