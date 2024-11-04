# Gracida Tapia Bryan.
# 28 de octubre del 2024.
# Descripción:
# Primer ejercicio del examen del parcial 1.


#/////////////////////////////////////////////////////////////////////////////////////////
# Primer ejercicio
print("  *** EJERCICIO 1 - LICENCIATURA EN INFORMATICA ***")
numero = int(input("ingrese la cantidad de numeros a imprimir en consola: "))
print()
contador = 1

while contador <= numero:
    if ((contador % 5) == 0) and ((contador % 3) == 0):
        print("Licenciatura en Informatica")
    elif (contador % 5) == 0:
        print("Informatica, ", end=" ")
    elif (contador % 3) == 0:
        print("Licenciatura, ", end=" ")
    else:
        print(f"{contador}, ", end=" ")
    contador += 1
print("")
print("Fin de la cuenta")
