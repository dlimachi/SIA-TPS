import pandas as pd
import matplotlib.pyplot as plt
from perceptron import perceptron_training
import numpy as np

df = pd.read_csv('TP3-ej2-conjunto.csv')

data_set = []
for _, row in df.iterrows():
    x_values = row[['x1', 'x2', 'x3']].values
    y_value = row['y']
    data_set.append((x_values, y_value))

x_values = [row[0][0] for row in data_set]
y_values = [row[0][1] for row in data_set]
z_values = [row[0][2] for row in data_set]
# Extrae las etiquetas y de cada punto
labels = [row[1] for row in data_set]

# Crea una figura 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Grafica los puntos
ax.scatter(x_values, y_values, z_values, c=labels, cmap='bwr')

# Etiqueta los ejes
ax.set_xlabel('X1')
ax.set_ylabel('X2')
ax.set_zlabel('X3')

# --- Grafico ---
_, w_min = perceptron_training(data_set, 0.01, 1000)

print(w_min)
# x1 * w1 + x2 * w2 + x3 * w3 + w0 = 0



# Crear una malla para el plano de decisión
xx, yy = np.meshgrid(range(-2, 3), range(-2, 3))
zz = (-w_min[1] * w_min[0] - w_min[2] * xx - w_min[3] * yy) / w_min[3]

# Dibujar el plano de decisión
plane = ax.plot_surface(xx, yy, zz, alpha=0.5, color='blue')

plt.show()
