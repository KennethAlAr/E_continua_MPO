
import random
import json

def input_nueva_pregunta():
    pregunta = input("Introduce la nueva pregunta:\n")
    respuesta_correcta = input("Introduce la respuesta correcta:\n")
    respuesta_incorrecta1 = input("Introduce la primera respuesta incorrecta:\n")
    respuesta_incorrecta2 = input("Introduce la segunda respuesta incorrecta:\n")
    respuesta_incorrecta3 = input("Introduce la tercera respuesta incorrecta:\n")
    respuestas = [respuesta_correcta, respuesta_incorrecta1, respuesta_incorrecta2, respuesta_incorrecta3]
    tema = anadir_tema()
    dificultad = anadir_dificultad()
    return pregunta, respuestas, tema, dificultad

def anadir_tema():
    while True:
        try:
            opcion = int(input("""¿Cual es el tema de la pregunta?
1. Geografía
2. Arte y Literatura
3. Historia
4. Entretenimiento
5. Ciencias y Naturaleza
6. Deportes y pasatiempos
"""))
            match opcion:
                case 1:
                    tema = "geografia"
                    return tema
                case 2:
                    tema = "arte_literatura"
                    return tema
                case 3:
                    tema = "historia"
                    return tema
                case 4:
                    tema = "entretenimiento"
                    return tema
                case 5:
                    tema = "ciencias_naturaleza"
                    return tema
                case 6:
                    tema = "deportes_pasatiempos"
                    return tema
                case _:
                    print("Opción no válida, por favor introduce una de las opciones de la lista.")
        except ValueError:
            print("Opción no válida, por favor introduce una de las opciones de la lista.")

def anadir_dificultad():
    while True:
        try:
            opcion = int(input("""¿Cual es la dificultad de la pregunta?
1. Muy fácil
2. Fácil
3. Medio
4. Difícil
5. Muy difícil
"""))
            match opcion:
                case 1:
                    dificultad = "muy_facil"
                    return dificultad
                case 2:
                    dificultad = "facil"
                    return dificultad
                case 3:
                    dificultad = "medio"
                    return dificultad
                case 4:
                    dificultad = "dificil"
                    return dificultad
                case 5:
                    dificultad = "trivia_hell"
                    return dificultad
                case _:
                    print("Opción no válida, por favor introduce una de las opciones de la lista.")
        except ValueError:
            print("Opción no válida, por favor introduce una de las opciones de la lista.")

def desordenar_respuestas(respuestas):
    #Creamos una copia real de "respuestas" para que no se modifique el original si modificamos la copia.
    copia_respuestas = respuestas[:]
    respuestas_formateadas = []
    respuesta_correcta = -1
    lista_opciones = ["A. ", "B. ", "C. ", "D. "]
    lista_respuestas = ["A", "B", "C", "D"]
    for i in range(4):
        eleccion = random.choice(copia_respuestas)
        respuestas_formateadas.append(eleccion)
        copia_respuestas.remove(eleccion)
    for respuesta in respuestas_formateadas:
        if respuesta == respuestas[0]:
            respuesta_correcta = respuestas_formateadas.index(respuesta)
    for i in range (4):
        respuestas_formateadas[i] = lista_opciones[i] + respuestas_formateadas[i]
    respuesta_correcta = lista_respuestas[respuesta_correcta]

    return respuesta_correcta, respuestas_formateadas


def crear_pregunta(pregunta, respuestas, tema, dificultad):
    respuesta_correcta, respuestas_formateadas = desordenar_respuestas(respuestas)
    nueva_pregunta = {
        "pregunta" : pregunta,
        "respuestas" : respuestas_formateadas,
        "respuesta_correcta" : respuesta_correcta,
        "tema" : tema,
        "dificultad" : dificultad
    }
    return nueva_pregunta

def imprimir_pregunta(nueva_pregunta):
    resumen = (f"Pregunta: {nueva_pregunta["pregunta"]}\n"
               f"Respuestas:\n"
               f"{nueva_pregunta["respuestas"][0]}\n"
               f"{nueva_pregunta["respuestas"][1]}\n"
               f"{nueva_pregunta["respuestas"][2]}\n"
               f"{nueva_pregunta["respuestas"][3]}\n"
               f"Respuesta correcta: {nueva_pregunta["respuesta_correcta"]}\n"
               f"Tema: {nueva_pregunta["tema"]}\n"
               f"Dificultad: {nueva_pregunta["dificultad"]}")
    return resumen

def confirmar_anadir_pregunta(nueva_pregunta, pool_preguntas):
    opcion = -1
    while not (opcion == 1 or opcion == 2):
        try:
            print("Este es el resumen de tu pregunta:")
            print(imprimir_pregunta(nueva_pregunta))
            opcion = int(input("¿Quieres añadirla al catálogo de preguntas?\n1. Si\n2. No"))
            match opcion:
                case 1:
                    print("Añadida pregunta al catálogo de preguntas.")
                    pool_preguntas.append(nueva_pregunta)
                case 2:
                    print("Saliendo del gestor de preguntas nuevas.")
                case _:
                    print("Opción no válida, por favor introduce una de las opciones de la lista.")
        except ValueError:
            print("Opción no válida, por favor introduce una de las opciones de la lista.")

