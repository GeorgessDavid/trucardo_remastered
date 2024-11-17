import random

# Función para que la máquina decida si cantar o no

def maquinaDecideSiCantar(turno, juegoActual, confirmacion, manoMaq):
    
    if not confirmacion:
        # Seleccionar los juegos posibles según el turno y el estado actual del juego
        if (juegoActual in ['', 'no'] and turno == 1):
            posiblesJuegos = ['truco', 'envido', 'real envido', 'falta envido', 'no']
        elif (juegoActual in ['', 'no'] and turno > 1):
            posiblesJuegos = ['truco', 'no']
        elif juegoActual == 'truco':
            posiblesJuegos = ['retruco', 'no']
        elif juegoActual == 'retruco':
            posiblesJuegos = ['vale cuatro', 'no']
        else:
            posiblesJuegos = ['no']
    else:
        posiblesJuegos = ['si', 'no']

    # Elegir un juego al azar de las opciones posibles
    return random.choice(posiblesJuegos)
