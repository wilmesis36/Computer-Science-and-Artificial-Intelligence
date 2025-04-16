# Knapsack Problem (Problema de la mochila): Este es un clásico problema de optimización combinatoria donde tenemos un conjunto de artículos 
# con ciertos pesos y valores, y una capacidad máxima de la mochila. El objetivo es maximizar el valor total de los artículos que podemos meter 
# en la mochila sin exceder la capacidad.

# Complejidad computacional: A medida que aumentamos el número de artículos, el tiempo de ejecución crece exponencialmente, lo cual refleja 
# la "explosión combinatoria" de soluciones posibles. Esto simula la complejidad que se puede encontrar en problemas de optimización en IA.

# Generación aleatoria de datos: El código genera pesos y valores aleatorios para los artículos y calcula el valor óptimo para cada caso. 
# A medida que aumentamos el número de artículos, la complejidad aumenta, lo que simula el desafío de encontrar soluciones eficientes.

# Medición de tiempo: Se mide el tiempo que tarda en resolver el problema para cada conjunto de datos.

import random
import time
import matplotlib.pyplot as plt

# Función para simular un problema de optimización (como el problema de la mochila)
def knapsack_problem(weights, values, capacity):
    """
    Resuelve el problema de la mochila usando programación dinámica.
    - weights: lista de pesos de los artículos
    - values: lista de valores de los artículos
    - capacity: capacidad máxima de la mochila
    
    Devuelve el valor óptimo que se puede obtener sin exceder la capacidad de la mochila.
    """
    n = len(weights)  # Número de artículos
    # Creamos una matriz dp de (n+1) x (capacity+1) para almacenar los resultados intermedios
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    # Llenamos la tabla dp para encontrar la solución óptima
    for i in range(1, n + 1):  # Recorremos los artículos
        for w in range(1, capacity + 1):  # Recorremos las capacidades posibles
            # Si el artículo puede caber en la mochila (peso[i-1] <= w)
            if weights[i - 1] <= w:
                # Tomamos el máximo entre no incluir el artículo o incluirlo
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weights[i - 1]] + values[i - 1])
            else:
                # Si no cabe, simplemente copiamos el valor de la fila anterior
                dp[i][w] = dp[i - 1][w]
    
    # El valor óptimo estará en la esquina inferior derecha de la matriz dp
    return dp[n][capacity]

# Función para generar datos aleatorios para el problema de la mochila
def generate_knapsack_data(num_items):
    """
    Genera un conjunto de datos aleatorios para el problema de la mochila.
    - num_items: número de artículos en el problema
    Devuelve tres listas: los pesos, los valores de los artículos y la capacidad de la mochila.
    """
    weights = [random.randint(1, 10) for _ in range(num_items)]  # Pesos aleatorios entre 1 y 10
    values = [random.randint(10, 100) for _ in range(num_items)]  # Valores aleatorios entre 10 y 100
    capacity = sum(weights) // 2  # Capacidad de la mochila será la mitad del peso total
    return weights, values, capacity

# Función que simula el aumento de la complejidad computacional al resolver el problema
def simulate_computational_complexity():
    """
    Simula cómo aumenta el tiempo de ejecución al incrementar el número de artículos.
    Realiza la simulación para distintos tamaños de problema.
    
    Este es un ejemplo de cómo la complejidad computacional en IA puede crecer a medida que
    aumentan el tamaño de los problemas, reflejando la 'explosión combinatoria' que ocurre en muchos
    problemas de optimización en Inteligencia Artificial.
    
    En el código se usa un problema de optimización clásico, el problema de la mochila, cuya 
    complejidad crece exponencialmente con el número de artículos debido a las posibles combinaciones
    de elementos que se pueden considerar para optimizar el valor sin exceder la capacidad de la mochila.
    """
    num_items_list = [10, 20, 30, 40, 50]  # Lista de tamaños de problema
    times = []  # Lista para almacenar los tiempos de ejecución
    for num_items in num_items_list:
        print(f"\nSimulando para {num_items} artículos:")
        # Generamos datos aleatorios para cada número de artículos
        weights, values, capacity = generate_knapsack_data(num_items)
        
        # Medimos el tiempo de ejecución para resolver el problema
        start_time = time.time()
        result = knapsack_problem(weights, values, capacity)  # Llamamos a la función de solución
        end_time = time.time()

        # Mostramos el resultado y el tiempo de ejecución
        print(f"Valor óptimo: {result}")
        time_taken = end_time - start_time
        print(f"Tiempo de ejecución: {time_taken:.6f} segundos")
        
        # Almacenamos el tiempo de ejecución
        times.append(time_taken)
    
    # Graficamos los resultados
    plt.plot(num_items_list, times, marker='o', color='b', linestyle='-', linewidth=2, markersize=8)
    plt.xlabel('Número de artículos')
    plt.ylabel('Tiempo de ejecución (segundos)')
    plt.title('Impacto de la complejidad computacional en el problema de la mochila')
    plt.grid(True)
    plt.show()

# Ejecutamos la simulación
simulate_computational_complexity()
