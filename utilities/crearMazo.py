def crear_mazo():
    palos = ('Espadas', 'Bastos', 'Oros', 'Copas')  # Usamos tupla ya que no se modificará
    valores = ('1', '2', '3', '4', '5', '6', '7', '10', '11', '12')  # También se convierte en tupla
    mazo = list(map(lambda carta: f'{carta[1]} de {carta[0]}', [(palo, valor) for palo in palos for valor in valores]))
    return mazo

# Probando la función
# mazo = crear_mazo()
# print(mazo)