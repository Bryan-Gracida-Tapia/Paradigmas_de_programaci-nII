# Gracida Tapia Bryan.
# 28 de octubre del 2024.
# Descripción:
# Tercer ejercicio del examen del parcial 1 modificado.
from random import randint

#/////////////////////////////////////////////////////////////////////////////////////////
# Tercer ejercicio
victoria,empate,victoria_CPU = 0, 0, 0
print("  *** PIEDRA, PAPEL O TIJERA ***")

contador = 0
while contador != 4:
    print(f"Victorias del jugador: {victoria}, Empates: {empate}, Victoria del CPU: {victoria_CPU}")
    print("- Piedra.")
    print("- Papel.")
    print("- Tijera.")
    print("- Salir.")
    print("Elija una opción:")
    opcion_elegida = input()
    opcion_elegida = opcion_elegida.lower()
    opcion_elegida_CPU = int(randint (1,3))
    print(opcion_elegida_CPU)
    print()

    if (opcion_elegida == "piedra" and opcion_elegida_CPU == 3) or (opcion_elegida == "papel" and opcion_elegida_CPU == 1) or (opcion_elegida == "tijera" and opcion_elegida_CPU == 2):
        print(f"Victoria de CPU")
        victoria_CPU += 1
        print()
    elif (opcion_elegida == "piedra" and opcion_elegida_CPU == 2) or (opcion_elegida == "papel" and opcion_elegida_CPU == 3) or (opcion_elegida == "tijera" and opcion_elegida_CPU == 1):
        print(f"Victoria  de usuario")
        victoria += 1
        print()
    elif (opcion_elegida == "piedra" and opcion_elegida_CPU == 1) or (opcion_elegida == "papel" and opcion_elegida_CPU == 2) or (opcion_elegida == "tijera" and opcion_elegida_CPU == 3):
        print(f"Empate")
        empate += 1
        print()
    elif opcion_elegida == "salir":
        contador = 4
        print("saliendo del programa...")
    else:
        print("Opción no valida, intente de nuevo")