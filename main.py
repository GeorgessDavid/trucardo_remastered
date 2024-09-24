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
    
     # Determinar el ganador
    if valor_carta1 < valor_carta2:
        ganadorUltimaRonda = 'Jugador 1'
    elif valor_carta2 < valor_carta1:
        ganadorUltimaRonda = 'Jugador 2'
    else:
        ganadorUltimaRonda = 'Empate'

    return ganadorUltimaRonda

# Función para separar el tanto recibido, devuelve número como integer y el palo de la carta.
def separar_tanto(string):
    # Desempaquetamos directamente el resultado de split en dos variables
    numero, palo = string.split(' de ')

    # Convertimos el número en entero y retornamos la lista
    return [int(numero), palo]

def calcular_tanto(cartas):
    if len(cartas) < 2:
        print('Error, se esperaba un arreglo de dos o más cartas')
        return 0

    # Separamos los números y los palos
    num = []
    palo = []
    for carta in cartas:
        naipe = separar_tanto(carta)
        num.append(naipe[0])
        palo.append(naipe[1])

    tanto = 0

    # Caso cuando las tres cartas son del mismo palo
    if palo[0] == palo[1] == palo[2]:
        mas_alta = max(num)
        num.remove(mas_alta)
        tanto = mas_alta + max(num)
        return tanto

    # Caso 1: Dos cartas del mismo palo y sin figuras
    for i in range(3):
        for j in range(i + 1, 3):
            if palo[i] == palo[j] and num[i] < 10 and num[j] < 10:
                tanto = 20 + num[i] + num[j]

            # Caso 2: Dos cartas del mismo palo con al menos una figura
            elif palo[i] == palo[j]:
                if num[i] > 10 or num[j] > 10:
                    tanto = 20 + min(num[i], num[j])

    # Caso 3: Ningún par de cartas del mismo palo
    if tanto == 0:
        tanto = max([n for n in num if n < 10], default=0)

    return tanto

def calcular_puntos(juego, seQuiere, puntosjugador1, puntosjugador2, jugadorQueSuma):
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