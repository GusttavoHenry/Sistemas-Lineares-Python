import numpy as np

# Definindo os coeficientes do sistema como uma matriz
A = np.array([[2, 3],
              [4, -1]])

# Definindo os termos independentes como um vetor
b = np.array([8, 7])

# Resolvendo o sistema
x = np.linalg.solve(A, b)

print("A solução do sistema é:")
print(x)