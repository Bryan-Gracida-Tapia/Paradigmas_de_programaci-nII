# Gracida Tapia Bryan.
# 06 de Diciembre del 2024.
# Descripción:
# Creación del juego PIEDRA, PAPEL, TIJERAS, LAGARTO, SPOCK, de la serie de The Big Bang Theory, utilizando diccionarios.
import random

from Examen_parcial_II.Ej1_escalera import numero_ingresado


# ///////////////////////////////////////////////////////////////////////////////////////// Función menú.
def menu():
    print("\n------------------------------------------ ")
    print("** MENÚ **")
    print("[1].- Convertir de decimal a binario y hexadecimal.")
    print("[2].- Convertir de binario a decimal y hexadecimal.")
    print("[3].- Convertir de hexadecimal a decimal y binario.")
    print("[4].- Salir.")
    opcion_elejida = int(input("Ingresa número: "))
    return opcion_elejida

def decimal_a_binario(numero_ingresado):
    lista_binario = []  # Lista vacía
    bandera = 0
    auxiliar = numero_ingresado
    # Para convertir de decimal a binario

    while bandera == 0:
        digito_binario = auxiliar % 2  # Dígito binario será igual a 1 o 0
        lista_binario.append(digito_binario)  # Agrega el 1 o 0, según corresponda a la lista_binario
        auxiliar = auxiliar // 2  # Ahora numero_decimal_auxiliar será la divisón entera del número decimal entre dos
        if auxiliar == 0 or auxiliar == 1:  # Sí el resultado de la división entera del numero decimal entre dos es 1 o 0, significa que debe terminar el ciclo
            lista_binario.append(auxiliar)
            bandera = 1
    print(f"{numero_ingresado} en binario es: ")
    # Invertir lista
    for i in range(1, len(lista_binario) + 1):
        print(f"{lista_binario[i * -1]}",end="")  # imprime la lista desde -1 hasta -n, donde -n es el número total de elementos de la lista, recordando que el índice -1 refiere al último elemento de la lista

def decimal_a_hexadecimal(numero_ingresado):
    # Para convertir de decimal a hexadecimal
    lista_hexadecimal = []
    conjunto_hexadecimal = ["A", "B", "C", "D", "E", "F"]
    auxiliar = numero_ingresado  # Reinicio el número decimal auxiliar
    bandera = 0

    while bandera == 0:
        digito_hexadecimal = auxiliar % 16
        if digito_hexadecimal >= 10 and digito_hexadecimal <= 15:
            digito_hexadecimal = conjunto_hexadecimal[digito_hexadecimal - 10]
        lista_hexadecimal.append(digito_hexadecimal)
        auxiliar = auxiliar // 16
        if auxiliar == 0 or auxiliar == 1:
            lista_hexadecimal.append(auxiliar)
            bandera = 1

    print(f"{numero_ingresado} en hexadecimal es: ")
    for i in range(1, len(lista_hexadecimal) + 1):
        print(f"{lista_hexadecimal[i * -1]}", end="")

def binario_a_decimal(numero_ingresado):
    lista_digitos_binario = [int(numero) for numero in numero_ingresado]
    auxiliar = lista_digitos_binario
    numero_decimal = 0
    exponente = 0
    posicion = -1
    # Para convertir de binario a decimal
    for i in auxiliar:
        numero_decimal += (2 ** exponente) * auxiliar[posicion]
        exponente += 1
        posicion -= 1
    print(f"{numero_ingresado} en decimal es:")
    print(numero_decimal)

    return numero_decimal

def hexdecimal_a_decimal(numero_ingresado):
    numero_hexadecimal = input("Ingrese número hexadecimal: ")
    lista_hexadecimal = [numero for numero in numero_hexadecimal]
    auxiliar = lista_hexadecimal

    for i in range(len(lista_hexadecimal)):
        if lista_hexadecimal[i] == "A":
            auxiliar[i] = 10
        elif lista_hexadecimal[i] == "B":
            auxiliar[i] = 11
        elif lista_hexadecimal[i] == "C":
            auxiliar[i] = 12
        elif lista_hexadecimal[i] == "D":
            auxiliar[i] = 13
        elif lista_hexadecimal[i] == "E":
            auxiliar[i] = 14
        elif lista_hexadecimal[i] == "F":
            auxiliar[i] = 15
        else:
            auxiliar[i] = int(auxiliar[i])

    numero_decimal = 0
    exponente = 0
    digito_invertido = -1
    for i in auxiliar:
        numero_decimal += (16 ** exponente) * auxiliar[digito_invertido]
        exponente += 1
        digito_invertido -= 1
    print(f"{numero_hexadecimal} en decimal es: ", end="")
    print(numero_decimal)
    return numero_decimal

def decimal_a_binario_hexadecimal(numero_ingresado):
    decimal_a_binario(numero_ingresado)
    print()
    decimal_a_hexadecimal(numero_ingresado)


def binario_a_decimal_hexadecimal(numero_ingresado):
    decimal = binario_a_decimal(numero_ingresado)
    print()
    decimal_a_hexadecimal(decimal)

def hexadecimal_a_decimal_binario(numero_ingresado):
    hexdecimal_a_decimal(numero_ingresado)


def conversion(opcion):
    if opcion == 1:
        numero_ingresado = int(input("Ingrese un número decimal entero: "))
        decimal_a_binario_hexadecimal(numero_ingresado)
    elif opcion == 2:
        numero_ingresado = input("Ingrese un número binario: ")
        binario_a_decimal_hexadecimal(numero_ingresado)
    elif opcion == 3:
        numero_ingresado = input("Ingrese un número hexadecimal: ")
        hexadecimal_a_decimal_binario(numero_ingresado)
    elif opcion == 4:
        print("Saliendo...")
    else:
        print("Opción no válida :(")


print(" *** Conversión entre las bases decimal, binaria y hexadecimal.  *** ")

opcion = 0
while opcion != 4:
    opcion = menu()
    conversion(opcion)




