from utilities.obtenerJerarquia import obtener_jerarquia as obtener_jerarquia

def determinar_ganador(name: str, carta1: str, carta2: str):
    '''
    Función para calcular el ganador entre dos cartas
    '''
    # Encontrar los índices de las cartas
    valor_carta1 = obtener_jerarquia(carta1)
    valor_carta2 = obtener_jerarquia(carta2)
    
    # Determinar el ganador
    if valor_carta1 < valor_carta2:
        ganadorUltimaRonda = name
    elif valor_carta2 < valor_carta1:
        ganadorUltimaRonda = 'La CPU'
    else:
        ganadorUltimaRonda = 'Empate'

    return ganadorUltimaRonda