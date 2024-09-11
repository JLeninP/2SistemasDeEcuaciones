import sys
import numpy as np

A: np.ndarray = np.array([
    [0.52, 0.20, 0.25],
    [0.30, 0.50, 0.20],
    [0.18, 0.30, 0.55]
])

b: np.ndarray = np.array([[4800],
             [5810],
             [5690]
             ])

sys.stdout.write("\n\tMATRIZ INVERSA\n")
A_inv: np.ndarray = np.linalg.inv(A)
sys.stdout.write(str(A_inv))

sys.stdout.write("\n\n\tMATRIZ X (SOLUCIÓN)\n")
X: np.ndarray = np.dot(A_inv, b)
sys.stdout.write(str(X))
