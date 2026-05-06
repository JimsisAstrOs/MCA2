#**Grafica Area entre curvas**
#Jimena Ortiz Trujillo

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-np.pi/3, np.pi/3, 400)

y1 = 1/(np.cos(x)**2)
y2 = 8*np.cos(x)

plt.plot(x, y1, label='y = sec^2(x)')
plt.plot(x, y2, label='y = 8*cos(x)')

plt.fill_between(x, y1, y2, where=(y2 >= y1), alpha=0.3)

plt.legend()
plt.title("Area entre curvas")
plt.grid()

plt.savefig("Grafica_Area_entre_curvas.png")
plt.show()
