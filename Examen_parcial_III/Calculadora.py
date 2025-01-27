# Gracida Tapia Bryan.
# 25 de noviembre del 2024.
# Descripción:
# Calculadora basica.
import Menus
from colorama import Fore

# ///////////////////////////////////////////////////////////////////////////////////////// Función calculadora.
def validacion() -> list | None:
    """
    :return: retorna una lista con los numeros que ingreso el usuario una vez ya validados.
    """
    lista = []
    contador = 1
    numero_validado = 1
    print(Fore.MAGENTA + "Ingresa los numeros (Ingresa el numero 0 para terminar)\n")
    while numero_validado !=0 :
        numero = input(Fore.MAGENTA + f"numero {contador}:")
        numero_validado = Menus.cadena_a_flotante(numero)
        while numero_validado is None:
            numero = input(Fore.MAGENTA + "Opción no válida. Intente nuevamente: ")
            numero_validado = Menus.cadena_a_flotante(numero)
        lista.append(numero_validado)
        contador += 1
    return lista

# ///////////////////////////////////////////////////////////////////////////////////////// Función calculadora.
def calculadora (opcion: int, *vargs):
    """
    :param opcion:
    :return: retorna un valor de tipo float según la operacion que desea el usuario.
    """
    if opcion == 1:     # ................................ Suma.
        print(Fore.MAGENTA + f"La suma del los números es: {(sum(vargs)):.2f}")
        print()

    elif opcion == 2:       # ................................ Resta.
        resultado = vargs[0]
        for num in vargs[1:]:
            resultado -= num
        print(Fore.MAGENTA + f"La resta del los números es: {resultado:.2f}")
        print()

    elif opcion == 3:       # ................................ Multiplicación.
        resultado = 1
        for i in range(len(vargs) - 1):
            resultado *= vargs[i]
        print(Fore.MAGENTA + f"La multiplicación del los números es: {resultado:.2f}")
        print()
    elif opcion == 4:       # ................................ Potenciación.
        resultado = vargs[0]
        for i in range(len(vargs[1:]) - 1):
            resultado **= vargs[i]
        print(Fore.MAGENTA + f"La potenciación del los números es: {resultado:.2f}")
        print()
    elif opcion == 5:       # ................................ Salir del programa.
        print(Fore.MAGENTA + "Saliendo del programa...")

    else:
        print(Fore.MAGENTA + "Opcion no valida, intente de nuevo")


# ///////////////////////////////////////////////////////////////////////////////////////// Main.
def main() -> None:
    if __name__ == '__main__':
        opcion = 0
        numeros = []
        while opcion != 5 :
            opcion = Menus.menu_calculadora()
            if opcion != 5 and opcion <= 5:
                numeros = validacion()
            calculadora(opcion,*numeros)

        print()
        print("-----------------------------")
        print()


# ///////////////////////////////////////////////////////////////////////////////////////// Código a nivel de módulo.
main()

