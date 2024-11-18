def calcular_puntos(playerName: str, juego: str, seQuiere: bool, puntosjugador1: int, puntosjugador2: int, jugadorQueSuma: str) -> list:    
    # Definir los puntos para cada tipo de juego
    puntos_juego = {
        'truco': [1, 2],
        'retruco': [2, 3],
        'vale cuatro': [3, 4],
        'envido': [1, 2],
        'real envido': [1, 4],
        'falta envido': [1, 999]
    }

    # Verificar si el juego es válido
    juegosPermitidos = list(filter(lambda key: key in puntos_juego.keys(), [juego]))
    
    # Si no se cantó ni truco ni envido, se suma un punto.
    if len(juegosPermitidos) == 0:
        print('No se cantó ni truco ni envido. Sólo se suma un punto.')
    
    # Obtener los puntos según si se quiso o no
    puntos = puntos_juego.get(juego, [1, 1])[1 if seQuiere else 0]

    # Sumar los puntos al jugador correspondiente
    if jugadorQueSuma == playerName:
        puntosjugador1 += puntos
    else:
        puntosjugador2 += puntos

    return [puntosjugador1, puntosjugador2]