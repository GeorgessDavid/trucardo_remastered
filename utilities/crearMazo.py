def crear_mazo():
    palos = ('Espadas', 'Bastos', 'Oros', 'Copas')  # Usamos tupla ya que no se modificará
    valores = ('1', '2', '3', '4', '5', '6', '7', '10', '11', '12')  # También se convierte en tupla
    # Usamos comprensión de listas para generar el mazo
    return [f'{valor} de {palo}' for palo in palos for valor in valores]