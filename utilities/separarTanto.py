def separarTanto(string):
    numero = ''
    palo = ''
    
    partes = string.split(' de ')
    numero = int(partes[0])
    palo = partes[1]

    return [numero, palo]