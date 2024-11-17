from utilities.calcularPuntos import calcular_puntos as calcular_puntos

def testcalcular_puntos():
    assert calcular_puntos('truco', True, 25, 30, 'jugador2') == [25, 32], 'El jugador 2 deberia sumar 2 puntos'