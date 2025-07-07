
import json
from Funcionalidades.Cuestionario import realizar_cuestionario, menu_cuestionario
from Funcionalidades.Anadir_Preguntas import menu_nueva_pregunta
from Funcionalidades.Ranking import menu_ranking

pool_preguntas = []
with open ("Pool_Preguntas/Preguntas.json", encoding="utf-8") as preguntas:
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
                menu_ranking(pool_preguntas)
            case 3:
                menu_nueva_pregunta(pool_preguntas)
            case 4:
                print("Saliendo del Generador de Cuestionarios Interactivo.")
            case _:
                print("Opción no válida, por favor introduce una de las opciones de la lista.")
    except ValueError:
        print("Opción no válida, por favor introduce una de las opciones de la lista.")