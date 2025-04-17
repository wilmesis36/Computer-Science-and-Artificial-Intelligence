
# Instalar las librerías necesarias (solo si no están instaladas)
!pip install pgmpy networkx matplotlib
!pip install pgmpy

# Instalar las librerías necesarias (solo si no están instaladas)
!pip install pgmpy networkx matplotlib

# Importamos las librerías necesarias
import matplotlib.pyplot as plt
import networkx as nx
from pgmpy.models import DiscreteBayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination

# Paso 1: Crear el modelo bayesiano
model = DiscreteBayesianNetwork([('Gripe', 'Fiebre'),  # Gripe afecta a Fiebre
                                 ('Gripe', 'Tos'),    # Gripe afecta a Tos
                                 ('Resfriado', 'Fiebre'),  # Resfriado afecta a Fiebre
                                 ('Resfriado', 'Tos')])   # Resfriado afecta a Tos

# Paso 2: Definir las distribuciones de probabilidad condicional (CPTs)
cpd_gripe = TabularCPD(variable='Gripe', variable_card=2, values=[[0.7], [0.3]])  # 70% probabilidad de no tener gripe, 30% de tener gripe
cpd_resfriado = TabularCPD(variable='Resfriado', variable_card=2, values=[[0.8], [0.2]])  # 80% probabilidad de no tener resfriado, 20% de tenerlo

# Probabilidades de fiebre dadas Gripe y Resfriado
cpd_fiebre_gripe = TabularCPD(variable='Fiebre', variable_card=2, 
                               values=[[0.1, 0.6],  # 0.1 si no tiene gripe, 0.6 si tiene gripe
                                       [0.9, 0.4]],  # 0.9 si no tiene gripe, 0.4 si tiene gripe
                               evidence=['Gripe'], evidence_card=[2])

cpd_fiebre_resfriado = TabularCPD(variable='Fiebre', variable_card=2, 
                                   values=[[0.2, 0.7],  # 0.2 si no tiene resfriado, 0.7 si tiene resfriado
                                           [0.8, 0.3]],  # 0.8 si no tiene resfriado, 0.3 si tiene resfriado
                                   evidence=['Resfriado'], evidence_card=[2])

# Probabilidades de tos dadas Gripe y Resfriado
cpd_tos_gripe = TabularCPD(variable='Tos', variable_card=2,
                           values=[[0.3, 0.7],  # 0.3 si no tiene gripe, 0.7 si tiene gripe
                                   [0.7, 0.3]],  # 0.7 si no tiene gripe, 0.3 si tiene gripe
                           evidence=['Gripe'], evidence_card=[2])

cpd_tos_resfriado = TabularCPD(variable='Tos', variable_card=2,
                               values=[[0.4, 0.5],  # 0.4 si no tiene resfriado, 0.5 si tiene resfriado
                                       [0.6, 0.5]],  # 0.6 si no tiene resfriado, 0.5 si tiene resfriado
                               evidence=['Resfriado'], evidence_card=[2])

# Paso 3: Añadir las distribuciones al modelo
model.add_cpds(cpd_gripe, cpd_resfriado, cpd_fiebre_gripe, cpd_fiebre_resfriado, cpd_tos_gripe, cpd_tos_resfriado)

# Paso 4: Verificar el modelo
model.check_model()

# Paso 5: Realizar inferencias (por ejemplo, calcular la probabilidad de que el paciente tenga gripe dado que tiene fiebre y tos)
inference = VariableElimination(model)

# Calcular P(Gripe | Fiebre = 1, Tos = 1) => Probabilidad de tener gripe dado que tiene fiebre y tos
probabilidad_gripe = inference.query(variables=['Gripe'], evidence={'Fiebre': 1, 'Tos': 1})

# Mostrar el resultado
print(probabilidad_gripe)

# Paso 6: Visualización de la red bayesiana
# Creamos el gráfico de la red bayesiana usando networkx
plt.figure(figsize=(10, 8))
G = nx.DiGraph()  # Creamos un grafo dirigido

# Añadimos los nodos
G.add_edges_from([('Gripe', 'Fiebre'), ('Gripe', 'Tos'), 
                 ('Resfriado', 'Fiebre'), ('Resfriado', 'Tos')])

# Dibujamos el grafo
pos = nx.spring_layout(G)  # Layout para organizar los nodos
nx.draw(G, pos, with_labels=True, node_size=3000, node_color="skyblue", font_size=15, font_weight='bold', arrows=True)

# Mostrar la gráfica
plt.title("Red Bayesiana: Diagnóstico de Gripe vs Resfriado", fontsize=16)
plt.show()
