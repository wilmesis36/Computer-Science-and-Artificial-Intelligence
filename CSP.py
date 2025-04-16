# ========================================
# Ejemplo básico de CSP: Coloreo de mapas
# Librería: python-constraint
# ========================================

# Instalamos la librería necesaria (solo si no está ya instalada)
!pip install -q python-constraint

# Importamos la clase principal para definir un problema CSP
from constraint import Problem

# ----------------------------------------
# Creamos una instancia del problema CSP
# ----------------------------------------
problem = Problem()

# ----------------------------------------
# VARIABLES DEL PROBLEMA
# Vamos a modelar 4 regiones: A, B, C, D
# Cada región debe tener un color diferente de sus vecinas
# ----------------------------------------
variables = ['A', 'B', 'C', 'D']

# DOMINIO: Colores posibles para cada región
colors = ['Rojo', 'Verde', 'Azul']

# Asignamos a cada región su dominio de colores
for region in variables:
    problem.addVariable(region, colors)

# ----------------------------------------
# RESTRICCIONES ENTRE REGIONES
# Dos regiones vecinas no pueden tener el mismo color
# A es vecina de B y C
# B es vecina de C y D
# C es vecina de D
# ----------------------------------------

# Cada restricción se define con una función lambda que asegura que los valores son diferentes
problem.addConstraint(lambda a, b: a != b, ('A', 'B'))
problem.addConstraint(lambda a, c: a != c, ('A', 'C'))
problem.addConstraint(lambda b, c: b != c, ('B', 'C'))
problem.addConstraint(lambda b, d: b != d, ('B', 'D'))
problem.addConstraint(lambda c, d: c != d, ('C', 'D'))

# ----------------------------------------
# RESOLVER EL PROBLEMA
# Obtenemos todas las soluciones que cumplen las restricciones
# ----------------------------------------
solutions = problem.getSolutions()

# ----------------------------------------
# MOSTRAR RESULTADOS
# Imprimimos cuántas soluciones válidas se encontraron y sus asignaciones
# ----------------------------------------
print(f"🧠 Se encontraron {len(solutions)} soluciones posibles:\n")
for i, solution in enumerate(solutions, 1):
    print(f"Solución {i}: {solution}")
