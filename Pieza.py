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

    @abstractmethod
    def es_movimiento_valido(self, nueva_col, nueva_fila, piezas=None):
        pass

    @abstractmethod
    def es_captura_valida(self, nueva_col, nueva_fila, piezas=None):
        pass

    def camino_libre(self, nueva_col, nueva_fila, piezas):
        """
        Verifica genéricamente si hay piezas en la trayectoria lineal o diagonal
        entre la posición actual y la destino (excluyendo inicio y fin).
        Útil para Torre, Alfil y Reina.
        """
        d_col = 0
        d_fila = 0
        
        # Determinar dirección del paso (-1, 0, o 1)
        if nueva_col > self.col: d_col = 1
        elif nueva_col < self.col: d_col = -1
        
        if nueva_fila > self.fila: d_fila = 1
        elif nueva_fila < self.fila: d_fila = -1
        
        curr_col = self.col + d_col
        curr_fila = self.fila + d_fila
        
        # Iterar mientras no lleguemos a la casilla destino
        while (curr_col != nueva_col) or (curr_fila != nueva_fila):
            if self.hay_pieza(curr_col, curr_fila, piezas):
                return False
            curr_col += d_col
            curr_fila += d_fila
            
        return True

    def hay_pieza(self, col, fila, piezas):
        for p in piezas:
            if p.col == col and p.fila == fila:
                return True
        return False