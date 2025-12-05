from Pieza import Pieza
from Config import *

class Reina(Pieza):
    def __init__(self, color, columna, fila):
        super().__init__(color, columna, fila)

    def dibujar(self, lienzo, es_seleccionada=False):
        # 1. Transformación de Coordenadas Lógicas a Píxeles (Mapping)
        x_pixel = self.col * TAMANO_CELDA
        y_pixel = self.fila * TAMANO_CELDA
        
        margen = 10 
        base_y1 = y_pixel + margen + 25 
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

        # DIBUJAR REINA
        
        # Ajustamos los márgenes específicamente para la Reina para hacerla más esbelta
        margen_reina = 14 
        base_x1_reina = x_pixel + margen_reina
        base_x2_reina = x_pixel + TAMANO_CELDA - margen_reina
        
        # 1. Base (Rectángulo)
        # Usamos base_y1 y base_y2 originales para mantener la altura en el suelo
        lienzo.crear_rectangulo(base_x1_reina, base_y1, base_x2_reina, base_y2, color_relleno, color_borde)

        # 2. Cuerpo (Vestido/Trapecio invertido)
        # Recalculamos ancho base con las nuevas coordenadas
        ancho_base = base_x2_reina - base_x1_reina
        cuerpo_x1_base = base_x1_reina + (ancho_base * 0.2)
        cuerpo_x2_base = base_x2_reina - (ancho_base * 0.2)
        cuerpo_y_base = base_y1
        
        cuerpo_x1_top = base_x1_reina + (ancho_base * 0.1)
        cuerpo_x2_top = base_x2_reina - (ancho_base * 0.1)
        cuerpo_y_top = base_y1 - 20 # Reducimos la altura para que quepa mejor (era 25)

        puntos_cuerpo = [
            cuerpo_x1_base, cuerpo_y_base,
            cuerpo_x2_base, cuerpo_y_base,
            cuerpo_x2_top, cuerpo_y_top,
            cuerpo_x1_top, cuerpo_y_top
        ]
        lienzo.crear_poligono(puntos_cuerpo, color_relleno, color_borde)

        # 3. Corona (Picos)
        # Dibujamos una serie de triángulos o un polígono dentado encima del cuerpo
        ancho_corona = cuerpo_x2_top - cuerpo_x1_top
        paso = ancho_corona / 4
        
        puntos_corona = [cuerpo_x1_top, cuerpo_y_top] # Empezar izq abajo
        
        # 3 picos
        for i in range(3):
            x_pico = cuerpo_x1_top + (paso * (i + 0.5)) + (paso/2)
            y_pico = cuerpo_y_top - 8 # Altura del pico reducida (era 10)
            if i == 1: y_pico -= 4 # Pico central (era 5 extra)
            
            x_valle = cuerpo_x1_top + (paso * (i + 1))
            y_valle = cuerpo_y_top
            
            puntos_corona.append(x_pico)
            puntos_corona.append(y_pico)
            puntos_corona.append(x_valle)
            puntos_corona.append(y_valle)
            
            # Adorno en la punta del pico (joya)
            lienzo.crear_circulo(x_pico, y_pico, 2, color_relleno, color_borde)

        puntos_corona.append(cuerpo_x2_top)
        puntos_corona.append(cuerpo_y_top)
        
        lienzo.crear_poligono(puntos_corona, color_relleno, color_borde)
    
    def mover_a(self, nueva_col, nueva_fila):
        self.col = nueva_col
        self.fila = nueva_fila
    
    def es_movimiento_valido(self, nueva_col, nueva_fila, piezas):

        diff_col = abs(nueva_col - self.col)
        diff_fila = abs(nueva_fila - self.fila)
        
        # Misma columna, misma fila O diagonal (Alfil)
        es_lineal = (self.col == nueva_col) or (self.fila == nueva_fila)
        es_diagonal = (diff_col == diff_fila)
        
        if not (es_lineal or es_diagonal):
            return False
        
        # Trayectoria: No saltar piezas (heredado)
        return self.camino_libre(nueva_col, nueva_fila, piezas)
    
    def es_captura_valida(self, nueva_col, nueva_fila, piezas):
        # La captura de la Reina sigue las mismas reglas de movimiento
        return self.es_movimiento_valido(nueva_col, nueva_fila, piezas)
    
    
