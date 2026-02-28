nombre_usuario1= (input("Ingresa nombre del jugador 1:"))

import random

def lanzar_dados():
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)
    return dado1, dado2

# Ejemplo
d1, d2 = lanzar_dados()
print(f"Dado 1: {d1}, Dado 2: {d2}")
print("Total:", d1 + d2)

if d1 == d2:
     print(f"Felicidades {nombre_usuario1} puedes sacar una ficha")
else:
    print("turno del siguiente jugador")
