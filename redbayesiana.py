
# Instalar las librerías necesarias (solo si no están instaladas)
!pip install pgmpy networkx matplotlib
!pip install pgmpy
# Instalar las librerías necesarias
!pip install pgmpy networkx matplotlib

# Importar librerías
import matplotlib.pyplot as plt
import networkx as nx
from pgmpy.models import DiscreteBayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination

# Paso 1: Crear el modelo bayesiano
model = DiscreteBayesianNetwork([
    ('Gripe', 'Fiebre'),
    ('Resfriado', 'Fiebre'),
    ('Gripe', 'Tos'),
    ('Resfriado', 'Tos')
])

# Paso 2: Definir las CPDs

# Probabilidad de tener gripe o no
cpd_gripe = TabularCPD(variable='Gripe', variable_card=2, values=[[0.7], [0.3]])

# Probabilidad de tener resfriado o no
cpd_resfriado = TabularCPD(variable='Resfriado', variable_card=2, values=[[0.8], [0.2]])

# CPD de Fiebre según Gripe y Resfriado
cpd_fiebre = TabularCPD(variable='Fiebre', variable_card=2,
                        values=[
                            [0.99, 0.9, 0.9, 0.6],  # Fiebre = No
                            [0.01, 0.1, 0.1, 0.4]   # Fiebre = Sí
                        ],
                        evidence=['Gripe', 'Resfriado'],
                        evidence_card=[2, 2])

# CPD de Tos según Gripe y Resfriado
cpd_tos = TabularCPD(variable='Tos', variable_card=2,
                     values=[
                         [0.9, 0.6, 0.6, 0.3],   # Tos = No
                         [0.1, 0.4, 0.4, 0.7]    # Tos = Sí
                     ],
                     evidence=['Gripe', 'Resfriado'],
                     evidence_card=[2, 2])

# Paso 3: Añadir CPDs al modelo
model.add_cpds(cpd_gripe, cpd_resfriado, cpd_fiebre, cpd_tos)

# Paso 4: Verificar el modelo
assert model.check_model(), "Modelo no válido"

# Paso 5: Inferencias
inference = VariableElimination(model)
resultado = inference.query(variables=['Gripe'], evidence={'Fiebre': 1, 'Tos': 1})
print("🔍 Probabilidad de tener Gripe dado que hay Fiebre y Tos:\n")
print(resultado)

# Paso 6: Visualización de la red
plt.figure(figsize=(10, 6))
G = nx.DiGraph()
G.add_edges_from([
    ('Gripe', 'Fiebre'),
    ('Resfriado', 'Fiebre'),
    ('Gripe', 'Tos'),
    ('Resfriado', 'Tos')
])
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_size=3000, node_color='lightblue', font_size=14, font_weight='bold', arrows=True)
plt.title("📊 Red Bayesiana: Diagnóstico de Gripe vs Resfriado", fontsize=16)
plt.show()
