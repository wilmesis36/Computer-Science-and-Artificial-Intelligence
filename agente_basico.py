# Importamos las librerías necesarias
import random          # Para generar posiciones aleatorias
import time            # Para pausar entre movimientos
from IPython.display import clear_output  # Para limpiar la salida entre pasos en Colab

# ===== CONFIGURACIÓN DEL ENTORNO =====

# Definimos el tamaño del entorno (una cuadrícula de 5x5)
grid_size = 5

# Ubicación aleatoria de la recompensa (el objetivo del agente)
reward_position = (random.randint(0, grid_size-1), random.randint(0, grid_size-1))

# Posición inicial del agente (empieza en la esquina superior izquierda)
agent_position = [0, 0]

# ===== FUNCIONES =====

# Esta función muestra visualmente el entorno en la consola
def display_grid():
    clear_output(wait=True)  # Borra la salida anterior (para simular movimiento)
    for i in range(grid_size):  # Recorremos las filas
        row = ""
        for j in range(grid_size):  # Recorremos las columnas
            if (i, j) == tuple(agent_position):
                row += "🤖 "  # Representa al agente
            elif (i, j) == reward_position:
                row += "🏆 "  # Representa la recompensa
            else:
                row += "⬜ "  # Casilla vacía
        print(row)  # Imprimimos cada fila
    print("\n")

# Esta función implementa la "inteligencia" del agente:
# se mueve en línea recta hacia la recompensa (estrategia determinista)
def move_agent():
    if agent_position[0] < reward_position[0]:
        agent_position[0] += 1  # Mover hacia abajo
    elif agent_position[0] > reward_position[0]:
        agent_position[0] -= 1  # Mover hacia arriba
    elif agent_position[1] < reward_position[1]:
        agent_position[1] += 1  # Mover hacia la derecha
    elif agent_position[1] > reward_position[1]:
        agent_position[1] -= 1  # Mover hacia la izquierda

# ===== CICLO PRINCIPAL DEL AGENTE =====

# El agente sigue ejecutando acciones hasta alcanzar la recompensa
while tuple(agent_position) != reward_position:
    display_grid()   # Mostrar entorno actual
    move_agent()     # Elegir acción y moverse
    time.sleep(0.5)  # Esperar medio segundo (para visualizar el movimiento)

# Mostrar estado final cuando se alcanza la recompensa
display_grid()
print("🎉 ¡El agente encontró la recompensa!")
