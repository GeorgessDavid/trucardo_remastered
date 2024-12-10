from utilities.determinarGanador import determinar_ganador as determinarGanador

def test_determinarGanador1():
    assert determinarGanador('Julián', '4 de Espadas', '5 de Espadas') == 'La CPU', 'La CPU debería ganar'

def test_determinarGanador2():
    assert determinarGanador('Julián', '5 de Espadas', '4 de Espadas') == 'Julián', 'Julián debería ganar'

def test_determinarGanador3():
    assert determinarGanador('Julián', '4 de Espadas', '4 de Espadas') == 'Empate', 'Debería haber empate'

def test_determinarGanador4():
    assert determinarGanador('Julián', '4 de Espadas', '1 de Espadas') == 'La CPU', 'La CPU debería ganar'

def test_determinarGanador5():
    assert determinarGanador('Julián', '1 de Espadas', '4 de Espadas') == 'Julián', 'Julián debería ganar'

def test_determinarGanador6():
    assert determinarGanador('Julián', '1 de Espadas', '12 de Oros') == 'Julián', 'Debería haber empate'
    
def test_determinarGanador7():
    assert determinarGanador('Julián', '12 de Oros', '1 de Espadas') == 'La CPU', 'Debería haber empate'
    
def test_determinarGanador8():
    assert determinarGanador('Julián', '7 de Oros', '7 de Espadas') == 'La CPU', 'La CPU debería ganar'

def test_determinarGanador9():
    assert determinarGanador('Julián', '7 de Bastos', '7 de Copas') == 'Empate', 'Debería haber empate'