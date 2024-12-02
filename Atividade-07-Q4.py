import numpy as np

# Definindo os coeficientes das equações em uma matriz A
A = np.array([[1, 1],
              [2, 3]])

# Definindo os termos independentes em um vetor b
b = np.array([5, 10])

# Resolvendo o sistema linear
x = np.linalg.solve(A, b)

print("A solução do sistema é:")
print(x)