import os
from datetime import datetime
from src.helper.checkName import checkName as checkName
from src.helper.printError import printError as error


def createPlayer(name: str) -> str:
    ''' 
    Función para crear un nuevo jugador. 
    '''
    name=name.strip()
    while name == '':
        error('\nDebes introducir un nombre.')
        name = input('\nIntroduce el nombre del jugador: ').strip()
        
    while not checkName(name):
        error('\nNombre inválido. Debe contener solo letras sin espacios.')
        name = input('\nIntroduce el nombre del jugador: ').strip()

    try: 
        os.mkdir(f'logs/game_{name}_{datetime.now().strftime("%Y-%m-%d_%H-%M-%S")}') # Crear carpeta para guardar los logs
        playerData = open(f'logs/game_{name}_{datetime.now().strftime("%Y-%m-%d_%H-%M-%S")}/playerName.txt', 'w', encoding='UTF-8')

        try: 
            playerData.write(f'PlayerName: {name}')
            print('\nJugador creado exitosamente.')
            
            return [f'logs/game_{name}_{datetime.now().strftime("%Y-%m-%d_%H-%M-%S")}', name]
        
        except Exception as err:
            print(f'\nError al escribir el archivo: {err}')

        finally:
            playerData.close()

    except FileNotFoundError: 
        print('\nNo se encuentra el archivo playerData.txt')

