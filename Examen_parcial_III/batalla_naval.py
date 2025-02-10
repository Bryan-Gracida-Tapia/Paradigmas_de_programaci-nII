# Gracida Tapia Bryan.
# 10 de febrero del 2025.
# Descripción:
# Juego de la gerra naval con dos modos de juego: Jugador contra Jugador y Jugador contra CPU.
import random
import Menus
from colorama import Fore

# ///////////////////////////////////////////////////////////////////////////////////////// Función para limpiar la pantalla.
def limpiar() -> None :
    """
    Imprime varias lineas en blanco, para simular una pantalla limpia.
    """
    print("\n" * 50)

# ///////////////////////////////////////////////////////////////////////////////////////// Función crear y mostrar el tablero.
def crear_tablero() -> list:
    """
    Crea un tablero vacío de 7 filas por 7 columnas.
    :return: Regresa el tablero en forma de lista.
    """
    return [[" " for _ in range(7)] for _ in range(7)]

def mostrar_tablero(tablero) -> None:
    """
    Muestra el tablero en pantalla.
    :param:recibe el tablero vacio o con las fichas existentes, y posteriormente lo imprime en pantalla
    """
    print(" 1    2    3    4    5    6    7")
    print("---------------------------------")
    for fila in tablero:
        print("|" + "|".join(f" {celda} " for celda in fila) + "|")
        print("---------------------------------")


# ///////////////////////////////////////////////////////////////////////////////////////// Funciones de validación.
def colocar_ficha(tablero, fila, columna, ficha) -> bool:
    """
    Coloca una ficha en la posición indicada si es posible.
    :param tablero: recibe el tablero con las fichas que esten existentes.
    :param fila: recibe el valor de la fila disponible.
    :param columna: recibe la columna elejida por el usuario.
    :param ficha: recibe X o O dependiendo de la ficha que toque verificar.
    :return: Regresa un valor booleano dependiendo si es posible colocar la ficha o no.
    """

    if tablero[fila][columna] == " ":
        tablero[fila][columna] = ficha
        return True
    return False

# ///////////////////////////////////////////////////////////////////////////////////////// funcion batalla naval.
def colocar_barcos(tablero,barcos,turno) -> None:
    """
    Se colocan barcos en un tablero, dependiendo del turno..
    :param tablero: tablero que guardara la ubicación de los barcos
    """
    contador = 0
    ficha = "🚤"
    while contador < barcos:
        limpiar()
        contador += 1
        mostrar_tablero(tablero)
        print(f"Truno de jugador {turno} de colocar barcos")
        while True:
            entrada = input("Elige fila y columna (formato: fila columna): ").split()
            if len(entrada) == 2 and all(x.isdigit() for x in entrada):
                fila, columna = int(entrada[0]) - 1, int(entrada[1]) - 1
                if 0 <= fila < 7 and 0 <= columna < 7 and colocar_ficha(tablero, fila, columna, ficha):
                    break
                print("Casilla ocupada o fuera de rango. Intenta de nuevo.")
            else:
                print("Entrada inválida. Ingresa dos números separados por un espacio.")

# ///////////////////////////////////////////////////////////////////////////////////////// Colocar bombas.
def colocar_bombas(tablero_tiros,turno) -> None:
    """
    se colocan bombas en un tablero, dependiendo del turno.
    :param tablero_tiros: tablero con el registro de los tiros ya hechos
    :param turno: turno sea jugador 1 o 2 o CPU
    """

    contador = 0
    ficha = "☄️"
    while contador < 1:
        limpiar()
        contador += 1
        mostrar_tablero(tablero_tiros)
        print(f"Turno de jugador {turno}")
        while True:
            entrada = input("Elige fila y columna (formato: fila columna): ").split()
            if len(entrada) == 2 and all(x.isdigit() for x in entrada):
                fila, columna = int(entrada[0]) - 1, int(entrada[1]) - 1
                if 0 <= fila < 7 and 0 <= columna < 7 and colocar_ficha(tablero_tiros, fila, columna, ficha):
                    break
                print("Casilla ocupada o fuera de rango. Intenta de nuevo.")
            else:
                print("Entrada inválida. Ingresa dos números separados por un espacio.")

# ///////////////////////////////////////////////////////////////////////////////////////// Verificar impactos.
def verificar_impactos(tablero_barcos,tablero_tiros) -> bool:
    """
    Compara los tableros de barcos y tiros para verificar si las bombas acertaron.
    :param tablero_barcos: Tablero con la ubicación de los barcos.
    :param tablero_tiros: Tablero con las ubicaciones de los tiros.
    """
    for fila in range(7):
        for columna in range(7):
            if tablero_barcos[fila][columna] == "🚤" and tablero_tiros[fila][columna] == "☄️":
                tablero_barcos[fila][columna] = "💢"
                tablero_tiros[fila][columna] = "💢"

                print(f"Impacto en ({fila + 1}, {columna + 1})")
                return True
    return False

def alternar_tiros(tablero_jugador1,tablero_jugador2,barcos) -> None:
    """
    Compara los tableros de barcos y tiros para verificar si las bombas acertaron.
    :param tablero_jugador1: Tablero con la ubicación de los barcos del primer jugador.
    :param tablero_jugador2: Tablero con las ubicaciones de los barcos del segundo jugador.
    :param barcos: Cantidad de barcos segun el modo de juego.
    """
    tablero_tiros_jugador1 = crear_tablero()
    tablero_tiros_jugador2 = crear_tablero()
    turno = 0
    barcos_vivos_jugador1 = barcos
    barcos_vivos_jugador2 = barcos
    while barcos_vivos_jugador1 != 0 or barcos_vivos_jugador2 != 0:
        if turno % 2 == 1:
            turno += 1
            colocar_bombas(tablero_tiros_jugador1, turno=1)
            while verificar_impactos(tablero_jugador2, tablero_tiros_jugador1) and barcos_vivos_jugador2 != 0:
                colocar_bombas(tablero_tiros_jugador1, turno=1)
                barcos_vivos_jugador2 -= 1

        else:
            colocar_bombas(tablero_tiros_jugador2, turno=2)
            while verificar_impactos(tablero_jugador1, tablero_tiros_jugador2) and barcos_vivos_jugador1 != 0:
                colocar_bombas(tablero_tiros_jugador2, turno=2)
                barcos_vivos_jugador1 -= 1

        if barcos_vivos_jugador2 == 0:
            print("Gana el jugador 1")
            break
        if barcos_vivos_jugador1 == 0:
            print("Gana el jugador 2")
            break


# ///////////////////////////////////////////////////////////////////////////////////////// Función main.
def ejecutar_batalla_naval() -> None:
    """
    Función donde se encuentra las llamadas a funciones principales..
    :return:
    """
    if __name__ == "__main__":
        barcos =0
        opcion = Menus.menu_jugabilidad()
        dificultad = Menus.menu_modo_juego()
        if dificultad == 1:
            barcos = 3
        elif dificultad == 2:
            barcos = 5
        elif dificultad == 3:
            barcos = 10

        if opcion == 1:
            tablero_jugador1 = crear_tablero()
            colocar_barcos(tablero_jugador1,barcos,turno = 1)
            tablero_jugador2 = crear_tablero()
            colocar_barcos(tablero_jugador2,barcos,turno= 2)
            alternar_tiros(tablero_jugador1,tablero_jugador2,barcos)
        elif opcion == 2:
            print("Modo Jugador vs CPU aún no implementado.")
        else:
            print(Fore.RED + "Saliendo del programa...")

# ///////////////////////////////////////////////////////////////////////////////////////// Ejecutar código.
ejecutar_batalla_naval()
