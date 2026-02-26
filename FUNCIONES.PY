import random

nombre_usuario1 = input("Ingresa nombre del jugador 1: ")
objetivo = int(input("Ingresa el objetivo: "))

def lanzamientos_hasta_objetivo(objetivo):
        
        if objetivo < 2 or objetivo > 12:
            raise ValueError("El número debe estar entre 2 y 12.")
        
        contador = 0
        
        while True:
            d1 = random.randint(1, 6)
            d2 = random.randint(1, 6)
            contador += 1
            
            print(f"Lanzamiento {contador}: Dado 1: {d1}, Dado 2: {d2} - Total: {d1 + d2}")
            
            if d1 + d2 == objetivo:
                return contador, d1, d2

lanzamientos, d1, d2 = lanzamientos_hasta_objetivo(objetivo)

print(f"\nSe necesitaron {lanzamientos} lanzamientos para alcanzar el objetivo")

if d1 == d2:
     print(f"Felicidades {nombre_usuario1} puedes sacar una ficha")
else:
    print("Turno del siguiente jugador")
