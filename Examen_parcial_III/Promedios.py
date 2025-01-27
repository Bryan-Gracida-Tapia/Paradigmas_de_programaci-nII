# Gracida Tapia Bryan.
# 25 de noviembre del 2024.
# Descripción:
# Juego cuatro en raya con dos modos de juego: J vs J y J vs CPU.
import Menus
from colorama import Fore

# ///////////////////////////////////////////////////////////////////////////////////////// Función calcular promedio.
def promedio_final(**kwargs):
    """
    Recibe materias con sus claves y valor en este caso(Clave : materias  y Valor : Promedios)
    :param kwargs: Materias y sus promedios
    """
    print("** PROMEDIO **")

    promedio_general = sum(kwargs.values()) / len(kwargs)
    print(f"\nEl promedio general es: {promedio_general:.2f}")

# ///////////////////////////////////////////////////////////////////////////////////////// Función ingresar calificaciones.
def ingresar_materias_promedios() -> None:
    materias = {}

    print("Registro de materias y promedios")

    while True:
        materia = input("\nIntroduce el nombre de la materia, escribe fin para dejar de ingresar materias: \n")

        if materia.lower() == 'fin':
            break

        promedio_cadena = input(f"Introduce el promedio de {materia}: \n")

        promedio = Menus.cadena_a_flotante(promedio_cadena)

        while promedio is None:
            print("Introduce un promedio válido")
            promedio_cadena = input(f"Introduce el promedio de {materia}: ")
            promedio = Menus.cadena_a_flotante(promedio_cadena)

        materias[materia] = promedio

    if materias:
        print(materias)
        promedio_final(**materias)
    else:
        print("No se registro de materias existentres")

# ///////////////////////////////////////////////////////////////////////////////////////// Función main.
def main() -> None:
    if __name__ == '__main__':
        ingresar_materias_promedios()

# ///////////////////////////////////////////////////////////////////////////////////////// Código a nivel de módulo.
main()
