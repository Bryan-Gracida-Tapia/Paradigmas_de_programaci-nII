# Gracida Tapia Bryan.
# 28 de octubre del 2024.
# Descripción:
# Tercer ejercicio del examen del parcial 1 modificado.
from random import randint

#/////////////////////////////////////////////////////////////////////////////////////////
# Tercer ejercicio
victoria,empate,victoria_CPU = 0, 0, 0
print("  *** PIEDRA, PAPEL O TIJERA ***")

contador = 0 # se crea un contador para así poder crear una bandera.
while contador != 4:
    print(f"Victorias del jugador: {victoria}, Empates: {empate}, Victoria del CPU: {victoria_CPU}") # Se imprime este letrero para asi tener un registro de los resultados de los juegos.
    print("- Piedra.")
    print("- Papel.")
    print("- Tijera.")
    print("- Salir.")
    print("Elija una opción:")
    opcion_elegida = input() # La opción elegida se se convertira a minúsculas para así tener una fácil manipulación en las cóndiciones .
    opcion_elegida = opcion_elegida.lower()
    opcion_elegida_CPU = int(randint (1,3)) # Con la condición randit generamos un número aleatorio entre 1 y 3
    print(opcion_elegida_CPU)
    print()

    if (opcion_elegida == "piedra" and opcion_elegida_CPU == 3) or (opcion_elegida == "papel" and opcion_elegida_CPU == 1) or (opcion_elegida == "tijera" and opcion_elegida_CPU == 2): # Condiciones para que gane el CPU, recordando que todos las combinaciones estan al reves.
        print(f"Victoria de CPU")
        victoria_CPU += 1 # Se realiza un incremento unitario cada vez que gane el CPU.
        print()
    elif (opcion_elegida == "piedra" and opcion_elegida_CPU == 2) or (opcion_elegida == "papel" and opcion_elegida_CPU == 3) or (opcion_elegida == "tijera" and opcion_elegida_CPU == 1): # Condiciones para que gane el usuario.
        print(f"Victoria  de usuario")
        victoria += 1 # Se realiza un incremento unitario cada vez que gane el usuario.
        print()
    elif (opcion_elegida == "piedra" and opcion_elegida_CPU == 1) or (opcion_elegida == "papel" and opcion_elegida_CPU == 2) or (opcion_elegida == "tijera" and opcion_elegida_CPU == 3): # Condiciones para que realice un empate
        print(f"Empate")
        empate += 1 # Se realiza un incremento unitario cuando usuario y CPU eligan la misma opción.
        print()
    elif opcion_elegida == "salir": # se toma esta condición cuando se desea salir del programa.
        contador = 4 # se reliza una bandera para asi romper el ciclo while
        print("saliendo del programa...")
    else:
        print("Opción no valida, intente de nuevo")