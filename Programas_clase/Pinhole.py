import numpy as np

# 1. Distancia focal

f = 50

# 2. Puntos en 3D (X,Y,Z)

puntos_3D = np.array([
    [2, 2, 10],
    [4, 2, 10],
    [2, 4, 20],
    [3, 3, 15]
])

# 3. Proyección Pinhole

print("Proyección usando modelo Pinhole:\n")

for punto in puntos_3D:
    X, Y, Z = punto
    
    x = (f * X) / Z
    y = (f * Y) / Z
    
    print(f"Punto 3D: ({X}, {Y}, {Z})")
    print(f"Proyección 2D: ({x:2f}, {y:2f})")
    print("-" * 40)
    