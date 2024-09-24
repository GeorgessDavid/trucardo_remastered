import random
# Función para barajar y repartir las cartas
def repartir_cartas(mazo):
    random.shuffle(mazo)
    # Usamos slicing para asignar las cartas a cada jugador
    mano_jugador1 = mazo[:3]  # Las primeras tres cartas para el jugador 1
    mano_jugador2 = mazo[3:6]  # Las siguientes tres cartas para el jugador 2
    # Retornamos las manos y el mazo restante
    return [mano_jugador1, mano_jugador2, mazo[6:]]  # Devolvemos el mazo restante