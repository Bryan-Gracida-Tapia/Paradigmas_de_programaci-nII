# Gracida Tapia Bryan.
# 08 de Diciembre del 2024.
# Descripción:
# Este programa determina la casa (Gryffindor, Slytherin, Hufflepuff y Ravenclaw) a la que se pertenece, de acuerdo a las respuestas ingresadas.
import random


# ///////////////////////////////////////////////////////////////////////////////////////// Función menú.
def menu():
    print("** Menú **")
    print("[1] Iniciar test")
    print("[2] Salir")
    opcion_elejida = int(input("Ingresa una opcion: "))
    return opcion_elejida
# ///////////////////////////////////////////////////////////////////////////////////////// Función iniciar el test.
def iniciar_test():
    # ................................ Diccionarios.
    # Diccionario de preguntas
    preguntas = [{"pregunta": "¿Cuál de las siguientes opciones odiarías más que la gente te llamara?","respuestas": {"Gryffindor": "Ordinario","Slytherin": "Ignorante","Hufflepuff": "Cobarde","Ravenclaw": "Egoísta"}},
                {"pregunta": "Después de tu muerte, ¿qué es lo que más le gustaría que hiciera la gente cuando escuche tu nombre?","respuestas": {"Gryffindor": "Te extraña, pero sonríe","Slytherin": "Pide más historias sobre tus aventuras","Hufflepuff": "Piensa con admiración tus logros","Ravenclaw": "No me importa lo que piensen de mí después de mi muerte, lo que piensen de mí ahora es lo que cuenta"}},
                {"pregunta": "Dada la opción, ¿preferirías inventar una poción que garantizara?","respuestas": {"Gryffindor": "Gloria","Slytherin": "Sabiduría","Hufflepuff": "Amor","Ravenclaw": "Poder"}},
                {"pregunta": "¿Cómo te definirías en una sola palabra?","respuestas": {"Gryffindor": "Valiente","Slytherin": "Ambicioso","Hufflepuff": "Leal","Ravenclaw": "Curioso"}},
                {"pregunta": "¿Qué cualidad te describe mejor?","respuestas": {"Gryffindor": "La fuerza","Slytherin": "La astucia","Hufflepuff": "La paciencia","Ravenclaw": "La inteligencia"}},
                {"pregunta": "¿Cuál es tu clase favorita?","respuestas": {"Gryffindor": "Vuelo","Slytherin": "Defensa contra las artes oscuras","Hufflepuff": "Animales fantásticos","Ravenclaw": "Pociones"}},
                {"pregunta": "¿Cuál es tu lenguaje de programación favorito?","respuestas": {"Gryffindor": "C","Slytherin": "Python","Hufflepuff": "C++","Ravenclaw": "JavaScript"}}
    ]

    # Diccionario de puntos por casa.
    puntuaciones = {"Gryffindor": 0, "Slytherin": 0, "Hufflepuff": 0, "Ravenclaw": 0}

    # ................................ Selección aleatoria de 5 preguntas de las 7 existentes en el dicionario de preguntas.

    preguntas_elejidas = random.sample(preguntas, 5)       # la palabra reservada random.sample() selecciona preguntas aleatorias en este caso las ingresadas en el diccionario preguntas, se puede utlizar con conjuntos y listas.

    # ................................ Mostrar las preguntas elijidas y sus opciones.

    for pregunta in preguntas_elejidas:
        print(f"\n{pregunta['pregunta']}")
        respuestas = list(pregunta["respuestas"].items())
        random.shuffle(respuestas)          # la palabra reservada ramdom.shuffle ordena aleatoriamente las opciones.
        opciones = {str(i + 1): respuesta[1] for i, respuesta in enumerate(respuestas)}
        for i, opcion in opciones.items():
            print(f"{i}) {opcion}")

        # ................................ Se lee la respuesta y se asigna el punto a la casa correspondiente en caso de ser valida.

        while True:
            respuesta = input("Selecciona una opción: ").strip()
            if respuesta in opciones:
                # Se busca la casa correspondiente a la respuesta
                for casa, texto in pregunta["respuestas"].items():
                    if opciones[respuesta] == texto:       # Se itera en cada una de las de las opciones, y se comparan las respuestas.
                        puntuaciones[casa] += 1
                break
            else:
                print("Opción no válida. Intenta nuevamente.")
    # ................................ Se buca la casa con mayor puntuación.
    # Determinar la casa con mayor puntuación
    casa_seleccionada = max(puntuaciones, key=puntuaciones.get)     # # la palabra reservada max se utiliza para determinar la puntuación mas alta.
    print(f"\nEl sombrero seleccionador te ha asignado a la casa {casa_seleccionada}. \n¡Felicidades!")

# ///////////////////////////////////////////////////////////////////////////////////////// Función selección.
def seleccion(opcion):
    if opcion == 1:
        iniciar_test()
    elif opcion == 2:
        print("Saliendo...")

    else:
        print("Opción no válida. Intenta nuevamente.")

# ///////////////////////////////////////////////////////////////////////////////////////// Código a nivel de módulo.
print("***  Test del sombrero seleccionador de Harry Potter.  ***")
opcion = 0
while opcion != 2:
    opcion = menu()
    seleccion(opcion)

    print()
    print("-----------------------------")
    print()


