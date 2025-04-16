# =====================================
# Algoritmo A* con Visualización en Python
# =====================================

import matplotlib.pyplot as plt
import numpy as np
from heapq import heappop, heappush  # Para manejar la open list como una cola de prioridad
import time

# --------------------------
# CONFIGURACIÓN DEL MAPA
# --------------------------

ROWS, COLS = 10, 10  # Tamaño de la cuadrícula
START = (0, 0)       # Punto de inicio
END = (9, 9)         # Punto de destino

# Obstáculos que el algoritmo debe esquivar
OBSTACLES = [
    (1, 3), (2, 3), (3, 3), (4, 3), (5, 3), (6, 3),
    (6, 2), (6, 1), (6, 0), (7, 0), (8, 0), (8, 1)
]

# --------------------------
# FUNCIONES AUXILIARES
# --------------------------

def heuristic(a, b):
    """
    Heurística: distancia Manhattan.
    Es la suma de las diferencias absolutas en filas y columnas.
    """
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def get_neighbors(pos):
    """
    Dado un nodo, devuelve sus vecinos válidos (arriba, abajo, izquierda, derecha)
    Excluye obstáculos y bordes del mapa.
    """
    directions = [(0,1),(1,0),(0,-1),(-1,0)]  # Derecha, abajo, izquierda, arriba
    neighbors = []
    for d in directions:
        nr, nc = pos[0] + d[0], pos[1] + d[1]
        if 0 <= nr < ROWS and 0 <= nc < COLS and (nr, nc) not in OBSTACLES:
            neighbors.append((nr, nc))
    return neighbors

def draw(grid=None, path=None, visited=None):
    """
    Dibuja la cuadrícula con:
    - Obstáculos: negro
    - Inicio: verde
    - Fin: rojo
    - Celdas visitadas: azul claro
    - Camino final: amarillo
    """
    display = np.ones((ROWS, COLS, 3))  # Inicializar blanco

    # Pintar obstáculos e inicio/fin
    for r in range(ROWS):
        for c in range(COLS):
            if (r, c) in OBSTACLES:
                display[r, c] = [0, 0, 0]  # Negro
            elif (r, c) == START:
                display[r, c] = [0, 1, 0]  # Verde
            elif (r, c) == END:
                display[r, c] = [1, 0, 0]  # Rojo

    # Celdas visitadas por A*
    if visited:
        for v in visited:
            if v != START and v != END:
                display[v[0], v[1]] = [0.6, 0.6, 1]

    # Camino encontrado
    if path:
        for p in path:
            if p != START and p != END:
                display[p[0], p[1]] = [1, 1, 0]

    # Mostrar cuadrícula
    plt.imshow(display)
    plt.grid(True)
    plt.xticks(np.arange(-0.5, COLS, 1), [])
    plt.yticks(np.arange(-0.5, ROWS, 1), [])
    plt.show()

# --------------------------
# IMPLEMENTACIÓN DEL A*
# --------------------------

def a_star(start, goal):
    """
    Algoritmo A* para encontrar el camino más corto desde `start` hasta `goal`.
    Devuelve el camino como una lista de coordenadas.
    """
    open_set = []
    heappush(open_set, (0 + heuristic(start, goal), 0, start, [start]))  # (f, g, nodo, camino)
    visited = set()  # Para evitar volver a visitar nodos

    while open_set:
        f, g, current, path = heappop(open_set)  # Extrae el nodo con menor f

        if current in visited:
            continue

        visited.add(current)

        # Visualizar estado actual del algoritmo
        draw(path=path, visited=visited)
        time.sleep(0.3)

        # Caso base: llegamos al objetivo
        if current == goal:
            return path

        # Explorar vecinos
        for neighbor in get_neighbors(current):
            if neighbor not in visited:
                new_g = g + 1  # Costo real desde el inicio hasta el vecino
                new_f = new_g + heuristic(neighbor, goal)  # f = g + h
                heappush(open_set, (new_f, new_g, neighbor, path + [neighbor]))

    return None  # No hay camino posible

# --------------------------
# EJECUCIÓN DEL ALGORITMO
# --------------------------

final_path = a_star(START, END)

if final_path:
    print("✅ ¡Camino encontrado!")
else:
    print("❌ No hay camino posible.")
