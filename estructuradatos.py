# Visualiza tres estructuras esenciales para la inteligencia artificial: árboles, grafos y matrices, usando librerías como networkx, matplotlib y numpy.

import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

# **Estructura de Datos**

# Configuración general de gráficos
plt.rcParams['figure.figsize'] = [6, 4]


# =============================
# 1. VISUALIZACIÓN DE UN ÁRBOL
# =============================

def mostrar_arbol():
    tree = nx.DiGraph()
    tree.add_edges_from([
        ("Raíz", "A"),
        ("Raíz", "B"),
        ("A", "A1"),
        ("A", "A2"),
        ("B", "B1"),
        ("B", "B2")
    ])

    pos = nx.spring_layout(tree)
    nx.draw(tree, pos, with_labels=True, node_color="lightblue", node_size=1000, arrows=True)
    plt.title("🌳 Árbol jerárquico")
    plt.show()

# =============================
# 2. VISUALIZACIÓN DE UN GRAFO
# =============================

def mostrar_grafo():
    graph = nx.Graph()
    graph.add_edges_from([
        ("A", "B"),
        ("A", "C"),
        ("B", "C"),
        ("C", "D"),
        ("D", "E"),
        ("E", "A")
    ])

    pos = nx.circular_layout(graph)
    nx.draw(graph, pos, with_labels=True, node_color="lightgreen", node_size=1000)
    plt.title("🌐 Grafo de relaciones")
    plt.show()

# =============================
# 3. VISUALIZACIÓN DE UNA MATRIZ
# =============================

def mostrar_matriz():
    matriz = np.array([
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ])

    plt.imshow(matriz, cmap="Blues", interpolation='nearest')
    for i in range(matriz.shape[0]):
        for j in range(matriz.shape[1]):
            plt.text(j, i, matriz[i, j], ha='center', va='center', color='black')

    plt.title("🧮 Matriz (como imagen)")
    plt.colorbar()
    plt.show()

# =============================
# Mostrar todo
# =============================
mostrar_arbol()
mostrar_grafo()
mostrar_matriz()
