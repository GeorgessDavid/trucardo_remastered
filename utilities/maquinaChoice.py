import random
from utilities.obtenerJerarquia import obtener_jerarquia
from utilities.calcularTanto import calcular_tanto

# Función para que la máquina decida si cantar o no

def maquinaDecideSiCantar(turno, juegoActual, confirmacion, manoMaq):
    cartasAltas = []
    cartasBajas = []
    for carta in manoMaq:
        jerarquia = obtener_jerarquia(carta)
        if jerarquia < 7:
            cartasAltas.append(jerarquia)
        else:
            cartasBajas.append(jerarquia)

    if ((juegoActual == 'envido' or juegoActual == 'real envido' or juegoActual == 'falta envido') and (confirmacion)):
        tanto = calcular_tanto(manoMaq)
        if tanto > 27:
            probabilidades = [0.9, 0.1]
        elif tanto > 23:
            probabilidades = [0.7, 0.3]
        elif tanto > 19:
            probabilidades = [0.5, 0.5]
        else:
            probabilidades = [0.0, 1.0]
    else:
        if (len(manoMaq) == 3):
            if len(cartasAltas) == 3:
                probabilidades = [0.9, 0.1]
            elif len(cartasAltas) == 2:
                probabilidades = [0.7, 0.3]
            elif len(cartasAltas) == 1:
                probabilidades = [0.5, 0.5]
            else:
                probabilidades = [0.3, 0.7]
        elif (len(manoMaq) == 2):
            if len(cartasAltas) == 2:
                probabilidades = [0.9, 0.1]
            elif len(cartasAltas) == 1:
                probabilidades = [0.5, 0.5]
            else:
                probabilidades = [0.3, 0.7]
        elif (len(manoMaq) == 1):
            if len(cartasAltas) == 1:
                probabilidades = [0.7, 0.3]
            else:
                probabilidades = [0.3, 0.7]

    if not confirmacion:
        # Seleccionar los juegos posibles según el turno y el estado actual del juego
        if (juegoActual in ['', 'no'] and turno == 1):
            
            tanto = calcular_tanto(manoMaq)
            if tanto > 27:
                probabilidades = [0.1, 0.2, 0.4, 0.2, 0.1]
            elif tanto > 23:
                probabilidades = [0.1, 0.4, 0.2, 0.2, 0.1]
            else:
                if len(cartasAltas) == 3:
                    probabilidades = [0.9, 0.0, 0.0, 0.0, 0.1]
                elif len(cartasAltas) == 2:
                    probabilidades = [0.7, 0.0, 0.0, 0.0, 0.3]
                elif len(cartasAltas) == 1:
                    probabilidades = [0.5, 0.0, 0.0, 0.0, 0.5]
                else:
                    probabilidades = [0.3, 0.0, 0.0, 0.0, 0.7]
            posiblesJuegos = ['truco', 'envido', 'real envido', 'falta envido', 'no']
            
        elif (juegoActual in ['', 'no'] and turno > 1):
            posiblesJuegos = ['truco', 'no']
        elif juegoActual == 'truco':
            posiblesJuegos = ['retruco', 'no']
        elif juegoActual == 'retruco':
            posiblesJuegos = ['vale cuatro', 'no']
        else:
            probabilidades = [1.0]
            posiblesJuegos = ['no']
    else:
        posiblesJuegos = ['si', 'no']
    # Elegir un juego al azar de las opciones posibles
    return random.choices(posiblesJuegos, weights=probabilidades, k=1)[0]


#Test
# maquinaDecideSiCantar(1, '', False, ['1 de Espadas', '4 de Oros', '2 de Bastos'])