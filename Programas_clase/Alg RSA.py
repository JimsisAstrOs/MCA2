import math

#1. Elegir números primos

p = 101
q = 113

# 2. Calcular n

n = p * q

# 3. CAlcular phi(n)

phi = (p - 1) * (q - 1)

#4. Elegir e

e = 17 # debe ser coprimo con phi

#verificación

if math.gcd(e, phi) != 1:
    raise ValueError("e no es coprimo con phi(n)")

#5. Calcular d ( inverso )

def inverso_modular(e, phi):
    for d in range(1, phi):
        if (e * d) % phi == 1:
            return d
        
d = inverso_modular(e, phi)

#6. Mostrar resultados 

print("Valores:")
print(f"p = {p}, q = {q}")
print(f"n = {n}")
print(f"phi(n) = {phi}")

print("\nLlave pública (n, e):")
print((n, e))

print("\nLlave privada (n, d):")
print((n, d))
