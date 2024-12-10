from utilities.separarTanto import separar_tanto as separarTanto

def test_separarTanto1():
    assert separarTanto('1 de Espadas') == [1, 'Espadas'], 'El tanto debería ser 1 de Espadas'

def test_separarTanto2():
    assert separarTanto('2 de Espadas') == [2, 'Espadas'], 'El tanto debería ser 2 de Espadas'

def test_separarTanto3():
    assert separarTanto('3 de Espadas') == [3, 'Espadas'], 'El tanto debería ser 3 de Espadas'
    
def test_separarTanto4():
    assert separarTanto('4 de Espadas') == [4, 'Espadas'], 'El tanto debería ser 4 de Espadas'

def test_separarTanto5():
    assert separarTanto('5 de Espadas') == [5, 'Espadas'], 'El tanto debería ser 5 de Espadas'