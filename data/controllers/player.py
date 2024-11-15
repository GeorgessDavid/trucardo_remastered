from helper.checkName import checkName as checkName

def createPlayer(name: str):
    ''' 
    Función para crear un nuevo jugador. 
    '''
    
    if not checkName(name):
        raise ValueError("No puede ingresar números en el nombre del jugador.")

    return name

print(createPlayer("Lionel Messi"))