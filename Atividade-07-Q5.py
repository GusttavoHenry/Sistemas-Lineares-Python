import numpy as np

# Definindo os coeficientes do sistema como uma matriz
A = np.array([[1, 3, 1],
              [2, -1, 2],
              [1, 2, -1]])

# Definindo os termos independentes como um vetor
b = np.array([10, 5, 2])

# Resolvendo o sistema
x = np.linalg.solve(A, b)

print("A solução do sistema é:")
print(x)