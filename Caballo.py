from Pieza import Pieza
from Config import *

class Caballo(Pieza):
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

        # DIBUJAR CABALLO (POLÍGONO)
        
        # Puntos clave relativos a la celda
        # x_pixel, y_pixel es la esquina superior izquierda de la celda
        # Ancho y alto de celda es TAMANO_CELDA
        
        # Coordenadas aproximadas para una silueta de caballo mirando a la izquierda
        # Puntos en orden (horario o antihorario):
        
        cx = x_pixel + TAMANO_CELDA // 2  # Centro X
        cy = y_pixel + TAMANO_CELDA // 2  # Centro Y
        
        puntos = [
            x_pixel + 10, y_pixel + 40,   # Base izquierda abajo
            x_pixel + 40, y_pixel + 40,   # Base derecha abajo
            x_pixel + 35, y_pixel + 30,   # Base derecha arriba (inicio cuello trasero)
            x_pixel + 35, y_pixel + 20,   # Cuello trasero
            x_pixel + 28, y_pixel + 10,   # Cabeza atrás (oreja)
            x_pixel + 20, y_pixel + 10,   # Cabeza arriba
            x_pixel + 10, y_pixel + 18,   # Hocico punta
            x_pixel + 15, y_pixel + 25,   # Barbilla
            x_pixel + 20, y_pixel + 30,   # Cuello delantero base
            x_pixel + 15, y_pixel + 30,   # Base izquierda arriba
        ]
        
        # Dibujamos el polígono del cuerpo
        lienzo.crear_poligono(puntos, color_relleno, color_borde)
        
        # OJO
        ojo_x = x_pixel + 20
        ojo_y = y_pixel + 15
        color_ojo = "white" if self.color == "black" else "black"
        lienzo.crear_circulo(ojo_x, ojo_y, 2, color_ojo, color_ojo)
    
    def mover_a(self, nueva_col, nueva_fila):
        self.col = nueva_col
        self.fila = nueva_fila
    
    def es_movimiento_valido(self, nueva_col, nueva_fila, piezas):
        # Movimiento válido para caballo: movimiento en L
        diff_col = abs(nueva_col - self.col)
        diff_fila = abs(nueva_fila - self.fila)
        
        # (1 horizontal y 2 vertical) O (2 horizontal y 1 vertical)
        return (diff_col == 1 and diff_fila == 2) or (diff_col == 2 and diff_fila == 1)
    
    def es_captura_valida(self, nueva_col, nueva_fila, piezas):
        # El caballo captura igual que se mueve y salta piezas
        return self.es_movimiento_valido(nueva_col, nueva_fila, piezas)
            
    
    
