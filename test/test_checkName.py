from src.helper.checkName import checkName

def test_checkName1():
    assert checkName('Juan') == True, 'El nombre debería ser válido.'

def test_checkName2():
    assert checkName('Juan Carlos') == True, 'El nombre debería ser válido.'

def test_checkName3():
    assert checkName('Juan Carlos 123') == False, 'El nombre no debería ser válido.'

def test_checkName4():
    assert checkName('Sebastián') == True, 'El nombre debería ser válido.'

def test_checkName():
    assert checkName('Sebastián 123') == False, 'El nombre no debería ser válido.'