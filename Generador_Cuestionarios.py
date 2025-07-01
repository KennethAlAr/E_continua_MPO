
import json
from Funcionalidades.Cuestionario import *

pool_preguntas = []
with open ("Pool_Preguntas/preguntas.json", encoding="utf-8") as preguntas:
    pool_preguntas = json.load(preguntas)

def string_menu_principal():
    menu = """###MENÚ###
1 - Empezar cuestionario
2 - La cima al conocimiento (Modo Ranking)
3 - Añadir preguntas
4 - Salir

¿Qué quieres hacer?\n"""
    return menu

opcion = -1
while opcion != 4:
    try:
        opcion = int(input(string_menu_principal()))
        match opcion:
            case 1:
                realizar_cuestionario(menu_cuestionario(pool_preguntas))
            case 2:
                print("op2") #Entramos al mod RANKING (20 PREGUNTAS DIFICULTAD ASCENDENTE, PUNTUACIÓN POR DIFICULTAD)
            case 3:
                print("op3") #Entramos a la función para añadir una pregunta nueva (A MANOPLA / ARCHIVO JSON / ARCHIVO TXT)
            case 4:
                print("Saliendo del Generador de Cuestionarios Interactivo.") #Salir
            case _:
                print("Opción no válida, por favor introduce una de las opciones de la lista.")
    except ValueError:
        print("Opción no válida, por favor introduce una de las opciones de la lista.")