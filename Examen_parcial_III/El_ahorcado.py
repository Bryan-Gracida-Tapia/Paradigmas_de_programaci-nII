# Gracida Tapia Bryan.
# 25 de noviembre del 2024.
# Descripción:
# Juego del ahorcado, cuenta con dos modos.
import random
import Menus
from colorama import Fore

# ///////////////////////////////////////////////////////////////////////////////////////// Función para limpiar la pantalla.
def limpiar() -> None:
    """
    Imprime varias lineas en blanco, para simular una pantalla limpia.
    """
    print("\n" * 50)

# ///////////////////////////////////////////////////////////////////////////////////////// Función para imprimir el ahorcado de forma grafica.
def mostrar_ahorcado(intentos) -> None :
    """
    :param intentos: Reciba la cantidad de intentos que lleva el usuario.
    :return: Dibuja el ahorcado basado en los intentos que le quedan al usuario.
    """

    estados = [
        """
            |-----|     
            |     |   
            |     x  
            |    
        -----------
        """,
        """
            |-----|     
            |     |   
            |     O   
            |      
            |    
        -----------
        """,
        """
            |-----|     
            |     |   
            |     O   
            |     | 
            |    
        -----------
        """,
        """
            |-----|     
            |     |   
            |     O   
            |    /|  
            |    
        -----------
        """,
        """
            |-----|     
            |     |   
            |     O   
            |    /|\  
            |    
        -----------
        """,
        """
            |-----|     
            |     |   
            |     O   
            |    /|\  
            |    /  
        -----------
        """,
        """
            |-----|     
            |     |   
            |     O   
            |    /|\  
            |    / \  

        -----------
        """,
    ]
    print(Fore.RED + estados[6 - intentos])

# ///////////////////////////////////////////////////////////////////////////////////////// Función de juego del ahorcado.
def jugar_ahorcado(opcion) -> None:
    """
    Función principal del juego del ahorcado.
    Modo de juego: Jugador contra Jugador ó Jugador contra CPU, dependiendo de lo que elija el usuario
    :return:
    """
    if opcion == 1:
        print(Fore.YELLOW +"\nJugardor 1.")
        palabra_secreta = input(Fore.YELLOW + "Ingrese la palabra secreta: ")
        while not palabra_secreta.isalpha():
            palabra_secreta = input(Fore.YELLOW + "La palabra ingresada, no es correcta, intente de nuevo: ")
    if opcion == 2:
        palabras = ["indole", "programacion", "incontinencia", "enunciado", "computadora"]
        palabra_secreta = random.choice(palabras)
    if opcion == 3:
        print(Fore.YELLOW + "Saliendo del programa ...")
        print()
        return None

    letras_adivinadas = ["_" for _ in palabra_secreta]
    intentos = 6
    letras_intentadas = []
    while intentos > 0 and "_" in letras_adivinadas:
        limpiar()
        mostrar_ahorcado(intentos)
        print(Fore.YELLOW + "\nJugador 2.")
        print(Fore.YELLOW + f"Palabra: {letras_adivinadas}")
        print(Fore.YELLOW + f"Letras intentadas: {letras_intentadas}")
        letra = input(Fore.YELLOW + "Adivina una letra: ").lower()

        if len(letra) != 1 or not letra.isalpha():
            print(Fore.YELLOW + "Letra válida, intenta de nuevo.")
            continue

        if letra in letras_intentadas:
            print(Fore.YELLOW + "Ya intentaste esa letra, prueba con otra.")
            print()
            continue

        if letra in palabra_secreta:
            for i, caracter in enumerate(palabra_secreta):
                if caracter == letra:
                    letras_adivinadas[i] = letra
        else:
            intentos -= 1
        letras_intentadas.append(letra)

    limpiar()
    mostrar_ahorcado(intentos)

    if "_" not in letras_adivinadas:
        print(Fore.YELLOW + "\n¡Felicidades! Has adivinado la palabra:", palabra_secreta)
    else:
        print(Fore.YELLOW + "\nLo siento, has perdido. La palabra era:", palabra_secreta)


# ///////////////////////////////////////////////////////////////////////////////////////// Función main.
def main() -> None:
    """
    Función donde se encuentra las llamadas a funciones principales..
    :return:
    """
    if __name__ == "__main__":
        eleccion = 1
        opcion = 0
        while eleccion != 2 and opcion != 3:
            opcion = Menus.menu_jugabilidad()
            jugar_ahorcado(opcion)
            if opcion != 3:
                eleccion = Menus.menu_repetir()

# ///////////////////////////////////////////////////////////////////////////////////////// Código a nivel de módulo.
main()