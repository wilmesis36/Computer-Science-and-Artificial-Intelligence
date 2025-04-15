# Instalamos la librería si no la tienes instalada (esto solo es necesario una vez)
!pip install scikit-learn

# Importamos las librerías necesarias
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split  # Para dividir el conjunto de datos
from sklearn.neighbors import KNeighborsClassifier  # Algoritmo K-Nearest Neighbors
from sklearn import datasets  # Para cargar datasets de ejemplo
from sklearn.metrics import classification_report  # Para evaluar el modelo

# Cargamos un dataset de ejemplo (iris dataset)
# Este es un conjunto de datos muy utilizado en Machine Learning
iris = datasets.load_iris()  # Cargamos el conjunto de datos Iris, que contiene información sobre flores
X = iris.data  # Características de las flores (longitud y ancho de sépalo/pétalo)
y = iris.target  # Etiquetas de clase (categorías) que representan las especies de las flores

# Dividimos el dataset en datos de entrenamiento y datos de prueba (70% - 30%)
# Esto es importante para entrenar el modelo con una parte de los datos y probarlo con los datos no vistos.
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Creamos el clasificador KNN (K-Nearest Neighbors)
# KNN es un algoritmo que clasifica un punto basándose en la proximidad a otros puntos (vecinos) en el espacio de características.
knn = KNeighborsClassifier(n_neighbors=3)  # Usamos 3 vecinos para hacer la clasificación

# Entrenamos el clasificador con los datos de entrenamiento
# El modelo aprende patrones de los datos para poder predecir las etiquetas de nuevos datos.
knn.fit(X_train, y_train)

# Realizamos predicciones sobre los datos de prueba
# Después de entrenar el modelo, lo evaluamos usando los datos de prueba que el modelo no ha visto.
y_pred = knn.predict(X_test)

# Mostramos el reporte de clasificación para evaluar el rendimiento del modelo
# El reporte incluye métricas como precisión, recall y F1-score, que ayudan a evaluar qué tan bien el modelo clasifica.
print("Reporte de clasificación:")
print(classification_report(y_test, y_pred))

# Visualizamos la relación entre las características (se utiliza solo para un dataset sencillo como este)
# Este paso nos ayuda a ver cómo el modelo está clasificando los datos en un gráfico de 2D.
plt.scatter(X_test[:, 0], X_test[:, 1], c=y_pred, cmap='viridis', marker='o')
plt.title('Clasificación de Flores Iris - KNN')
plt.xlabel('Longitud del Sépalo')  # Una de las características del dataset
plt.ylabel('Ancho del Sépalo')  # Otra de las características del dataset
plt.colorbar(label='Categoría')  # Leyenda de las categorías predichas
plt.show()
