# Gracida Tapia Bryan.
# 26 de Enero del 2025.
# Descripción:
# Menús que se utilizan en el programa.
from colorama import Fore
# ///////////////////////////////////////////////////////////////////////////////////////// Menu Selección.
def menu():
    """

    :return: retorna un valor entero según haya elegido el usuario.
    """
    print(Fore.CYAN + "     *** Menú ***")
    print(Fore.CYAN + "[1].- Juego del Gato")
    print(Fore.CYAN +"[2].- Juego del Ahorcado")
    print(Fore.CYAN +"[3].- Juego del Cuatro en Raya")
    print(Fore.CYAN +"[4].- Calculadora")
    print(Fore.CYAN +"[5].- Promedios")
    print(Fore.RED +"[6].- Salir")
    opcion = input(Fore.WHITE + "Selecciona una opción: ")
    while not opcion.isnumeric() or int(opcion) not in range(1, 7):
        print(Fore.RED + "Opción no válida. Intenta de nuevo")
        opcion = input(Fore.WHITE + "Selecciona una opción: ")
    return int(opcion)

# ///////////////////////////////////////////////////////////////////////////////////////// Menu Jugabilidad.
def menu_jugabilidad():
    """

    :return: retorna un valor entero según haya elegido el usuario.
    """
    print(Fore.BLUE +"*** Modo de juego ***")
    print(Fore.BLUE + "[1].- Jugador contra jugador")
    print(Fore.BLUE + "[2].- Jugador con CPU")
    print(Fore.BLUE + "[3].- Salir")
    opcion = input(Fore.BLUE +  "Selecciona una opción: ")
    while not opcion.isnumeric() or int(opcion) not in range(1, 4):
        print(Fore.BLUE + "Opción no válida. Intenta de nuevo")
        opcion = input(Fore.BLUE + "Selecciona una opción: ")
    return int(opcion)

# ///////////////////////////////////////////////////////////////////////////////////////// Menu repetir.
def menu_repetir():
    """

    :return: retorna un valor entero según haya elegido el usuario.
    """
    print(Fore.YELLOW + "*** Volver a jugar ***")
    print(Fore.YELLOW + "[1].- Si")
    print(Fore.YELLOW + "[2].- No")
    opcion = input(Fore.YELLOW + "Selecciona una opción: ")
    while not opcion.isnumeric() or int(opcion) not in range(1, 3):
        print(Fore.YELLOW + "Opción no válida. Intenta de nuevo")
        opcion = input(Fore.YELLOW + "Selecciona una opción: ")
    return int(opcion)

# ///////////////////////////////////////////////////////////////////////////////////////// Menu Calculadora.
def menu_calculadora():
    """

    :return: retorna un valor entero según haya elegido el usuario.
    """
    print(Fore.YELLOW + "*** Menú Calculadora ***")
    print(Fore.YELLOW + "1) Suma.")
    print(Fore.YELLOW + "2) Resta.")
    print(Fore.YELLOW + "3) Multiplicación.")
    print(Fore.YELLOW + "4) Potenciación.")
    print(Fore.RED + "5) Salir.")

    opcion = input(Fore.WHITE + "Selecciona una opción: ")
    while not opcion.isnumeric() or int(opcion) not in range(1, 6):
        print(Fore.RED + "Opción no válida. Intenta de nuevo")
        opcion = input(Fore.WHITE + "Selecciona una opción: ")
    return int(opcion)


# ///////////////////////////////////////////////////////////////////////////////////////// Función cadena a flotante.
def cadena_a_flotante(cadena: str) -> float | None:
    """
    Convierte la cadena recibida a un entero en caso de que sea número, de lo contrario vuelve a pedir un número.
    :param cadena: Recibe la cadena a convertir.
    :return: El número flotante o None de no ser válido..
    """
    numero_puntos = cadena.count(".")
    revisar_cadena = cadena.replace(".", "").lstrip("-")
    if revisar_cadena.isnumeric() and numero_puntos in (0, 1):
        return float(cadena)
    else:
        return None
