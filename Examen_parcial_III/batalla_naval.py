# Gracida Tapia Bryan.
# 26 de Enero del 2025.
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
def colocar_barcos(tablero) -> None:
    """
    Modo de juego: Jugador contra Jugador.
    :return:
    """
    contador = 0
    ficha = "🚤"
    while contador < 3:
        limpiar()
        contador += 1
        mostrar_tablero(tablero)
        print("Coloca tus barcos")
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
def colocar_bombas(tablero_tiros) -> None:
    """
    Modo de juego: Jugador contra Jugador.
    :return:
    """
    contador = 0
    ficha = "☄️"
    while contador < 3:
        limpiar()
        contador += 1
        mostrar_tablero(tablero_tiros)
        print("Coloca tus bombas")
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
def verificar_impactos(tablero_barcos, tablero_tiros):
    """
    Compara los tableros de barcos y tiros para verificar si las bombas acertaron.
    :param tablero_barcos: Tablero con la ubicación de los barcos.
    :param tablero_tiros: Tablero con las ubicaciones de los tiros.
    """
    for fila in range(7):
        for columna in range(7):
            if tablero_barcos[fila][columna] == "🚤" and tablero_tiros[fila][columna] == "☄️":
                tablero_barcos[fila][columna] = "💢"

                print(f"Impacto en ({fila + 1}, {columna + 1})")
    print("Tablero actualizado después de los impactos:")
    mostrar_tablero(tablero_barcos)


# ///////////////////////////////////////////////////////////////////////////////////////// Función main.
def main() -> None:
    """
    Función donde se encuentra las llamadas a funciones principales..
    :return:
    """
    if __name__ == "__main__":
        opcion = Menus.menu_jugabilidad()
        if opcion == 1:
            tablero = crear_tablero()
            colocar_barcos(tablero)
            tablero_tiros = crear_tablero()
            colocar_bombas(tablero_tiros)
            verificar_impactos(tablero, tablero_tiros)
        elif opcion == 2:
            print("Modo Jugador vs CPU aún no implementado.")
        else:
            print(Fore.RED + "Saliendo del programa...")

# ///////////////////////////////////////////////////////////////////////////////////////// Ejecutar código.
main()

