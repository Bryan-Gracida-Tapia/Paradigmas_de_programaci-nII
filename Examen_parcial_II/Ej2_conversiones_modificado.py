# Gracida Tapia Bryan.
# 08 de Diciembre del 2024.
# Descripción:
# Este programa realiza conversiones dependiendo el numero ingresado.
import random


# ///////////////////////////////////////////////////////////////////////////////////////// Función menú.
def menu():
    print("** Menú **")
    print("[1].- Convertir de decimal a binario y hexadecimal.")
    print("[2].- Convertir de binario a decimal y hexadecimal.")
    print("[3].- Convertir de hexadecimal a decimal y binario.")
    print("[4].- Suma de binarios.")
    print("[5].- Salir.")
    opcion_elejida = int(input("Ingresa número: "))
    return opcion_elejida

# ///////////////////////////////////////////////////////////////////////////////////////// Funciones para cada conversión.
def decimal_a_binario(numero_ingresado):        # ................................ Decimal a binario.
    lista_binario = []  # Lista vacía
    bandera = 0
    auxiliar = numero_ingresado

    while bandera == 0:
        digito_binario = auxiliar % 2
        lista_binario.append(digito_binario)
        auxiliar = auxiliar // 2  # Auxiliar será la divisón entera del número decimal entre dos.
        if auxiliar == 0 or auxiliar == 1:  # En caso de que la división entera tenga un valor de 1 o 0, se termina la conversión
            lista_binario.append(auxiliar)      # Se agrega el ultima residuo de la división entera.
            bandera = 1
    print(f"{numero_ingresado} en binario es:  0b" , end="")

    for i in range(1, len(lista_binario) + 1):      # Se invierte la lista.
        print(f"{lista_binario[i * -1]}",end="")

def decimal_a_hexadecimal(numero_ingresado):        # ................................ Decimal a hexadecimal.
    lista_hexadecimal = []  # Lista vacia
    conjunto_hexadecimal = ["A", "B", "C", "D", "E", "F"]
    auxiliar = numero_ingresado
    bandera = 0

    while bandera == 0:         # Se realiza la conversión
        digito_hexadecimal = auxiliar % 16
        if digito_hexadecimal >= 10 and digito_hexadecimal <= 15:   # En caso de que digito_hexadecimal se encuentre en un rago de 10 a 15 se replaza por un elemento del Conjunto hexadecimal.
            digito_hexadecimal = conjunto_hexadecimal[digito_hexadecimal - 10]
        lista_hexadecimal.append(digito_hexadecimal)
        auxiliar = auxiliar // 16       # Auxiliar será la divisón entera del número decimal entre diesiseis.
        if auxiliar == 0 or auxiliar == 1:      # En caso de que la división entera tenga un valor de 1 o 0, se termina la conversión
            lista_hexadecimal.append(auxiliar)      # Se agrega el ultima residuo de la división entera.
            bandera = 1

    print(f"{numero_ingresado} en hexadecimal es: 0x" , end="")
    for i in range(1, len(lista_hexadecimal) + 1):
        print(f"{lista_hexadecimal[i * -1]}", end="")

def binario_a_decimal(numero_ingresado):        # ................................ Binario a decimal.
    lista_digitos_binario = [int(numero) for numero in numero_ingresado]
    auxiliar = lista_digitos_binario
    numero_decimal = 0
    exponente = 0
    posicion = -1

    for i in auxiliar:      # Se reliza la conversión
        numero_decimal += (2 ** exponente) * auxiliar[posicion]
        exponente += 1
        posicion -= 1

    print(f"0b{numero_ingresado} en decimal es:" , end="")
    print(numero_decimal)

    return numero_decimal

def hexdecimal_a_decimal(numero_ingresado):         # ................................ hexadecimal a decimal.
    numero_decimal = 0
    exponente = 0
    posicion = -1
    lista_hexadecimal = [numero for numero in numero_ingresado]     # Se ingresa numero o caracter uno por uno, a una lista
    auxiliar = lista_hexadecimal

    for i in range(len(lista_hexadecimal)):     # Se remplazan los caracteres ingresados en la lista por numeros
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

    for i in auxiliar:      # Se realiza la conversión, una vez ya remplazados los elementos.
        numero_decimal += (16 ** exponente) * auxiliar[posicion]
        exponente += 1
        posicion -= 1

    print(f"0x{numero_ingresado} en decimal es: ", end="")
    print(numero_decimal)
    return numero_decimal


# ///////////////////////////////////////////////////////////////////////////////////////// Función de selección de función.
def seleccion(opcion):
    if opcion == 1:         # ................................ decimal a binario y hexadecimal.
        numero_ingresado = int(input("Ingrese un número decimal entero: "))
        # Se hace llamada a las conversiones necesarias.
        decimal_a_binario(numero_ingresado)
        print()
        decimal_a_hexadecimal(numero_ingresado)
    elif opcion == 2:       # ................................ binario a decimal y hexadecimal.
        numero_ingresado = input("Ingrese un número binario: ")
        # Se hace llamada a las conversiones necesarias.
        decimal = binario_a_decimal(numero_ingresado)
        print()
        decimal_a_hexadecimal(decimal)
    elif opcion == 3:       # ................................ hexadecimal a binario y decimal.
        numero_ingresado = input("Ingrese un número hexadecimal: ")
        # Se hace llamada a las conversiones necesarias.
        hexdecimal_a_decimal(numero_ingresado)
        print()
        decimal_a_binario(numero_ingresado)
    elif opcion == 4:
        primer_numero = input("Ingrese el primer número binario: ")
        segundo_numero = input("Ingrese el segundo número binario: ")
        primer_decimal = binario_a_decimal(primer_numero)
        segundo_decimal =  binario_a_decimal(segundo_numero)
        suma_decimal = primer_decimal + segundo_decimal
        decimal_a_binario(suma_decimal)

    elif opcion == 5:
        print("Saliendo...")
    else:
        print("Opción no válida :(")

# ///////////////////////////////////////////////////////////////////////////////////////// Código a nivel de módulo.

print(" *** Conversión entre las bases decimal, binaria y hexadecimal.  *** ")
opcion = 0
while opcion != 4:
    opcion = menu()
    seleccion(opcion)

    print()
    print("-----------------------------")
    print()

