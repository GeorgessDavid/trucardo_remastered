import inquirer
import time
import sys
parent_dir="."
sys.path.append(parent_dir)

from game_logic import ejecutar_truco as ejecutar_truco
from src.controllers.player.player import createPlayer
from src.controllers.player.setLog import setLog
# from src.controllers.player.player import getPlayers;


# Ejecutar el juego
def main():
    options = [
        'Nuevo Juego',
        'Cargar Juego',
        'Salir'
    ]

    questions = [
        inquirer.List('option', message="Selecciona una opción", choices=options)
    ]

    answer = inquirer.prompt(questions)

    if(answer['option'] == 'Salir'):
        print('alto puto sos gato de mierda no te dan los huevos')
        return
    elif(answer['option'] == 'Nuevo Juego'):
        path = createPlayer(input('\nIngrese su nombre: '))
        print(path)
        if (path):
            print('\nInicializando...')
            time.sleep(3)
            setLog(path, ejecutar_truco)
        

main()