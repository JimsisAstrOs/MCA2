# Autor: Ortiz Jimena 

import numpy as np
import matplotlib.pyplot as plt

#------------------ Sistema inciso a) 

A_a = np.array([
    [1, 1/2, 1/3],
    [1/2, 1/3, 1/4],
    [1/3, 1/4, 1/5]
], dtype=float)



cond_a = np.linalg.norm(A_a, 1) * np.linalg.norm(np.linalg.inv(A_a), 1)
print("Condición (a):", cond_a)


#------------------ Sistema inciso b) 

A_b = np.array([
    [1,1,1,1],
    [1.01,1.02,1.03,1.04],
    [1.01**2,1.02**2,1.03**2,1.04**2],
    [1.01**3,1.02**3,1.03**3,1.04**3]
])

cond_b = np.linalg.norm(A_b, np.inf) * np.linalg.norm(np.linalg.inv(A_b), np.inf)
print("Condición (b):", cond_b)


#------------------ Sistema inciso c) 

A_c = np.array([
    [1,2],
    [2,4.0001]
])

#Eigenvalores 

eigvals = np.linalg.eigvals(A_c)
cond_c = max(eigvals)/min(eigvals)
print("Condición (c):", cond_c)


#----------------------- GRÁFICA SISTEMA (c) 

x = np.linspace (-10,10,100)

y1 = (3 - x)/2
y2 = (6.0001 - 2*x)/4.0001

plt.plot(x, y1, label="x + 2y = 3")
plt.plot(x, y2, label="2x + 4.0001y = 6.0001")

plt.legend()
plt.grid()
plt.title("Sistema (c)")
plt.show()