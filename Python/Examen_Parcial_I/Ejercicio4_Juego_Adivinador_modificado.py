# Gracida Tapia Bryan.
# 28 de octubre del 2024.
# Descripción:
# Tercer ejercicio del examen del parcial 1 modificado.
from random import randint

#/////////////////////////////////////////////////////////////////////////////////////////
# Cuarto ejercicio
print("  *** JUEGO DEl ADIVINADOR ***")

print(f"El CPU a elegido un número, tienes 5 intentos para adivinar el número")
opcion_elegida_CPU = int(randint (1,100))

print("Ingrese la dificultad con la que desea jugar: ")
print("- Fácil.")
print("- Mediano.")
print("- Dificil.")
print("Elija una opción:")
opcion_elegida = input()
opcion_elegida = opcion_elegida.lower()
contador = 5
if opcion_elegida == "facil":
    contador = 10
    print(f"El CPU a elegido un número, tienes 10 intentos para adivinar el número")
    opcion_elegida_CPU = int(randint(1, 50))
    while contador != 0:
        print("Ingresa un número entre 1 - 50:")
        numero = int(input())
        print(opcion_elegida_CPU)
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
        elif numero == opcion_elegida_CPU:
            print(f"Felicidades adivinaste el número")
            print(opcion_elegida_CPU)
            contador = 0
            print()
        else:
            print("Perdiste")
            print(f"Ya no te quedan intentos, el numero elejido por el cpu era: {opcion_elegida_CPU}")
            print()
    print()
elif opcion_elegida == "mediano":
    contador = 5
    print(f"El CPU a elegido un número, tienes 5 intentos para adivinar el número")
    opcion_elegida_CPU = int(randint(1, 100))
    while contador != 0:
        print("Ingresa un número entre 1 - 100:")
        numero = int(input())
        print(opcion_elegida_CPU)
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
        elif numero == opcion_elegida_CPU:
            print(f"Felicidades adivinaste el número")
            print(opcion_elegida_CPU)
            contador = 0
            print()
        else:
            print("Perdiste")
            print(f"Ya no te quedan intentos, el numero elejido por el cpu era: {opcion_elegida_CPU}")
            print()
elif opcion_elegida == "dificil":
    contador = 4
    print(f"El CPU a elegido un número, tienes 4 intentos para adivinar el número")
    opcion_elegida_CPU = int(randint(1, 110))
    while contador != 0:
        print("Ingresa un número entre 1 - 110:")
        numero = int(input())
        print(opcion_elegida_CPU)
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
        elif numero == opcion_elegida_CPU:
            print(f"Felicidades adivinaste el número")
            print(opcion_elegida_CPU)
            contador = 0
            print()
        else:
            print("Perdiste")
            print(f"Ya no te quedan intentos, el numero elejido por el cpu era: {opcion_elegida_CPU}")
            print()
else:
    print("Opción no válida, intente de nuevo")

