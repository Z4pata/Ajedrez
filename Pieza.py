from abc import ABC, abstractmethod

class Pieza:
    def __init__(self, color, columna, fila):
        self.color = color
        # Guardamos coordenadas lógicas (ej: 0,0 para a8), no píxeles
        self.col = columna 
        self.fila = fila        # Coordenada y en el tablero
    
    @abstractmethod
    def mover_a(self, nueva_col, nueva_fila):
        pass
    
    @abstractmethod
    def dibujar(self, lienzo, es_seleccionada=False):
        pass