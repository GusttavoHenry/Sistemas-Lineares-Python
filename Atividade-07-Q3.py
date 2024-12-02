import numpy as np

# Definindo os coeficientes do sistema linear em forma de matriz
A = np.array([[3, -2, 4],
              [2, 1, -1],
              [1, -1, 3]])

# Definindo o vetor dos termos independentes
b = np.array([1, 2, 5])

# Resolvendo o sistema linear
x = np.linalg.solve(A, b)

print("A solução do sistema é:")
print(x)