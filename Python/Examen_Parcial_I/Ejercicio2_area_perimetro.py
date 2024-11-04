# Gracida Tapia Bryan.
# 28 de octubre del 2024.
# Descripción:
# Segundo ejercicio del examen del parcial 1.


#/////////////////////////////////////////////////////////////////////////////////////////
# Segundo ejercicio
pi = 3.1416
contador = 0
while contador != 4:
    print("1) Calcular el área de un rectángulo.")
    print("2) Calcular el perímetro de un rectángulo.")
    print("3) Calcular el área de un círculo.")
    print("4) Calcular el perímetro de un círculo.")
    print("5) Salir.")

    opcion_elegida = int(input())

    if opcion_elegida == 1:
        primer_numero = float(input("Ingrese el largo del rectangulo en centimetros"))
        segundo_numero = float(input("Ingrese el ancho del rectangulo en centimetros"))

        print(f"El area del rectangulo con {primer_numero}cm de largo y {segundo_numero}cm de ancho es: {(primer_numero * segundo_numero):.2f}")
        print()
    elif opcion_elegida == 2:
        primer_numero = float(input("Ingrese el largo del rectangulo en centimetros"))
        segundo_numero = float(input("Ingrese el ancho del rectangulo en centimetros"))

        print(f"El perimetro del rectangulo con {primer_numero}cm de largo y {segundo_numero}cm de ancho es: {((primer_numero * 2) + (segundo_numero * 2)):.2f}")
        print()
    elif opcion_elegida == 3:
        primer_numero = float(input("Ingrese el radio del circulo"))

        print(f"El area del circulo con un radio de {primer_numero} es de: {(pi * (primer_numero ** 2)):.2f}")
        print()
    elif opcion_elegida == 4:
        primer_numero = float(input("Ingrese el radio del circulo"))

        print(f"El perimetro del circulo con un radio de {primer_numero} es de: {(pi * (primer_numero * 2)):.2f}")
        print()
    elif opcion_elegida == 5:
        contador = 4
        print("Saliendo del programa...")
    else:
        print("Opcion no valida, intente de nuevo")
