import numpy as np

# Definindo as matrizes
A = np.array([[1, 2, 1], [2, -1, 1], [3, 1, -1]])
b = np.array([4, 1, 7])

# Resolvendo o sistema
x = np.linalg.solve(A, b)

print("A solução do sistema é:")
print(x)