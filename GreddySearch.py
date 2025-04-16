# ================================================
# ALGORITMO DE BÚSQUEDA GREEDY (GREEDY SEARCH)
# Descripción: Demostración básica del algoritmo Greedy Search
#              con visualización de un grafo en Google Colab
# ================================================

import heapq  # Para usar una cola de prioridad (heap)
import matplotlib.pyplot as plt  # Para visualizar el grafo
import networkx as nx  # Para crear y manejar grafos

# ------------------------------------------------
# Definimos un grafo dirigido como un diccionario
# Cada nodo tiene una lista de vecinos
# ------------------------------------------------
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['G'],
    'F': ['G'],
    'G': []
}

# ------------------------------------------------
# Heurística (h(n)): estimación del costo desde cada
# nodo hasta el nodo objetivo (G).
# Cuanto menor sea el valor, más "cerca" creemos que está.
# ------------------------------------------------
heuristic = {
    'A': 7,
    'B': 6,
    'C': 2,
    'D': 1,
    'E': 1,
    'F': 1,
    'G': 0
}

# ------------------------------------------------
# Función que implementa el algoritmo Greedy Search
# ------------------------------------------------
def greedy_search(start, goal):
    visited = set()  # Conjunto para registrar los nodos visitados
    priority_queue = []  # Cola de prioridad basada en h(n)
    path = {}  # Diccionario para reconstruir el camino

    # Insertamos el nodo inicial en la cola con su heurística
    heapq.heappush(priority_queue, (heuristic[start], start))

    while priority_queue:
        # Sacamos el nodo con menor heurística
        _, current = heapq.heappop(priority_queue)

        if current in visited:
            continue
        visited.add(current)

        # Si llegamos al objetivo, terminamos
        if current == goal:
            break

        # Agregamos vecinos no visitados a la cola
        for neighbor in graph[current]:
            if neighbor not in visited:
                heapq.heappush(priority_queue, (heuristic[neighbor], neighbor))
                # Guardamos de dónde venimos para reconstruir el camino
                if neighbor not in path:
                    path[neighbor] = current

    # Reconstrucción del camino desde el objetivo al inicio
    full_path = []
    node = goal
    while node != start:
        full_path.append(node)
        node = path.get(node)
        if node is None:
            print("No se encontró camino.")
            return []
    full_path.append(start)
    full_path.reverse()  # Invertimos para obtener el orden correcto
    return full_path

# ------------------------------------------------
# Configuración inicial: nodo de inicio y meta
# ------------------------------------------------
start_node = 'A'
goal_node = 'G'
result_path = greedy_search(start_node, goal_node)

# ------------------------------------------------
# Mostramos el resultado del algoritmo
# ------------------------------------------------
print(f"\n🔍 Camino encontrado por Greedy Search de {start_node} a {goal_node}:")
print(" ➜ ".join(result_path))

# ------------------------------------------------
# Visualización del grafo con NetworkX y Matplotlib
# ------------------------------------------------
# Creamos el grafo dirigido
G = nx.DiGraph()
for node, neighbors in graph.items():
    for neighbor in neighbors:
        G.add_edge(node, neighbor)

# Posicionamiento automático de nodos
pos = nx.spring_layout(G)

# Dibujamos el grafo completo
nx.draw(G, pos, with_labels=True, node_color='lightblue',
        node_size=1200, font_size=14, edge_color='gray')

# Dibujamos el camino encontrado en rojo
path_edges = list(zip(result_path, result_path[1:]))
nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='red', width=3)

plt.title("Greedy Search Path", fontsize=16)
plt.show()
