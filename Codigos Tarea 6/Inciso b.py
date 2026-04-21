#Autor:Ortiz Jimena

import numpy as np

# Valores
x = [1.01, 1.02, 1.03, 1.04]

# Matriz de Vandermonde
A = np.array([
    [1, 1, 1, 1],
    [1.01, 1.02, 1.03, 1.04],
    [1.01**2, 1.02**2, 1.03**2, 1.04**2],
    [1.01**3, 1.02**3, 1.03**3, 1.04**3]
])

# Eigenvalores y eigenvectores

valores, vectores = np.linalg.eig(A)

print("Eigenvalores:")
print(valores)

print("Eigenvectores:")
print(vectores)