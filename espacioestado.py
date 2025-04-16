# ------------------------------------------------------------------------------
# Simulación del concepto de Espacios de Estados y Grafos de Búsqueda Avanzados
#
# Usaremos el clásico problema del 8-puzzle (un tablero 3x3 con piezas numeradas 
# del 1 al 8 y un espacio vacío). Este problema es ideal para explorar:
#
# ✅ Espacios de estados: cada configuración del tablero es un estado.
# ✅ Grafos de búsqueda: cada movimiento entre estados es una arista.
# ✅ Algoritmos avanzados como A* con heurística (ej. distancia de Manhattan).
# ✅ Poda de caminos subóptimos gracias al uso de heurísticas.
#
# 🧠 ¿Qué haremos?
# - Simular el espacio de estados del 8-puzzle.
# - Implementar un algoritmo de búsqueda A* para encontrar el camino más corto 
#   desde un estado inicial hasta el estado objetivo.
# - Utilizar heurística para mejorar la eficiencia (reducir caminos innecesarios).
# - Mostrar el número de nodos explorados y la solución encontrada.
#
# 🎓 ¿Qué aprendes con esto?
# - Cada configuración del tablero representa un estado en el espacio de estados.
# - A* explora estos estados como si fueran nodos de un grafo de búsqueda.
# - La heurística (distancia de Manhattan) reduce los caminos a explorar.
# - Se aplican técnicas de poda para evitar reexplorar caminos.
# - Se obtiene una solución óptima, minimizando los pasos desde el estado inicial 
#   al objetivo.
# ------------------------------------------------------------------------------

import heapq
import itertools

# Estado objetivo (meta): la configuración correcta del 8-puzzle
goal_state = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]  # 0 representa el espacio vacío
]

# Definimos los movimientos posibles y cómo afectan la posición
moves = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

# Convierte una matriz 3x3 en una tupla para poder usarla como clave en conjuntos o diccionarios
def board_to_tuple(board):
    return tuple(itertools.chain(*board))

# Encuentra la posición del espacio vacío (0)
def find_zero(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == 0:
                return i, j

# Aplica un movimiento al tablero y devuelve el nuevo tablero resultante
def apply_move(board, direction):
    i, j = find_zero(board)  # Encuentra dónde está el espacio vacío
    di, dj = moves[direction]  # Determina hacia dónde se moverá
    ni, nj = i + di, j + dj  # Nueva posición después del movimiento

    # Validamos que la nueva posición esté dentro de los límites del tablero
    if 0 <= ni < 3 and 0 <= nj < 3:
        # Copiamos el tablero actual y aplicamos el movimiento
        new_board = [row[:] for row in board]
        new_board[i][j], new_board[ni][nj] = new_board[ni][nj], new_board[i][j]
        return new_board

    return None  # Movimiento inválido

# Heurística: calcula la suma de distancias de Manhattan para cada número respecto a su posición en la meta
def manhattan_distance(board):
    distance = 0
    for i in range(3):
        for j in range(3):
            val = board[i][j]
            if val != 0:
                # Calcula la posición correcta del número en el estado meta
                goal_i, goal_j = divmod(val - 1, 3)
                # Distancia de Manhattan = diferencia en filas + columnas
                distance += abs(i - goal_i) + abs(j - goal_j)
    return distance

# Algoritmo A* para encontrar la solución óptima al 8-puzzle
def solve_puzzle(initial_board):
    # Cola de prioridad (heap) que contiene tuplas: (costo_estimado_total, costo_actual, tablero, camino)
    frontier = []
    heapq.heappush(frontier, (0 + manhattan_distance(initial_board), 0, initial_board, []))
    
    visited = set()  # Conjunto para evitar ciclos y repeticiones de estados

    while frontier:
        # Extrae el nodo con menor costo estimado total
        est_total_cost, cost_so_far, board, path = heapq.heappop(frontier)
        board_key = board_to_tuple(board)

        # Si ya visitamos este estado, lo ignoramos
        if board_key in visited:
            continue
        visited.add(board_key)

        # Verifica si hemos llegado al estado objetivo
        if board == goal_state:
            return path, cost_so_far, len(visited)

        # Generamos nuevos estados (vecinos) aplicando cada movimiento posible
        for move in moves:
            new_board = apply_move(board, move)
            if new_board:
                new_path = path + [move]  # Agrega el movimiento al historial
                new_cost = cost_so_far + 1  # Costo acumulado
                est_cost = new_cost + manhattan_distance(new_board)  # A* = costo real + heurística
                # Agrega el nuevo estado a la frontera
                heapq.heappush(frontier, (est_cost, new_cost, new_board, new_path))

    # Si no hay solución (no debería pasar con tableros válidos)
    return None, None, len(visited)

# Estado inicial desordenado
initial_state = [
    [2, 8, 3],
    [1, 6, 4],
    [7, 0, 5]
]

# Ejecutamos el algoritmo de búsqueda
solution, cost, nodes_explored = solve_puzzle(initial_state)

# Imprimimos el resultado
print("Estado inicial:")
for row in initial_state:
    print(row)

print("\nSecuencia de movimientos hasta la solución:")
print(solution)

print(f"\nMovimientos requeridos: {cost}")
print(f"Nodos explorados: {nodes_explored}")
