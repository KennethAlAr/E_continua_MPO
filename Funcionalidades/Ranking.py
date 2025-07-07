
import random
from inputimeout import inputimeout, TimeoutOccurred
import time
import json

def preparar_cuestionario(pool_preguntas):
    cuestionario = []
    lista_preguntas = []
    #Creamos una copia real de pool_preguntas para no modificar el catálogo de preguntas.
    copia_preguntas = pool_preguntas[:]
    #Para cada dificultad creamos una lista_preguntas con preguntas que coincidan con esa dificultad y añadimos 4 preguntas
    #aleatorias de lista_preguntas al cuestionario.
    for dificultad in ["muy_facil", "facil", "medio", "dificil", "trivia_hell"]:
        for pregunta in copia_preguntas:
            if pregunta['dificultad'] == dificultad:
                lista_preguntas.append(pregunta)
                copia_preguntas.remove(pregunta)
        #En caso que no haya preguntas suficientes de una de las dificultades el cuestionario no se puede hacer.
        if len(lista_preguntas) < 4:
            print("No hay suficientes preguntas de todas las dificultades para comenzar el modo ranking")
            return "salir"
        for i in range(4):
            pregunta = random.choice(lista_preguntas)
            cuestionario.append(pregunta)
            lista_preguntas.remove(pregunta)
        lista_preguntas.clear()
    return cuestionario

def mostrar_pregunta(pregunta_cuestionario):
    print(pregunta_cuestionario['pregunta'])
    for opcion in pregunta_cuestionario['opciones']:
        print(opcion)

def obtener_respuesta(tiempo_restante):
    respuesta = ""
    tiempo_inicio = time.time()
    while not (respuesta == "A" or respuesta == "B" or respuesta == "C" or respuesta == "D"):
        try:
            tiempo_restante = tiempo_restante -(time.time() - tiempo_inicio)
            # inputimeout espera una respuesta durante el tiempo indicado y si el tiempo termina devuelve el error 'TimeoutOcurred'.
            #   En este caso el tiempo es 3 minutos para el test completo, por eso calculamos al inicio de cada bucle el
            #   tiempo que le queda para terminar el test.
            #En la función realizar_ranking() se calcula el tiempo restante antes de entrar a cada pregunta.
            input_usuario = inputimeout("¿Cuál es tu respuesta?\n", timeout = tiempo_restante)
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
        except TimeoutOccurred:
            print("¡Tiempo agotado!")
            return "salir"
    return respuesta

def corregir_pregunta(respuesta, pregunta):
    if respuesta == "salir":
        return "salir"
    elif respuesta == pregunta['respuesta_correcta']:
        print("¡Respuesta correcta!")
        return 1
    else:
        print(f"Respuesta incorrecta. La respuesta correcta era la {pregunta['respuesta_correcta']}")
        return 0

def calcular_puntuacion(aciertos, tiempo_restante):
    if tiempo_restante < 0:
        tiempo = 0
    else:
        tiempo = tiempo_restante
    resultado = aciertos * 100 * (1 + (tiempo * 0.5 / 180))
    return resultado

def obtener_nombre(resultado):
    print(f"¡Tu puntuación es de {resultado:.2f} puntos!")
    nombre = input("Escribe el nombre con el cual quieres guardar la puntuación:")
    return nombre

def guardar_puntuacion(nombre, resultado):
    archivo = "Puntuaciones/Puntuaciones.json"
    #Abrimos el archivo puntuaciones.json para volcar los datos en la variable 'datos'.
    with open(archivo, "r") as puntuaciones:
        datos = json.load(puntuaciones)
    #Añadimos el nombre y la puntuación del usuario a la lista de 'datos'.
    datos.append({"nombre": nombre, "puntuacion": resultado})
    #Sobreescribimos el archivo puntuaciones.json con la nueva lista 'datos'.
    with open(archivo, "w") as puntuaciones:
        json.dump(datos, puntuaciones, indent = 2)
    print(f"Puntuación guardada con el nombre '{nombre}'")

