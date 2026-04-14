import numpy as np

# 1. PUntos en 3D (X,Y,Z,1)
X = np.array([
    [2, 2, 10, 1],
    [4, 2, 20, 1],
    [2, 4, 20, 1],
    [3, 3, 15, 1]
])

#2. Puntos en la imagen (x, y)
x = np.array([
    [110, 210],
    [150, 210],
    [90, 230],
    [120, 220]
])

# 3. Construcción de la matriz A
A = []

for i in range(len(x)):
    X_i = X[i]
    x_i, y_i = x[i]

    fila1 = np.hstack([X_i, np.zeros(4), -x_i * X_i])
    fila2 = np.hstack([np.zeros(4), X_i, -y_i * X_i])

    A.append(fila1)
    A.append(fila2)

A = np.array(A)

# 4.Resolver con SVD
U, S, Vt = np.linalg.svd(A)

#Última fila de V transpuesta
P = Vt[-1].reshape(3, 4)

# 5. Mostrar resultados
print("Matriz A:")
print(A)

print("\nMatriz de proyección P:")
print(P)

# 6. Verificación

print("\nVerificación (P * X):")

for i in range(len(X)):
    X_i = X[i]
    resultado = P @ X_i
    
    #Normalización homogénea
    resultado = resultado / resultado[2]
    
    print(f"Punto 3D: {X_i}")
    print(f"Proyección estimada: ({resultado[0]:.2f}, {resultado[1]:.2f})")
    print(f"Proyección real: {x[i]}")
    print("-" * 40)
    