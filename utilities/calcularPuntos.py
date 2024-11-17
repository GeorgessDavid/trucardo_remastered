def calcular_puntos(juego: str, seQuiere: bool, puntosjugador1: int, puntosjugador2: int, jugadorQueSuma: str) -> list:
    # Definir los puntos para cada tipo de juego
    puntos_juego = {
        'truco': [1, 2],
        'retruco': [2, 3],
        'vale cuatro': [3, 4],
        'envido': [1, 2],
        'real envido': [1, 4],
        'falta envido': [1, 999]
    }

    # Obtener los puntos según si se quiso o no
    puntos = puntos_juego.get(juego, [1, 1])[1 if seQuiere else 0]

    # Sumar los puntos al jugador correspondiente
    if jugadorQueSuma == 'Jugador 1':
        puntosjugador1 += puntos
    else:
        puntosjugador2 += puntos

    return [puntosjugador1, puntosjugador2]