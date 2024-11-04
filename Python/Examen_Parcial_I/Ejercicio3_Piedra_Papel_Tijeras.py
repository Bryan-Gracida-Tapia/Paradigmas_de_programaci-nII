# Gracida Tapia Bryan.
# 28 de octubre del 2024.
# Descripción:
# Tercer ejercicio del examen del parcial 1.
from random import randint

#/////////////////////////////////////////////////////////////////////////////////////////
# Tercer ejercicio
victoria,empate,victoria_CPU = 0, 0, 0
print("  *** PIEDRA, PAPEL O TIJERA ***")

contador = 0
while contador != 4:
    print(f"Victorias del jugador: {victoria}, Empates: {empate}, Victoria del CPU: {victoria_CPU}")
    print("1) Piedra.")
    print("2) Papel.")
    print("3) Tijera.")
    print("4) Salir.")
    print("Elija una opción:")
    opcion_elegida = int(input())
    opcion_elegida_CPU = int(randint (1,3))
    print(opcion_elegida_CPU)
    print()

    if opcion_elegida == 1 and opcion_elegida_CPU == 2:
        print(f"Victoria de CPU")
        victoria_CPU += 1
        print()
    elif opcion_elegida == 2 and opcion_elegida_CPU == 3:
        print(f"Victoria de CPU")
        victoria_CPU += 1
        print()
    elif opcion_elegida == 3 and opcion_elegida_CPU == 1:
        print(f"Victoria de CPU")
        victoria_CPU += 1
        print()
    elif opcion_elegida == 1 and opcion_elegida_CPU == 3:
        print(f"Victoria  de usuario")
        victoria += 1
        print()
    elif opcion_elegida == 2 and opcion_elegida_CPU == 1:
        print(f"Victoria  de usuario")
        victoria += 1
        print()
    elif opcion_elegida == 3 and opcion_elegida_CPU == 2:
        print(f"Victoria  de usuario")
        victoria += 1
        print()
    elif opcion_elegida == opcion_elegida_CPU:
        print(f"Empate")
        empate += 1
        print()
    elif opcion_elegida == 4:
        contador = 4
        print("saliendo del programa...")
    else:
        print("Opción no valida, intente de nuevo")