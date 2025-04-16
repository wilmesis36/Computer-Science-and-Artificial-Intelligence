# Importamos las librerías necesarias
import time

# Representación del conocimiento: Hechos y Reglas
# -------------------------------------------
# Definimos los hechos iniciales (síntomas del paciente) y las reglas para el diagnóstico.

# Hechos iniciales proporcionados por el usuario
hechos = set()  # Base de hechos vacía

# Reglas del sistema experto (diagnóstico basado en los hechos)
reglas = [
    {
        "si": {"fiebre", "tos"},
        "entonces": "posible_gripe"
    },
    {
        "si": {"dolor_garganta", "tos"},
        "entonces": "posible_resfriado"
    },
    {
        "si": {"posible_gripe", "dolor_cabeza"},
        "entonces": "gripe"
    },
    {
        "si": {"posible_resfriado"},
        "entonces": "resfriado_comun"
    }
]

# Motor de inferencia: encadenamiento hacia adelante
# ---------------------------------------------------
# Aquí aplicamos las reglas de inferencia automáticamente para deducir nuevos hechos.
def motor_inferencia(hechos, reglas):
    nuevos_hechos = set()  # Conjunto para nuevos hechos inferidos.
    while True:
        cambio = False  # Variable que verifica si hubo un cambio.
        
        for regla in reglas:
            # Comprobamos si todos los hechos necesarios para aplicar la regla están presentes
            if regla["si"].issubset(hechos) and regla["entonces"] not in hechos:
                print(f"Aplicando regla: {regla}")  # Informamos cuál regla estamos aplicando.
                nuevos_hechos.add(regla["entonces"])  # Añadimos el nuevo hecho inferido.
                cambio = True
        
        hechos.update(nuevos_hechos)  # Actualizamos los hechos con los nuevos inferidos.
        if not cambio:
            break  # Si no hubo cambios, terminamos el proceso de inferencia.
    
    return hechos  # Retornamos los hechos finales tras la inferencia.

# Simulación de entrada del usuario
# ----------------------------------
# En esta sección, recibimos los síntomas del usuario y los agregamos a la base de hechos.
entrada_usuario = ["fiebre", "tos", "dolor_cabeza"]

# Agregamos los hechos iniciales a la base de hechos
hechos = set(entrada_usuario)

# Ejecución del motor de inferencia para obtener los resultados del diagnóstico
# --------------------------------------------------------------------------
print("🔍 Comenzando el diagnóstico...")

# Simulamos un pequeño retraso para que sea más visible el proceso en Colab
time.sleep(1)

# Ejecutamos la inferencia con los hechos y reglas
resultado = motor_inferencia(hechos, reglas)

# Presentación de los resultados
# --------------------------------
# Una vez realizados los diagnósticos, mostramos los resultados.
print("\n🔍 Diagnóstico final basado en síntomas:")
time.sleep(1)

# Imprimimos los hechos inferidos (diagnósticos)
for hecho in resultado:
    if hecho not in entrada_usuario:  # Excluimos los hechos iniciales
        print(f"- {hecho.replace('_', ' ').capitalize()}")  # Presentamos el diagnóstico final

