# Gracida Tapia Bryan.
# 28 de octubre del 2024.
# Descripción:
# Tercer ejercicio del examen del parcial 1 modificado.
from random import randint

#/////////////////////////////////////////////////////////////////////////////////////////
# Cuarto ejercicio
print("  *** JUEGO DEl ADIVINADOR ***")

print("Ingrese la dificultad con la que desea jugar: ")
print("- Fácil.")
print("- Mediano.")
print("- Dificil.")
print("Elija una opción:")
opcion_elegida = input() # La opción elegida se tomara en cuenta para saber cuantos intentos tiene el ususario y el rango de números.
opcion_elegida = opcion_elegida.lower() # Utilizamos la palabra reservada lower para transformar el contenido char en minusculas, así teniendo mas facibilidad a la hora de aplicar las condiciones.
contador = 5
if opcion_elegida == "facil": #/////////////////////////////////////////// Nivel facil
    contador = 10 # El nivel facil tiene dies intentos.
    print(f"El CPU a elegido un número, tienes 10 intentos para adivinar el número")
    opcion_elegida_CPU = int(randint(1, 50)) # Con la condición randit generamos un número aleatorio entre 1 y 50
    while contador != 0:
        print("Ingresa un número entre 1 - 50:")
        numero = int(input()) # Se lee un número por consola y se realiza un casting a int.
        print()

        if numero != opcion_elegida_CPU and opcion_elegida_CPU > numero: # En caso que el número ingresado sea diferente y menor al número que eligio la CPU
            contador -= 1 # Se resta uno al contador cada vez que el usuario ingresa un número para así saber cuantos intentos le sobran.
            print(f"El número elejido por el CPU es mayor al número {numero}")
            print(f"Intento fallido, te quedan: {contador} intentos.")
            print()
        elif numero != opcion_elegida_CPU and opcion_elegida_CPU < numero: # En caso que el número ingresado sea diferente y mayor al número que eligio la CPU
            contador -= 1
            print(f"El número elejido por el CPU es menor al número {numero}")
            print(f"Intento fallido, te quedan: {contador} intentos.")
            print()
        elif numero == opcion_elegida_CPU: # En caso que el número ingresado sea igual al del CPU
            print(f"Felicidades adivinaste el número")
            print(opcion_elegida_CPU)
            contador = 0
            print()
        else:
            print("Perdiste")
            print(f"Ya no te quedan intentos, el numero elejido por el cpu era: {opcion_elegida_CPU}")
            print()
    print()
elif opcion_elegida == "mediano": #/////////////////////////////////////////// Nivel mediano
    contador = 5 # El nivel mediano tiene cinco intentos.
    print(f"El CPU a elegido un número, tienes 5 intentos para adivinar el número")
    opcion_elegida_CPU = int(randint(1, 100)) # Con la condición randit generamos un número aleatorio entre 1 y 100
    while contador != 0:
        print("Ingresa un número entre 1 - 100:")
        numero = int(input()) # Se lee un número por consola y se realiza un casting a int.
        print()

        if numero != opcion_elegida_CPU and opcion_elegida_CPU > numero: # En caso que el número ingresado sea diferente y menor al número que eligio la CPU
            contador -= 1 # Se resta uno al contador cada vez que el usuario ingresa un número para así saber cuántos intentos le sobran.
            print(f"El número elejido por el CPU es mayor al número {numero}")
            print(f"Intento fallido, te quedan: {contador} intentos.")
            print()
        elif numero != opcion_elegida_CPU and opcion_elegida_CPU < numero: # En caso que el número ingresado sea diferente y mayor al número que eligio la CPU
            contador -= 1
            print(f"El número elejido por el CPU es menor al número {numero}")
            print(f"Intento fallido, te quedan: {contador} intentos.")
            print()
        elif numero == opcion_elegida_CPU: # En caso que el numero ingresado sea igual al del CPU
            print(f"Felicidades adivinaste el número")
            print(opcion_elegida_CPU)
            contador = 0
            print()
        else:
            print("Perdiste")
            print(f"Ya no te quedan intentos, el numero elejido por el cpu era: {opcion_elegida_CPU}")
            print()
elif opcion_elegida == "dificil": #/////////////////////////////////////////// Nivel dificil
    contador = 4 # El nivel dificil tiene cuatro intentos.
    print(f"El CPU a elegido un número, tienes 4 intentos para adivinar el número")
    opcion_elegida_CPU = int(randint(1, 110)) # Con la condición randit generamos un número aleatorio entre 1 y 110
    while contador != 0:
        print("Ingresa un número entre 1 - 110:")
        numero = int(input()) # Se lee un número por consola y se realiza un casting a int.
        print()

        if numero != opcion_elegida_CPU and opcion_elegida_CPU > numero: # En caso que el número ingresado sea diferente y menor al número que eligio la CPU
            contador -= 1 # Se resta uno al contador cada vez que el usuario ingresa un número para así saber cuantos intentos le sobran.
            print(f"El número elejido por el CPU es mayor al número {numero}")
            print(f"Intento fallido, te quedan: {contador} intentos.")
            print()
        elif numero != opcion_elegida_CPU and opcion_elegida_CPU < numero: # En caso que el número ingresado sea diferente y mayor al número que eligio la CPU
            contador -= 1
            print(f"El número elejido por el CPU es menor al número {numero}")
            print(f"Intento fallido, te quedan: {contador} intentos.")
            print()
        elif numero == opcion_elegida_CPU: # En caso que el número ingresado sea igual al del CPU.
            print(f"Felicidades adivinaste el número")
            print(opcion_elegida_CPU)
            contador = 0
            print()
        else:
            print("Perdiste")
            print(f"Ya no te quedan intentos, el número elejido por el cpu era: {opcion_elegida_CPU}")
            print()
else: #/////////////////////////////////////////// Si se ingresa una opción que no esta válida terminara el programa.
    print("Opción no válida")

