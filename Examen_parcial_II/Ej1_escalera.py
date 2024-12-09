# Gracida Tapia Bryan.
# 06 de Diciembre del 2024.
# Descripción:
# Creación del juego PIEDRA, PAPEL, TIJERAS, LAGARTO, SPOCK, de la serie de The Big Bang Theory, utilizando diccionarios.
import random


# ///////////////////////////////////////////////////////////////////////////////////////// Función menú.
def menu():
    print(" ** La escalera ** ")
    print("Ingrese el número de escalones deseados (positivo - ascendente ó negativo - descendente). \nSi desea salir ingrese un cero.")
    numero_ingresado = int(input("Ingresa número: "))
    return numero_ingresado

# ///////////////////////////////////////////////////////////////////////////////////////// Función para crear la escalera.
def crear_escalera(numero_ingresado):  # Cuando es un número positivo
    if numero_ingresado == 0:
        print("Saliendo...")
        return
    elif numero_ingresado < 0:  # Si se trata de un número negativo
        numero_ingresado = numero_ingresado * -1
        print("_")
        for j in range(0, numero_ingresado):
            print(f"{espacios * (j)}{escalon_descendente}")
    elif numero_ingresado > 0:  # Si se trata de un número positivo
        numero_ingresado = numero_ingresado * -1
        print(f"{espacios * (numero_ingresado * -1)}  _")
        for i in range(numero_ingresado, 0):
            print(f"{espacios * (i * -1)}{escalon_ascendente}")



espacios = "  "
escalon_ascendente = "_| "
escalon_descendente = " |_"

numero_ingresado = 1

while numero_ingresado != 0:
    numero_ingresado = menu()
    crear_escalera(numero_ingresado)

    print()
    print("-----------------------------")
    print()
