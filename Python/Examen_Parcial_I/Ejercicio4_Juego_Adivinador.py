# Gracida Tapia Bryan.
# 28 de octubre del 2024.
# Descripción:
# Tercer ejercicio del examen del parcial 1.
from random import randint

#/////////////////////////////////////////////////////////////////////////////////////////
# Tercer ejercicio
print("  *** JUEGO DEl ADIVINADOR ***")

print(f"El CPU a elegido un número, tienes 5 intentos para adivinar el número")
opcion_elegida_CPU = int(randint (1,100))
contador = 5
while contador != 0:
    print("Ingresa un número entre 1 - 100:")
    numero = int(input())
    
    print()

    if numero != opcion_elegida_CPU and opcion_elegida_CPU > numero:
        contador -= 1
        print(f"El número elejido por el CPU es mayor al número {numero}")
        print(f"Intento fallido, te quedan: {contador} intentos.")
        print()
    elif numero != opcion_elegida_CPU and opcion_elegida_CPU < numero:
        contador -= 1
        print(f"El número elejido por el CPU es menor al número {numero}")
        print(f"Intento fallido, te quedan: {contador} intentos.")
        print()
    elif numero == opcion_elegida_CPU :
        print(f"Felicidades adivinaste el número")
        print(opcion_elegida_CPU)
        contador = 0
        print()
    elif contador == 1:
        print("Perdiste")
        print(f"Ya no te quedan intentos, el numero elejido por el cpu era: {opcion_elegida_CPU}")
        print()
    else:
        print("Opción no válida, intente de nuevo")