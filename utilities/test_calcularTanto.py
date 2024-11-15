from calcularTanto import calcular_tanto as calcularTanto

def test_calcularTanto(): 
    assert calcularTanto(['12 de Espadas', '1 de Espadas', '3 de Bastos']) == 21, 'Debería devolver 21'

def test_calcularTanto2():
    assert calcularTanto(['2 de Bastos', '3 de Espadas', '5 de Bastos']) == 27, 'Debería devolver 27'

def test_tresMismoPalo_unaFigura3():
    assert calcularTanto(['2 de Espadas', '3 de Espadas', '10 de Espadas']) == 25, 'Debería devolver 25'
    
def test_tresMismoPalo_unaFigura2():
    assert calcularTanto(['2 de Espadas', '10 de Espadas', '3 de Espadas']) == 25, 'Debería devolver 25'
    
def test_tresMismoPalo_unaFigura1():
    assert calcularTanto(['10 de Espadas', '2 de Espadas', '3 de Espadas']) == 25, 'Debería devolver 25'

def test_tresMismoPalo_dosFiguras1_3():
    assert calcularTanto(['10 de Espadas', '2 de Espadas', '11 de Espadas']) == 22, 'Debería devolver 22'
    
def test_dosMismoPalo_unaFigura():
    assert calcularTanto(['10 de Espadas', '2 de Espadas', '11 de Oros']) == 22, 'Debería devolver 22'