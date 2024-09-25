import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Definir las ecuaciones
def eq1(x, y):
    return (200/100 - 1/100 * x - 10.01/100 * y)  # x3 = 200/100 - 1/100x1 - 10.01/100x2

def eq2(x, y):
    return (300/200 - 2.12/200 * x - 20/200 * y)  # x3 = 300/200 - 2.12/200x1 - 20/200x2

def eq3(x, y):
    return (400/300 - 3.1/300 * x - 30/300 * y)  # x3 = 400/300 - 3.1/300x1 - 30/300x2

# Crear un rango de valores para x y y
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
x, y = np.meshgrid(x, y)

# Calcular z para cada ecuación
z1 = eq1(x, y)
z2 = eq2(x, y)
z3 = eq3(x, y)

# Crear la figura y los ejes 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Graficar las superficies
ax.plot_surface(x, y, z1, alpha=0.5, rstride=100, cstride=100, color='red', label='Ecuación 1')
ax.plot_surface(x, y, z2, alpha=0.5, rstride=100, cstride=100, color='blue', label='Ecuación 2')
ax.plot_surface(x, y, z3, alpha=0.5, rstride=100, cstride=100, color='green', label='Ecuación 3')

# Configurar etiquetas y título
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Sistema de 3 Ecuaciones con 3 Incógnitas')

# Mostrar la gráfica
plt.show()