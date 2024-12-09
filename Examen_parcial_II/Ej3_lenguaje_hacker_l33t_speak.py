# Gracida Tapia Bryan.
# 08 de Diciembre del 2024.
# Descripción:
# Este programa remplaza caracteres de un texto ingresado dependiendo el lenjuage seleccionado.
import random


# ///////////////////////////////////////////////////////////////////////////////////////// Función menú.
def menu():
    print("** Menú **")
    print("1) Convertir un texto a lenguaje básico.")
    print("2) Convertir un texto a lenguaje intermedio.")
    print("3) Salir.")
    opcion = int(input("Ingresa una opción: "))
    return opcion

# ///////////////////////////////////////////////////////////////////////////////////////// Función para convertir el texto dependiendo del nivel elejido.
def convertir_texto(texto_ingresado,diccionario_basico,diccionario_intermedio):
    texto_convertido = ""
    if opcion == 1: # ................................ Convertir a lenguaje básico.
        for caracter in texto_ingresado:
            texto_convertido += diccionario_basico.get(caracter, caracter)      # Se remplaza el carácter si este existe en el diccionario.
        return texto_convertido
    else: # ................................ Convertir a lenguaje intermedio.
        for caracter in texto_ingresado:
            texto_convertido += diccionario_intermedio.get(caracter, caracter)  # Se remplaza el carácter si este existe en el diccionario
        return texto_convertido

# ///////////////////////////////////////////////////////////////////////////////////////// Función selección.
def seleccion(opcion):
    if opcion == 1 or opcion == 2:
        texto_ingresado = input("Ingresa texto a convertir: ")
        texto_covertido = convertir_texto(texto_ingresado, diccionario_basico,diccionario_intermedio)
    elif opcion == 3:
        print("Saliendo...")
    else:
        print("Opción no válida :(")
    return texto_covertido

# ///////////////////////////////////////////////////////////////////////////////////////// Código a nivel de módulo.
# ................................ Diccionarios.
# Diccionario del nivel básico
diccionario_basico = {'a': '4','A': '4','e': '3','E': '3','i': '1','o': '0','O': '0','u': '(_)','U': '(_)'}
# Diccionario del nivel intermedio
diccionario_intermedio = {'a': '4','A': '4','b': 'l3','B': 'l3','c': '[','C': '[','d': ')','D': ')','e': '3','E': '3','f': '|=','F': '|=','g': '&','G': '&','h': '#','H': '#','i': '1','I': '1','j': ',_|','J': ',_|',
                                           'k': '>|','K': '>|','l': '1','L': '1','m': '/\/\ ','M': '/\/\ ','n': '^/','N': '^/','o': '0','O': '0','p': '|*','P': '|*','q': '(_,)','Q': '(_,)','r': 'l2','R': 'l2','s': '5','S': '5',
                                           't': '7','T': '7','u': '(_)','U': '(_)','v': '\/','V': '\/','w': '\/\/','W': '\/\/','x': '><','X': '><','y': 'j','Y': 'j','z': '2','Z': '2'}

print("***  Lenguaje hacker (l33t sp34k).  ***")
opcion = 0
while opcion != 3:
    opcion = menu()
    texto_convertido = seleccion(opcion)
    print(f"Texto convertido : {texto_convertido}")

    print()
    print("-----------------------------")
    print()
