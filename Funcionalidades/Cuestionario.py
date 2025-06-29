
import random

def string_elegir_tema():
    menu = """Elige un tema para las preguntas:
1. Geografía
2. Arte y Literatura
3. Historia
4. Entretenimiento
5. Ciencias y Naturaleza
6. Deportes y pasatiempos
7. Modo Trivial (Cuestionario de temas variados)
8. Salir\n"""
    return menu

def elegir_tema():
    opcion = -1
    while opcion != 8:
        try:
            opcion = int(input(string_elegir_tema()))
            match opcion:
                case 1:
                    print("Preparando cuestionario sobre geografía...")
                    tema = "geografia"
                    return tema
                case 2:
                    print("Preparando cuestionario sobre arte y literatura...")
                    tema = "arte_literatura"
                    return tema
                case 3:
                    print("Preparando cuestionario sobre historia...")
                    tema = "historia"
                    return tema
                case 4:
                    print("Preparando cuestionario sobre entretenimiento...")
                    tema = "entretenimiento"
                    return tema
                case 5:
                    print("Preparando cuestionario sobre ciencias y naturaleza...")
                    tema = "ciencias_naturaleza"
                    return tema
                case 6:
                    print("Preparando cuestionario sobre deportes y pasatiempos...")
                    tema = "deportes_pasatiempos"
                    return tema
                case 7:
                    print("Preparando modo trivial...")
                    tema = "trivial"
                    return tema
                case 8:
                    print("Saliendo del modo cuestionario.")
                    tema = "salir"
                    return tema
                case _:
                    print("Opción no válida, por favor introduce una de las opciones de la lista.")
        except ValueError:
            print("Opción no válida, por favor introduce una de las opciones de la lista.")

def string_elegir_dificultad():
    menu = """Elige una dificultad para las preguntas:
1. Muy fácil
2. Fácil
3. Medio
4. Difícil
5. TriviaHell
6. Salir\n"""
    return menu

def elegir_dificultad():
    opcion = -1
    while opcion != 6:
        try:
            opcion = int(input(string_elegir_dificultad()))
            match opcion:
                case 1:
                    print("Preparando cuestionario nivel muy fácil...")
                    dificultad = "muy_facil"
                    return dificultad
                case 2:
                    print("Preparando cuestionario nivel fácil...")
                    dificultad = "facil"
                    return dificultad
                case 3:
                    print("Preparando cuestionario nivel medio...")
                    dificultad = "medio"
                    return dificultad
                case 4:
                    print("Preparando cuestionario nivel difícil...")
                    dificultad = "dificil"
                    return dificultad
                case 5:
                    print("Preparando TriviaHell...")
                    dificultad = "trivia_hell"
                    return dificultad
                case 6:
                    print("Saliendo del modo cuestionario.")
                    dificultad = "salir"
                    return dificultad
                case _:
                    print("Opción no válida, por favor introduce una de las opciones de la lista.")
        except ValueError:
            print("Opción no válida, por favor introduce una de las opciones de la lista.")

def elegir_numero_preguntas():
    while True:
        numero_preguntas = input("Escribe el número de preguntas que quieres en tu cuestionario o 'salir' para salir.\n")
        if numero_preguntas.lower() == "salir":
            print("Saliendo del modo cuestionario.")
        elif not numero_preguntas.isdigit():
            print("Opción no válida, por favor introduce una de las opciones de la lista.")
        elif int(numero_preguntas) < 10:
            print("El cuestionario debe tener al menos 10 preguntas.")
        elif int(numero_preguntas) > 100:
            print("El cuestionario debe tener como máximo 100 preguntas.")
        else:
            return int(numero_preguntas)

def crear_cuestionario(tema, dificultad, numero_preguntas, pool_preguntas):
    #Creamos un pool de preguntas para el cuestionario que coincida con el tema y la dificultad escogida.
    pool_cuestionario = []
    for pregunta in pool_preguntas:
        if pregunta['dificultad'] == dificultad:
            if tema == "trivial":
                pool_cuestionario.append(pregunta)
            elif pregunta['tema'] == tema:
                pool_cuestionario.append(pregunta)
    #Creamos un cuestionario escogiendo de manera aleatoria N preguntas del pool de preguntas sin que se repitan.
    cuestionario = []
    for i in range(numero_preguntas):
        pregunta = random.choice(pool_cuestionario)
        cuestionario.append(pregunta)
        pool_cuestionario.remove(pregunta)
    print(f"CREANDO CUESTIONARIO")
    return cuestionario

def menu_cuestionario(pool_preguntas):
    tema = elegir_tema()
    if not tema == "salir":
        dificultad = elegir_dificultad()
        if not dificultad == "salir":
            numero_preguntas = elegir_numero_preguntas()
            if not numero_preguntas == "salir":
                cuestionario = crear_cuestionario(tema, dificultad, numero_preguntas, pool_preguntas)
                return cuestionario

def mostrar_pregunta(pregunta_cuestionario):
    print(pregunta_cuestionario['pregunta'])
    print(pregunta_cuestionario['opciones'])

def obtener_respuesta():
    respuesta = ""
    while not (respuesta == "A" or respuesta == "B" or respuesta == "C" or respuesta == "D"):
        input_usuario = input("¿Cuál es tu respuesta?\n")
        if input_usuario.upper() == "A":
            respuesta = "A"
        elif input_usuario.upper() == "B":
            respuesta = "B"
        elif input_usuario.upper() == "C":
            respuesta = "C"
        elif input_usuario.upper() == "D":
            respuesta = "D"
        else:
            print("Opción no válida, por favor introduce una de las opciones de la lista.")
    return respuesta

def corregir_pregunta(respuesta, pregunta):
    if respuesta == pregunta['respuesta_correcta']:
        print("¡Respuesta correcta!")
        return 1
    else:
        print(f"Respuesta incorrecta. La respuesta correcta era la {pregunta['respuesta_correcta']}")
        return 0

def mostrar_resultados(aciertos, total):
    porcentaje = aciertos*100/total
    if porcentaje < 20:
        valoracion = "¡Ánimo! Parece que hoy no era tu día, pero cada error es una oportunidad para aprender."
    elif porcentaje < 40:
        valoracion = "¡No está mal para empezar! Sigue intentándolo y pronto dominarás el juego."
    elif porcentaje < 60:
        valoracion = "¡Se nota que sabes! Aunque aún queda margen para mejorar."
    elif porcentaje < 80:
        valoracion = "¡Muy bien! Se nota que sabes del tema."
    elif porcentaje < 100:
        valoracion = "¡Genial! No se te escapa ni una."
    elif aciertos == total:
        valoracion = "¡Increíble! Has acertado todas. Eres un auténtico maestro del trivial."
    resumen = f"""###RESUMEN DEL CUESTIONARIO###
Número total de preguntas: {total}
Número de aciertos: {aciertos}
Porcentaje de aciertos: {round(porcentaje)}%
{valoracion}"""
    return resumen

def realizar_cuestionario(cuestionario):
    aciertos = 0
    for pregunta in cuestionario:
        mostrar_pregunta(pregunta)
        aciertos += corregir_pregunta(obtener_respuesta(), pregunta)
    print(mostrar_resultados(aciertos, len(cuestionario)))