def gestion_nueva_pregunta(pool_preguntas):
    pregunta, respuestas, tema, dificultad =input_nueva_pregunta()
    nueva_pregunta = crear_pregunta(pregunta, respuestas, tema, dificultad)
    confirmar_anadir_pregunta(nueva_pregunta, pool_preguntas)

def obtener_ruta_archivo():
    ruta = input("""Por favor, introduce la ruta del archivo que quieres importar o escribe 'salir' para salir:
Pool_Preguntas/Ejemplo_importar_preguntas.json\n""")
    return ruta

def validar_archivo(lista_preguntas):
    for pregunta in lista_preguntas:
        if not isinstance(pregunta, dict):
            print("Error al importar el archivo. Alguna pregunta no cumple el formato específicado.")
            return False
        claves_preguntas = ["pregunta", "opciones", "respuesta_correcta", "tema", "dificultad"]
        for clave in claves_preguntas:
            if clave not in pregunta:
                print(f"Error al importar el archivo, falta la clave '{clave}'.")
                return False
        if not isinstance(pregunta["opciones"], list) or not len(pregunta["opciones"]) == 4:
            print("Error al importar el archivo, las respuestas de la pregunta no cumplen el formato especificado.")
            return False
        if not (pregunta["respuesta_correcta"] in ["A", "B", "C", "D"]):
            print("Error al importar el archivo. El valor de 'respuesta correcta' no es válido.")
            return False
        if not (pregunta["tema"] in ["geografia", "arte_literatura", "historia", "entretenimiento", "ciencias_naturaleza", "deportes_pasatiempos"]):
            print("Error al importar el archivo. El valor de 'tema' no es válido.")
            return False
        if not (pregunta["dificultad"] in ["muy_facil", "facil", "medio", "dificil", "trivia_hell"]):
            print("Error al importar el archivo. El valor de 'tema' no es válido.")
            return False
    return True

def importar_archivo(pool_preguntas):
    print("""Importando archivo .json o .txt. El archivo debe contener una lista de diccionarios con el siguiente formato:
[
  {
    "pregunta": "Tu pregunta va aquí",
    "opciones": [
      "A. Tu primera respuesta va aquí",
      "B. Tu segunda respuesta va aquí",
      "C. Tu tercera respuesta va aquí",
      "D. Tu cuarta respuesta va aquí"
    ],
    "respuesta_correcta": "La letra de la respuesta correcta va aquí ("A", "B", "C", "D")"
    "tema": "tema de la pregunta (Elegir entre: "geografia", "arte_literatura", "historia", "entretenimiento", "ciencias_naturaleza" o "deportes_pasatiempos")",
    "dificultad": "dificultad de la pregunta (Elegir entre: "muy_facil", "facil", "medio", "dificil" o "trivia_hell")"
  }
]
Ejemplo:
[
  {
    "pregunta": "¿Cuál es la capital de Francia?",
    "opciones": [
      "A. Madrid",
      "B. Londres",
      "C. Roma",
      "D. París"
    ],
    "respuesta_correcta": "D",
    "tema": "geografia",
    "dificultad": "muy_facil"
  },
  {
    "pregunta": "¿En qué continente está Brasil?",
    "opciones": [
      "A. África",
      "B. Europa",
      "C. Asia",
      "D. América"
    ],
    "respuesta_correcta": "D",
    "tema": "geografia",
    "dificultad": "muy_facil"
  }
]""")
    while True:
        try:
            nuevas_preguntas = []
            ruta = obtener_ruta_archivo()
            if not ruta.lower() == "salir":
                with open(ruta, encoding="utf-8") as preguntas:
                    nuevas_preguntas.extend(json.load(preguntas))
                    if validar_archivo(nuevas_preguntas):
                        pool_preguntas.extend(nuevas_preguntas)
                        print("Añadida lista de preguntas al catálogo de preguntas.")
                        print(pool_preguntas)
                break
            else:
                break
        except FileNotFoundError:
            print("Ruta no válida, por favor introduce una ruta válida.")

def menu_nueva_pregunta(pool_preguntas):
    opcion = -1
    while not opcion == 4:
        try:
            opcion = int(input("""¿Cómo deseas añadir preguntas nuevas?
1. Añadir pregunta a mano
2. Importar archivo .json o .txt
3. Salir\n"""))
            match opcion:
                case 1:
                    gestion_nueva_pregunta(pool_preguntas)
                case 2:
                    importar_archivo(pool_preguntas)
                    break
                case 3:
                    print("Saliendo del menú para introducir preguntas nuevas...")
                case _:
                    print("Opción no válida, por favor introduce una de las opciones de la lista.")
        except ValueError:
            print("Opción no válida, por favor introduce una de las opciones de la lista.")