# import os
from datetime import datetime
from src.helper.checkName import checkName as checkName


class DuplicatePlayerError(Exception):
    '''
    Error personalizado para indicar que el nombre del jugador ya se encuentra en uso.
    '''
    def __init__(self, mensaje):
        self.mensaje = mensaje
        super().__init__(self.mensaje)

# def getPlayers():
#     '''
#     Función para obtener el listado de jugadores y mostrarlos por pantalla.
#     '''
#     try:
#         playerData = open('./playerData.txt', "r", encoding="UTF-8")

#         for line in playerData:
#             print(f'\n{line}')

#     except FileNotFoundError: 
#         print('\nNo se encuentra el archivo playerData.txt')
        

def createPlayer(name: str) -> str:
    ''' 
    Función para crear un nuevo jugador. 
    '''

    if not checkName(name):
        raise ValueError("\nNo puede ingresar números en el nombre del jugador.")

    try: 
        playerData = open(f'logs/game_{name}_{datetime.now().strftime("%Y-%m-%d_%H-%M-%S")}.txt', "w", encoding="UTF-8")

        try: 
            playerData.write(f'PlayerName: {name}')
            print('\nJugador creado exitosamente.')
            return f'logs/game_{name}_{datetime.now().strftime("%Y-%m-%d_%H-%M-%S")}.txt'
        except Exception as err:
            print(f'\nError al escribir el archivo: {err}')
        finally: 
            playerData.close()
    except FileNotFoundError: 
        print('\nNo se encuentra el archivo playerData.txt')

