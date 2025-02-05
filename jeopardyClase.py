import random

# Base de datos de preguntas organizadas por niveles con más preguntas
jeopardy = {
    "Fácil": [
        {"pregunta": "¿Cuál es la capital de Francia?", "respuesta": "París", "opciones": ["Londres", "París", "Madrid", "Roma"]},
        {"pregunta": "¿Cuántos días tiene una semana?", "respuesta": "7", "opciones": ["5", "6", "7", "8"]},
        {"pregunta": "¿Qué planeta es conocido como el Planeta Rojo?", "respuesta": "Marte", "opciones": ["Marte", "Venus", "Júpiter", "Saturno"]},
        {"pregunta": "¿Cuántos lados tiene un triángulo?", "respuesta": "3", "opciones": ["3", "4", "5", "6"]},
        {"pregunta": "¿Qué animal dice 'muu'?", "respuesta": "Vaca", "opciones": ["Perro", "Gato", "Vaca", "Caballo"]}
    ],
    "Intermedio": [
        {"pregunta": "¿Cuál es el gas más abundante en la atmósfera?", "respuesta": "Nitrógeno", "opciones": ["Oxígeno", "Nitrógeno", "Dióxido de carbono", "Hidrógeno"]},
        {"pregunta": "¿Cuál es el río más largo del mundo?", "respuesta": "Amazonas", "opciones": ["Nilo", "Amazonas", "Yangtsé", "Misisipi"]},
        {"pregunta": "¿Qué país es conocido como la tierra del sol naciente?", "respuesta": "Japón", "opciones": ["China", "Japón", "Corea", "Tailandia"]},
        {"pregunta": "¿Cuántos colores tiene el arcoíris?", "respuesta": "7", "opciones": ["6", "7", "8", "9"]},
        {"pregunta": "¿En qué continente se encuentra Egipto?", "respuesta": "África", "opciones": ["Asia", "África", "Europa", "América"]}
    ],
    "Difícil": [
        {"pregunta": "¿En qué año llegó el hombre a la Luna?", "respuesta": "1969", "opciones": ["1969", "1970", "1958", "1965"]},
        {"pregunta": "¿Quién desarrolló la teoría de la relatividad?", "respuesta": "Einstein", "opciones": ["Newton", "Tesla", "Einstein", "Galileo"]},
        {"pregunta": "¿Cuál es el elemento químico con símbolo Au?", "respuesta": "Oro", "opciones": ["Oro", "Plata", "Hierro", "Cobre"]},
        {"pregunta": "¿Qué país ganó la Copa Mundial de Fútbol en 2018?", "respuesta": "Francia", "opciones": ["Francia", "Croacia", "Brasil", "Alemania"]},
        {"pregunta": "¿Cuál es la velocidad de la luz en el vacío?", "respuesta": "300,000 km/s", "opciones": ["300,000 km/s", "150,000 km/s", "1,000,000 km/s", "299,792 km/s"]}
    ],
}

# Función para mostrar pregunta y opciones en orden aleatorio
def mostrar_pregunta(pregunta):
    print(f"\nPregunta: {pregunta['pregunta']}")
    opciones = pregunta['opciones']
    random.shuffle(opciones)  # Mezcla las opciones
    for i, opcion in enumerate(opciones, 1):
        print(f"{i}. {opcion}")
    return opciones

# Función para usar ayudas
def usar_ayuda(pregunta, ayudas):
    print("\nAyudas disponibles:")
    for ayuda, disponible in ayudas.items():
        if disponible:
            print(f"- {ayuda}")
    eleccion = input("¿Qué ayuda quieres usar? (Escribe el nombre o 'ninguna'): ").strip().lower()

    if eleccion == "50/50" and ayudas["50/50"]:
        print("Usaste 50/50. Eliminando dos respuestas incorrectas...")
        correctas = [pregunta["respuesta"]]
        incorrectas = [op for op in pregunta["opciones"] if op != pregunta["respuesta"]]
        opciones_mostradas = correctas + random.sample(incorrectas, 1)
        random.shuffle(opciones_mostradas)
        print(f"Opciones restantes: {opciones_mostradas}")
        ayudas["50/50"] = False
        return opciones_mostradas
    elif eleccion == "llamada a un amigo" and ayudas["llamada a un amigo"]:
        print("Tu amigo dice que la respuesta es probablemente:", pregunta["respuesta"])
        ayudas["llamada a un amigo"] = False
    elif eleccion == "preguntar al público" and ayudas["preguntar al público"]:
        print("El público vota así:")
        for opcion in pregunta["opciones"]:
            porcentaje = random.randint(0, 100)
            print(f"{opcion}: {porcentaje}%")
        ayudas["preguntar al público"] = False
    else:
        print("No usaste ninguna ayuda o ya no está disponible.")
    return pregunta["opciones"]

# Bucle principal del juego
def jugar_jeopardy():
    dinero_acumulado = 0
    rondas = 0
    ayudas = {"50/50": True, "llamada a un amigo": True, "preguntar al público": True}

    print("¡Bienvenido al juego de Jeopardy!\n")

    for nivel, preguntas in jeopardy.items():
        premio_por_nivel = {"Fácil": 100, "Intermedio": 300, "Difícil": 500}
        print(f"--- Nivel: {nivel} ---")
        preguntas_random = random.sample(preguntas, len(preguntas))  # Seleccionar preguntas aleatorias
        for pregunta in preguntas_random:
            rondas += 1
            print(f"\nRonda {rondas}")
            opciones = mostrar_pregunta(pregunta)

            if any(ayudas.values()):
                usar_ayuda_opcion = input("¿Quieres usar una ayuda? (sí/no): ").strip().lower()
                if usar_ayuda_opcion == "sí":
                    opciones = usar_ayuda(pregunta, ayudas)

            respuesta = input("Ingresa el número de tu respuesta: ").strip()
            try:
                eleccion = opciones[int(respuesta) - 1]
                if eleccion == pregunta["respuesta"]:
                    print("¡Correcto!")
                    dinero_acumulado += premio_por_nivel[nivel]
                    print(f"Ganaste ${premio_por_nivel[nivel]}. Dinero acumulado: ${dinero_acumulado}")
                else:
                    print(f"Incorrecto. La respuesta correcta era: {pregunta['respuesta']}")
                    print(f"Te vas con ${dinero_acumulado}")
                    return
            except (ValueError, IndexError):
                print("Entrada no válida. Perdiste la oportunidad.")
                print(f"Te vas con ${dinero_acumulado}")
                return

            # Cada 4 rondas, preguntar si quiere retirarse
            if rondas % 4 == 0:
                continuar = input("\n¿Quieres continuar o retirarte? (continuar/retirarse): ").strip().lower()
                if continuar == "retirarse":
                    print(f"Te retiraste con ${dinero_acumulado}")
                    return

    print(f"\nEl juego ha terminado. Dinero total acumulado: ${dinero_acumulado}")

# Iniciar el juego
jugar_jeopardy()
