import numpy as np
import matplotlib.pyplot as plt

# Definir las ecuaciones
def eq1(x):
    return -1.0001/1.0000 * x + 2/1.0000  

def eq2(x):
    return -1.0000/1.0000 * x + 2/1.0000  

# Crear un rango de valores para x
x = np.linspace(-5, 5, 100)

# Calcular y para cada ecuación
y1 = eq1(x)
y2 = eq2(x)

# Crear la figura
plt.figure(figsize=(8, 6))

# Graficar las líneas
plt.plot(x, y1, label='Ecuación 1: x2 = -1.0001/1.0000x1 + 2/1.0000', color='red')
plt.plot(x, y2, label='Ecuación 2: x2 = -1.0000/1.0000x1 + 2/1.0000', color='blue')

# Configurar límites y etiquetas
plt.xlim(-5, 5)
plt.ylim(-5, 10)
plt.axhline(0, color='black',linewidth=0.5, ls='--')
plt.axvline(0, color='black',linewidth=0.5, ls='--')
plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5)
plt.title('Sistema de 2 Ecuaciones con 2 Incógnitas')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()

# Mostrar la gráfica
plt.show()