def mostrar_posicion(nombre, resultado):
    archivo = "Puntuaciones/Puntuaciones.json"
    #Abrimos el archivo puntuaciones.json para volcar los datos en la variable 'datos'.
    with open(archivo, "r") as puntuaciones:
        datos = json.load(puntuaciones)
    #Creamos una función para usarla dentro del sort, ya que la lista 'datos' contiene diccionarios y hay que decirle
    #cómo queremos ordenar los datos.
    def obtener_puntuacion(posicion):
        return posicion['puntuacion']
    #Ordenamos los datos según la puntuación del jugador en orden descendente.
    datos.sort(key=obtener_puntuacion, reverse=True)

    for i in range(len(datos)):
        if datos[i]['nombre'] == nombre and datos[i]['puntuacion'] == resultado:
            print(f"{nombre}, estás en la posicion {(i+1)} del ranking con {resultado:.2f} puntos")

def realizar_ranking(cuestionario):
    tiempo_total = 180
    tiempo_inicio = time.time()
    aciertos = 0
    if cuestionario == "salir":
        return
    for pregunta in cuestionario:
        mostrar_pregunta(pregunta)
        #Calculamos cuanto tiempo resta para terminar el test antes de realizar cada pregunta.
        tiempo_restante = tiempo_total - (time.time() - tiempo_inicio)
        correccion = corregir_pregunta(obtener_respuesta(tiempo_restante), pregunta)
        if correccion == "salir":
            break
        else:
            aciertos += correccion
    tiempo_restante = tiempo_total - (time.time() - tiempo_inicio)
    resultado = calcular_puntuacion(aciertos, tiempo_restante)
    nombre = obtener_nombre(resultado)
    guardar_puntuacion(nombre, resultado)
    mostrar_posicion(nombre, resultado)

def mostrar_top10():
    archivo = "Puntuaciones/Puntuaciones.json"
    # Abrimos el archivo puntuaciones.json para volcar los datos en la variable 'datos'.
    with open(archivo, "r") as puntuaciones:
        datos = json.load(puntuaciones)
    # Creamos una función para usarla dentro del sort, ya que la lista 'datos' contiene diccionarios y hay que decirle
    # cómo queremos ordenar los datos.
    def obtener_puntuacion(posicion):
        return posicion['puntuacion']
    # Ordenamos los datos según la puntuación del jugador en orden descendente.
    datos.sort(key=obtener_puntuacion, reverse=True)
    lista_top10 = []
    if len(datos) >= 10:
        rango = 10
    else:
        rango = len(datos)
    for i in range(rango):
        lista_top10.append(datos[i])
    print("### TOP 10 ###")
    # Si no hay puntuaciones suficientes para mostrar en el TOP10, se muestra una cadena de guiones.
    for i in range (10):
        try:
            print(f"TOP{(i+1)} - {lista_top10[i]['nombre']} - {lista_top10[i]['puntuacion']:.2f} puntos")
        except IndexError:
            print(f"TOP{(i+1)} - ----------")

def menu_ranking(pool_preguntas):
    print("""Entrando a 'La Cima al Conocimiento'
Este modo es un modo ranking.
Se te enfrentará a un cuestionario de 20 preguntas donde la dificultad irá 'in crescendo'.
El límite de tiempo para completar el cuestionario es de 3 minutos y se tendrá en cuenta el tiempo utilizado.
Al finalizar se dará una puntuación en función del número de respuestas correctas y el tiempo que te haya sobrado.\n""")
    opcion = -1
    while not opcion == 3:
        try:
            opcion = int(input("""¿Qué quieres hacer?
1. Empezar a escalar 'La Cima al Conocimiento'
2. Ver TOP10 de mejores puntuaciones
3. Salir\n"""))
            match opcion:
                case 1:
                    realizar_ranking(preparar_cuestionario(pool_preguntas))
                    break
                case 2:
                    mostrar_top10()
                    break
                case 3:
                    print("Saliendo del modo 'La Cima al Conocimiento'.")
                    pass
                case _:
                    print("Opción no válida, por favor introduce una de las opciones de la lista.")
        except ValueError:
            print("Opción no válida, por favor introduce una de las opciones de la lista.")