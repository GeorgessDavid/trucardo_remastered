import random

# Definimos la jerarquía de las cartas en el Truco.
JERARQUIA = [
    ['1 de Espadas'],
    ['1 de Bastos'],
    ['7 de Espadas'],
    ['7 de Oros'],
    tuple(['3 de Espadas', '3 de Oros', '3 de Copas', '3 de Bastos']),
    tuple(['2 de Espadas', '2 de Oros', '2 de Copas', '2 de Bastos']),
    tuple(['1 de Copas', '1 de Oros']),
    tuple(['12 de Espadas', '12 de Oros', '12 de Copas', '12 de Bastos']),
    tuple(['11 de Espadas', '11 de Oros', '11 de Copas', '11 de Bastos']),
    tuple(['10 de Espadas', '10 de Oros', '10 de Copas', '10 de Bastos']),
    tuple(['7 de Copas', '7 de Bastos']),
    tuple(['6 de Espadas', '6 de Oros', '6 de Copas', '6 de Bastos']),
    tuple(['5 de Espadas', '5 de Oros', '5 de Copas', '5 de Bastos']),
    tuple(['4 de Espadas', '4 de Oros', '4 de Copas', '4 de Bastos'])
]

def crear_mazo():
    palos = ('Espadas', 'Bastos', 'Oros', 'Copas')  # Usamos tupla ya que no se modificará
    valores = ('1', '2', '3', '4', '5', '6', '7', '10', '11', '12')  # También se convierte en tupla
    # Usamos comprensión de listas para generar el mazo
    return [f'{valor} de {palo}' for palo in palos for valor in valores]

# Función para definir la jerarquía de las cartas.
def obtener_jerarquia(carta):
    for i, grupo in enumerate(JERARQUIA):  # Enumeramos para obtener el índice y el grupo
        if carta in grupo:  # Verificamos si la carta está en el grupo
            return i

# Función para barajar y repartir las cartas
def repartir_cartas(mazo):
    random.shuffle(mazo)
    # Usamos slicing para asignar las cartas a cada jugador
    mano_jugador1 = mazo[:3]  # Las primeras tres cartas para el jugador 1
    mano_jugador2 = mazo[3:6]  # Las siguientes tres cartas para el jugador 2
    # Retornamos las manos y el mazo restante
    return [mano_jugador1, mano_jugador2, mazo[6:]]  # Devolvemos el mazo restante


def determinar_ganador(carta1, carta2):
    # Encontrar los índices de las cartas
    valor_carta1 = obtener_jerarquia(carta1)
    valor_carta2 = obtener_jerarquia(carta2)