# Gracida Tapia Bryan.
# 26 de Enero del 2025.
# Descripción:
# Juego del gato con dos modos de juego: Jugador contra Jugador y Jugador contra CPU.
import random
import Menus
from colorama import Fore

# ///////////////////////////////////////////////////////////////////////////////////////// Función para limpiar la pantalla.
def limpiar() -> None :
    """
    Imprime varias lineas en blanco, para simular una pantalla limpia.
    """
    print("\n" * 50)

# ///////////////////////////////////////////////////////////////////////////////////////// Funciones para tablero.
def crear_tablero_gato() -> list:
    """
    Crea un tablero vacío de 3 filas por 3 columnas.
    :return: Regresa el tablero en forma de lista.
    """
    return [[" " for _ in range(3)] for _ in range(3)]

def mostrar_tablero_gato(tablero):
    """
    Muestra el tablero en pantalla.
    :param tablero: Recibe las filas y columnas que tendra el tablero
    :return:
    """
    print("   1   2   3")
    for i, fila in enumerate(tablero):
        print(f"{i + 1}  " + " | ".join(fila))
        if i < 2:
            print("  -----------")

# ///////////////////////////////////////////////////////////////////////////////////////// Funciones de validación.
def colocar_ficha_gato(tablero, fila, columna, ficha) -> bool:
    """
    Coloca una ficha en la posición indicada si es posible.
    :param tablero: recibe el tablero con las fichas que esten existentes.
    :param fila: recibe el valor de la fila disponible.
    :param columna: recibe la columna elejida por el usuario.
    :param ficha: recibe X o O dependiendo de la ficha que toque verificar.
    :return: Regresa un valor booleano dependiendo si es posible colocar la ficha o no.
    """

    if tablero[fila][columna] == " ":
        tablero[fila][columna] = Fore.YELLOW + ficha
        return True
    return False

def verificar_victoria_gato(tablero, ficha) -> bool:
    """
    Verifica si hay un ganador en el juego del gato.
    :param tablero: Reciba el tablero con las fichas que ya esten colocadas
    :param ficha: Recibe X o Y, dependiendo del turno.
    :return: Regresa un valor booleano en caso de que gane la ultima ficha en colocarse.
    """

    for i in range(3):      # ................................ Verificar filas y columnas.
        if all(tablero[i][j] == ficha for j in range(3)) or all(tablero[j][i] == ficha for j in range(3)):
            return True

    # ................................ Verificar diagonales.
    if all(tablero[i][i] == ficha for i in range(3)) or all(tablero[i][2 - i] == ficha for i in range(3)):
        return True

    return False

# ///////////////////////////////////////////////////////////////////////////////////////// Funcion jugador vs jugador.
def jugador_vs_jugador() -> None:
    """
    Modo de juego: Jugador contra Jugador.
    :return:
    """

    tablero = crear_tablero_gato()
    turno = 0
    fichas = ["X", "O"]

    while True:
        limpiar()
        mostrar_tablero_gato(tablero)
        ficha_actual = fichas[turno % 2]

        if turno % 2 == 0:
            print("Turno del jugador (X)")
            fila, columna = -1, -1
            while fila < 0 or fila >= 3 or columna < 0 or columna >= 3:
                entrada = input("Elige fila y columna (formato: fila columna): ").split()
                if len(entrada) == 2 and all(x.isdigit() for x in entrada):
                    fila, columna = int(entrada[0]) - 1, int(entrada[1]) - 1
                    if fila < 0 or fila >= 3 or columna < 0 or columna >= 3:
                        print("Coordenadas fuera de rango. Intenta de nuevo.")
                    elif not colocar_ficha_gato(tablero, fila, columna, ficha_actual):
                        print("Casilla ocupada. Intenta otra vez.")
                        fila, columna = -1, -1
                else:
                    print("Entrada inválida. Por favor, ingresa dos números separados por un espacio.")
        else:
            print("Turno de la CPU (O)")
            fila, columna = random.randint(0, 2), random.randint(0, 2)
            while not colocar_ficha_gato(tablero, fila, columna, ficha_actual):
                fila, columna = random.randint(0, 2), random.randint(0, 2)

        if verificar_victoria_gato(tablero, ficha_actual):
            limpiar()
            mostrar_tablero_gato(tablero)
            if turno % 2 == 0:
                print("Jugador (X) gana!")
            else:
                print("La CPU (O) gana!")
            break

        if all(tablero[i][j] != " " for i in range(3) for j in range(3)):
            limpiar()
            mostrar_tablero_gato(tablero)
            print("El juego termina en empate!")
            break

        turno += 1


# ///////////////////////////////////////////////////////////////////////////////////////// Función jugador vs CPU.
def jugar_vs_cpu() -> None :
    """
    Modo de juego: Jugador contra CPU.
    :return:
    """
    tablero = crear_tablero_gato()
    turno = 0
    fichas = ["X", "O"]

    while True:
        limpiar()
        mostrar_tablero_gato(tablero)
        ficha_actual = fichas[turno % 2]

        if turno % 2 == 0:
            print("Turno del jugador (X)")
            fila, columna = -1, -1
            while fila < 0 or fila >= 3 or columna < 0 or columna >= 3:
                entrada = input("Elige fila y columna (formato: fila columna): ").split()
                if len(entrada) == 2 and all(x.isdigit() for x in entrada):
                    fila, columna = int(entrada[0]) - 1, int(entrada[1]) - 1
                    if fila < 0 or fila >= 3 or columna < 0 or columna >= 3:
                        print("Coordenadas fuera de rango. Intenta de nuevo.")
                    elif not colocar_ficha_gato(tablero, fila, columna, ficha_actual):
                        print("Casilla ocupada. Intenta otra vez.")
                        fila, columna = -1, -1
                else:
                    print("Entrada inválida. Por favor, ingresa dos números separados por un espacio.")
        else:
            print("Turno de la CPU (O)")
            fila, columna = random.randint(0, 2), random.randint(0, 2)
            while not colocar_ficha_gato(tablero, fila, columna, ficha_actual):
                fila, columna = random.randint(0, 2), random.randint(0, 2)

        if verificar_victoria_gato(tablero, ficha_actual):
            limpiar()
            mostrar_tablero_gato(tablero)
            if turno % 2 == 0:
                print("Jugador (X) gana!")
            else:
                print("La CPU (O) gana!")
            break

        if all(tablero[i][j] != " " for i in range(3) for j in range(3)):
            limpiar()
            mostrar_tablero_gato(tablero)
            print("El juego termina en empate!")
            break

        turno += 1

# ///////////////////////////////////////////////////////////////////////////////////////// Función main.
def main() -> None:
    """
    Función donde se encuentra las llamadas a funciones principales..
    :return:
    """
    if __name__ == "__main__":
        opcion = Menus.menu_jugabilidad()
        if opcion == 1:
            jugador_vs_jugador()
        elif opcion == 2:
            jugar_vs_cpu()
        else:
            print(Fore.RED + "Saliendo del programa...")

# ///////////////////////////////////////////////////////////////////////////////////////// Ejecutar código.
main()
