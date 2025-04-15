# Grafo que representa el espacio de estados
# Cada nodo tiene una lista de nodos adyacentes (vecinos)
# Además, cada nodo tiene un costo asociado para llegar al nodo objetivo.
graph = {
    'A': {'B': 1, 'C': 3},  # 'A' tiene como vecinos a 'B' y 'C' con costos 1 y 3 respectivamente
    'B': {'D': 1, 'E': 5},  # 'B' tiene como vecinos a 'D' y 'E' con costos 1 y 5 respectivamente
    'C': {'F': 1},          # 'C' tiene como vecino a 'F' con costo 1
    'D': {},                # 'D' no tiene vecinos
    'E': {'G': 2},          # 'E' tiene como vecino a 'G' con costo 2
    'F': {},                # 'F' no tiene vecinos
    'G': {}                 # 'G' es el nodo objetivo, no tiene vecinos
}

# Búsqueda en anchura (BFS)
def bfs(graph, start, goal):
    queue = [[start]]  # Cola que almacena las rutas, comenzando con el nodo de inicio
    visited = set()  # Conjunto para rastrear los nodos visitados

    while queue:
        path = queue.pop(0)  # Extraemos el primer camino de la cola
        node = path[-1]  # Tomamos el último nodo del camino actual

        # Si hemos llegado al objetivo, retornamos el camino completo
        if node == goal:
            return path

        # Si el nodo no ha sido visitado, lo marcamos y expandimos sus vecinos
        if node not in visited:
            visited.add(node)  # Marcamos el nodo como visitado
            for neighbor in graph[node]:  # Expandimos los vecinos del nodo actual
                new_path = list(path)  # Hacemos una copia del camino actual
                new_path.append(neighbor)  # Añadimos el vecino al camino
                queue.append(new_path)  # Añadimos el nuevo camino a la cola

# Búsqueda en profundidad (DFS)
def dfs(graph, start, goal, path=None, visited=None):
    if path is None:
        path = [start]  # Inicia el camino con el nodo de inicio
    if visited is None:
        visited = set()  # Conjunto para rastrear los nodos visitados

    node = path[-1]  # Tomamos el último nodo del camino actual

    # Si hemos encontrado el objetivo, retornamos el camino
    if node == goal:
        return path

    visited.add(node)  # Marcamos el nodo como visitado
    # Expandimos los vecinos del nodo actual
    for neighbor in graph[node]:
        if neighbor not in visited:  # Solo exploramos los nodos no visitados
            new_path = list(path)  # Hacemos una copia del camino actual
            new_path.append(neighbor)  # Añadimos el vecino al camino
            # Llamamos recursivamente para explorar este vecino
            result = dfs(graph, start, goal, new_path, visited)
            if result:  # Si encontramos el objetivo, devolvemos el camino
                return result

# Algoritmo Greedy
# Utiliza una heurística para guiar la búsqueda hacia el objetivo.
# La heurística evalúa cuán cerca está un nodo del objetivo.
def greedy(graph, start, goal, heuristic):
    visited = set()  # Conjunto para rastrear los nodos visitados
    queue = [(start, [start])]  # Cola de prioridad que almacena nodos y caminos

    while queue:
        # Ordenamos la cola según la heurística para expandir el nodo más prometedor
        queue.sort(key=lambda x: heuristic[x[0]])  # Ordena según el valor de la heurística
        node, path = queue.pop(0)  # Extraemos el primer nodo y su camino

        # Si hemos llegado al objetivo, retornamos el camino
        if node == goal:
            return path

        # Expandimos los vecinos del nodo actual
        if node not in visited:
            visited.add(node)  # Marcamos el nodo como visitado
            for neighbor in graph[node]:
                new_path = list(path)  # Hacemos una copia del camino actual
                new_path.append(neighbor)  # Añadimos el vecino al camino
                queue.append((neighbor, new_path))  # Añadimos el vecino y el camino a la cola

# Algoritmo A* (A-star)
# Combina la búsqueda en anchura con una heurística para encontrar el camino más corto.
# Considera tanto el costo acumulado como la estimación de la heurística.
def a_star(graph, start, goal, heuristic, cost):
    open_list = [(start, [start], 0)]  # Cola de prioridad con el nodo inicial y su costo
    closed_list = set()  # Conjunto de nodos ya procesados

    while open_list:
        # Ordenamos la lista abierta por el costo total (g(n) + h(n))
        open_list.sort(key=lambda x: x[2] + heuristic[x[0]])  # Costo acumulado + heurística
        node, path, current_cost = open_list.pop(0)  # Extraemos el nodo con el menor costo

        # Si hemos llegado al objetivo, retornamos el camino
        if node == goal:
            return path

        # Expandimos los vecinos del nodo actual
        if node not in closed_list:
            closed_list.add(node)  # Marcamos el nodo como procesado
            for neighbor, edge_cost in graph[node].items():
                new_cost = current_cost + edge_cost  # Calculamos el costo acumulado
                new_path = list(path)  # Hacemos una copia del camino actual
                new_path.append(neighbor)  # Añadimos el vecino al camino
                open_list.append((neighbor, new_path, new_cost))  # Añadimos el vecino a la cola

# Ejecutar las búsquedas
print("BFS de A a G:", bfs(graph, 'A', 'G'))  # Utilizando búsqueda en anchura (BFS)
print("DFS de A a G:", dfs(graph, 'A', 'G'))  # Utilizando búsqueda en profundidad (DFS)

# Definir heurística para Greedy y A*
heuristic = {
    'A': 6, 'B': 5, 'C': 4, 'D': 3, 'E': 2, 'F': 1, 'G': 0
}

# Costo para A*
cost = {
    'A': {'B': 1, 'C': 3},
    'B': {'D': 1, 'E': 5},
    'C': {'F': 1},
    'E': {'G': 2}
}

# Ejecutar Greedy y A*
print("Greedy de A a G:", greedy(graph, 'A', 'G', heuristic))
print("A* de A a G:", a_star(graph, 'A', 'G', heuristic, cost))
