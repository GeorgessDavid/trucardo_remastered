from utilities.calcularPuntos import calcular_puntos as calcular_puntos

def testcalcular_puntos1():
    assert calcular_puntos('Julián','truco', True, 25, 30, 'Jugador 2') == [25, 32], 'El jugador 2 deberia sumar 2 puntos'

def testcalcular_puntos2():
    assert calcular_puntos('Julián','truco', False, 22, 30, 'Jugador 2')  == [22, 31], 'El jugador 2 deberia sumar 1 punto'

def testcalcular_puntos3():
    assert calcular_puntos('Julián','truco' , True, 20 , 28, 'Julián')  == [22, 28], 'El jugador 1 debería sumar 2 puntos'

def testcalcular_puntos4():
    assert calcular_puntos('Julián','truco', False, 20, 28, 'Julián') == [21, 28], 'El jugador 1 debería sumar 1 punto'

def testcalcular_puntos5():
    assert calcular_puntos('Julián','retruco', True, 20, 28, 'Jugador 2') == [20, 31], 'El jugador 2 deberia sumar 3 puntos'

def testcalcular_puntos6():
    assert calcular_puntos('Julián','retruco', False, 20, 28, 'Jugador 2') == [20, 30], 'El jugador 2 deberia sumar 2 puntos'

def testcalcular_puntos7():
    assert calcular_puntos('Julián','retruco', True, 20, 28, 'Julián') == [23, 28], 'El jugador 1 deberia sumar 3 puntos'

def testcalcular_puntos8():
    assert calcular_puntos('Julián','retruco', False, 20, 28, 'Julián') == [22, 28], 'El jugador 1 deberia sumar 2 puntos'

def testcalcular_puntos9():
    assert calcular_puntos('Julián','vale cuatro', True, 20, 28, 'Jugador 2') == [20, 32], 'El jugador 2 deberia sumar 4 puntos'

def testcalcular_puntos10():
    assert calcular_puntos('Julián','vale cuatro', False, 20, 28, 'Jugador 2') == [20, 31], 'El jugador 2 deberia sumar 3 puntos'

def testcalcular_puntos11():
    assert calcular_puntos('Julián','vale cuatro', True, 20, 28, 'Julián') == [24, 28], 'El jugador 1 deberia sumar 4 puntos'

def testcalcular_puntos12():
    assert calcular_puntos('Julián','vale cuatro', False, 20, 28, 'Julián') == [23,28], 'El jugador 1 deberia sumar 3 puntos'

def tescalcular_puntos13():
    assert calcular_puntos('Julián','envido', True, 20, 28, 'Julián' ) == [22, 28], 'El jugador 1 deberia sumar 2 puntos'

def tescalcular_puntos14():
    assert calcular_puntos('Julián','envido', False, 20, 28, 'Julián' ) == [21, 28], 'El jugador 1 deberia sumar 1 punto'

def tescalcular_puntos15():
    assert calcular_puntos('Julián','envido', True, 20, 28, 'Jugador 2' ) == [20, 30], 'El jugador 2 deberia sumar 2 puntos'

def tescalcular_puntos16():
    assert calcular_puntos('Julián','envido', False, 20, 28, 'Jugador 2' ) == [20, 29], 'El jugador 1 deberia sumar 1 punto'

def tescalcular_puntos17():
    assert calcular_puntos('Julián','real envido', True, 20, 28, 'Julián' ) == [24, 28], 'El jugador 1 deberia sumar 4 puntos'

def tescalcular_puntos18():
    assert calcular_puntos('Julián','real envido', False, 20, 28, 'Julián' ) == [21, 28], 'El jugador 1 deberia sumar 1 punto'

def tescalcular_puntos19():
    assert calcular_puntos('Julián','real envido', True, 20, 28, 'Jugador 2' ) == [20, 32], 'El jugador 2 deberia sumar 4 puntos'

def tescalcular_puntos20():
    assert calcular_puntos('Julián','real envido', False, 20, 28, 'Jugador 2' ) == [20, 29], 'El jugador 1 deberia sumar 1 punto'

def tescalcular_puntos21():
    assert calcular_puntos('Julián','falta envido', True, 20, 28, 'Julián' ) == [1019, 28], 'El jugador 1 deberia sumar 999 puntos'

def tescalcular_puntos22():
    assert calcular_puntos('Julián','falta envido', False, 20, 28, 'Julián' ) == [21, 28], 'El jugador 1 deberia sumar 1 punto'

def tescalcular_puntos23():
    assert calcular_puntos('Julián','falta envido', True, 20, 28, 'Jugador 2' ) == [20, 1031], 'El jugador 2 deberia sumar 999 puntos'

def tescalcular_puntos24():
    assert calcular_puntos('Julián','falta envido', False, 20, 28, 'Jugador 2' ) == [20, 29], 'El jugador 1 deberia sumar 1 punto'