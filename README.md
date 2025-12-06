# ♟️ Ajedrez en Python

Un motor de ajedrez completo e interactivo desarrollado en Python utilizando la biblioteca gráfica **Tkinter**. Este proyecto implementa las reglas fundamentales del ajedrez, incluyendo movimiento de piezas, validación de jugadas, sistema de turnos y detección de Jaque y Jaque Mate.

Este proyecto forma parte de mi portafolio de desarrollo de software, demostrando habilidades en **Programación Orientada a Objetos (POO)**, lógica de algoritmos y diseño de interfaces gráficas de escritorio.

## ✨ Características

*   **Tablero Gráfico Interactivo**: Interfaz limpia dibujada con primitivas de Tkinter.
*   **Piezas Personalizadas**: Cada pieza (Peón, Torre, Caballo, Alfil, Reina, Rey) tiene su propia clase y representación visual única dibujada mediante código (sin imágenes externas).
*   **Validación de Movimientos**: Reglas de movimiento específicas para cada tipo de pieza.
    *   *Caballo*: Movimiento en "L" y salto de piezas.
    *   *Peón*: Avance simple, doble paso inicial y captura diagonal.
    *   *Torre/Alfil/Reina*: Movimientos lineales y diagonales con detección de colisiones.
    *   *Rey*: Movimiento en cualquier dirección.
*   **Sistema de Turnos**: Control estricto de turnos (Blancas vs Negras) con indicador visual en pantalla.
*   **Motor de Reglas Avanzado**:
    *   **Detección de Jaque**: Identifica cuando el Rey está bajo amenaza.
    *   **Prevención de Movimientos Ilegales**: Impide cualquier movimiento que deje al propio Rey en Jaque.
    *   **Detección de Jaque Mate**: Anuncia el fin del juego cuando un jugador no tiene movimientos legales para salvar a su Rey.

## 🛠️ Tecnologías Utilizadas

*   **Lenguaje**: Python 3.12+
*   **GUI**: Tkinter (Biblioteca estándar de Python)
*   **Paradigma**: Programación Orientada a Objetos (POO)

## 📂 Estructura del Proyecto

El código está organizado modularmente para facilitar la mantenibilidad y escalabilidad:

*   `main.py`: Punto de entrada, controlador principal del juego y bucle de eventos.
*   `Lienzo.py`: Abstracción de la capa gráfica (Tkinter) para dibujar formas y manejar eventos.
*   `Config.py`: Configuraciones globales (colores, dimensiones del tablero).
*   `Pieza.py`: Clase padre abstracta que define la interfaz común para todas las piezas.
*   `[Torre|Caballo|Alfil|Rey|Reina|Peon].py`: Clases concretas con la lógica de movimiento y dibujo de cada pieza.

## 🚀 Instalación y Ejecución

Sigue estos pasos para probar el proyecto en tu máquina local:

### 1. Prerrequisitos
Asegúrate de tener **Python 3.x** instalado en tu sistema. Puedes verificarlo con:
```bash
python --version
```

### 2. Clonar el Repositorio
Abre tu terminal y clona este repositorio:
```bash
git clone https://github.com/Z4pata/Ajedrez.git
cd Ajedrez
```

### 3. Ejecutar el Juego
No se requieren dependencias externas (pip install) ya que usa bibliotecas nativas de Python. Simplemente ejecuta:

```bash
python main.py
```

## 🎮 Cómo Jugar

1.  El juego inicia con el turno de las **BLANCAS**.
2.  Haz **Click Izquierdo** sobre una pieza para seleccionarla (se resaltará en verde).
3.  Haz **Click Izquierdo** en una casilla de destino válida (vacía o con pieza enemiga) para mover.
4.  Si el movimiento es válido y no deja a tu Rey en Jaque, la pieza se moverá y el turno pasará al oponente.
5.  Observa el panel inferior para ver de quién es el turno actual.
6.  ¡Intenta hacer Jaque Mate al Rey oponente!

---
Desarrollado con ❤️ y 🐍 Python.
