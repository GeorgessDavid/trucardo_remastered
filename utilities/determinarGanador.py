from utilities.obtenerJerarquia import obtener_jerarquia as obtener_jerarquia

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