# Gracida Tapia Bryan.
# 25 de noviembre del 2024.
# Descripción:
# Calculadora basica.
import Menus
import Promedios
import Calculadora
import El_ahorcado
import Cuatro_en_raya
import Gato

from colorama import Fore

def main()->None:
    opcion = 0
    while opcion != 6:
        Gato.limpiar()
        print(Fore.CYAN + "ARCANE")
        opcion = Menus.menu()
        print()
        if opcion == 1:  # ................................ Juego Gato.
            opcion = Menus.menu_jugabilidad()
            if opcion == 1:
                Gato.jugador_vs_jugador()
            elif opcion == 2:
                Gato.jugar_vs_cpu()
            else:
                print(Fore.RED + "Saliendo del programa...")
        elif opcion == 2:  # ................................ Juego ahorcado.
            eleccion = 1
            opcion = 0
            while eleccion != 2 and opcion != 3:
                opcion = Menus.menu_jugabilidad()
                El_ahorcado.jugar_ahorcado(opcion)
                if opcion != 3:
                    eleccion = Menus.menu_repetir()
        elif opcion == 3:  # ................................ Juego cuatro en raya.
            eleccion = 1
            opcion = 0
            while eleccion != 2 and opcion != 3:
                opcion = Menus.menu_jugabilidad()
                if opcion == 1:
                    Cuatro_en_raya.jugar_vs_jugador()
                elif opcion == 2:
                    Cuatro_en_raya.jugar_vs_cpu()
                else:
                    print(Fore.RED + "Saliendo del programa...")
                if  opcion != 3:
                    eleccion = Menus.menu_repetir()

        elif opcion == 4:  # ................................ Calculadora.
            opcion_dos = 0
            numeros = []
            while opcion_dos != 5:
                opcion_dos = Menus.menu_calculadora()
                if opcion_dos != 5 and opcion_dos <= 5:
                    numeros = Calculadora.validacion()
                Calculadora.calculadora(opcion_dos, *numeros)
        elif opcion == 5:  # ................................ Promedio.
            Promedios.ingresar_materias_promedios()
        elif opcion == 6:  # ................................ Salir del programa.
            print("Saliendo del programa...")
        else:
            print("Opcion no valida, intente de nuevo")

        print()
        print(Fore.BLACK + "-----------------------------")
        print()

main()
