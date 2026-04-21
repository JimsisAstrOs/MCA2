#Autor: Ortiz Jimena 

import numpy as np

# Matriz A (3x3)
A = np.array([
    [1, 1/2, 1/3],
    [1/2, 1/3, 1/4],
    [1/3, 1/4, 1/5]
])

# Eigenvalores y eigenvectores
valores, vectores = np.linalg.eig(A)


print("Eigenvalores:")
print(valores)

print("Eigenvectores:")
print(vectores)

