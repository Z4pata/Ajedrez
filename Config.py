CONSTANTES = {
    "ANCHO_TABLERO": 400,
    "ALTO_TABLERO": 450, # 50px extra para el letrero de turno
    "DIMENSION": 8  # 8x8 tablero
}

# Calculamos el tamaño de celda dinámicamente
TAMANO_CELDA = CONSTANTES["ANCHO_TABLERO"] // CONSTANTES["DIMENSION"]

# Colores (Paleta)
# Centralizar los colores permite cambiar el "tema" del juego fácilmente.
COLOR_CASILLA_CLARA = "#F0D9B5"
COLOR_CASILLA_OSCURA = "#B58863"
COLOR_PIEZA_NEGRA = "black"
COLOR_PIEZA_BLANCA = "white"
COLOR_BORDE_NEGRO = "white"
COLOR_BORDE_BLANCO = "black"