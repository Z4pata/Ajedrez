import tkinter as tk

class Lienzo:
    def __init__(self, ancho, alto):
        self.root = tk.Tk()
        self.root.title("Ajedrez Python - Interactivo con Clicks")
        self.canvas = tk.Canvas(self.root, width=ancho, height=alto, bg="white")
        self.canvas.pack()
    
    def crear_rectangulo(self, x1, y1, x2, y2, color_relleno, color_borde):      
        self.canvas.create_rectangle(x1, y1, x2, y2, fill=color_relleno, outline=color_borde)

    def crear_circulo(self, x, y, radio, color_relleno, color_borde):
        self.canvas.create_oval(x - radio, y - radio, x + radio, y + radio, fill=color_relleno, outline=color_borde)

    def limpiar(self):
        """Método clave para borrar todos los elementos dibujados en el lienzo."""
        self.canvas.delete("all")

    def vincular_click(self, handler):
        """Vincula el evento de click (Boton 1) a la función de manejo."""
        self.canvas.bind("<Button-1>", handler)

    def esperar_cierre(self):
        self.root.mainloop()