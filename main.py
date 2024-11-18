import inquirer
import time
import sys
parent_dir="."
sys.path.append(parent_dir)

from game_logic import ejecutar_truco as ejecutar_truco
from src.controllers.player.player import createPlayer
from src.controllers.player.setLog import setLog
from src.controllers.log.showLogs import showLogs
from src.helper.colorLog import color as colorLog


# Ejecutar el juego
def main():
    options = [
        'Nuevo Juego',
        'Ver Historial',
        'Salir'
    ]

    questions = [
        inquirer.List('option', message="Selecciona una opción", choices=options)
    ]

    answer = inquirer.prompt(questions)


    if(answer['option'] == 'Nuevo Juego'):
        newGame = createPlayer(input('\nIngrese el nombre del jugador: '))
        
        path = newGame[0]
        name = newGame[1]
        
        if (path):
            print('\nInicializando...')
            time.sleep(3)
            setLog(path, ejecutar_truco, name)
    elif(answer['option'] == 'Ver Historial'):
        back = showLogs()
        if back:
            main()
    else:
        return

main()
print(colorLog(1,37, 40,'\nCopyright (r) LVA - La Vagancia Avanza - 2024. Todos los derechos reservados.\nTrucardoLVA'))
print('\nCréditos: \nProduct Owner: Georges David  \nProject Manager: Iván Díaz \nContent Creator: Felipe Iván Figueredo Alarcón\nCommunity Manager: Luca Ravello Benito\nGod: Lionel Andrés Messi Cuccitinni\n---------------------\nTech Adviser: Franco Martorella\nLawyer - Just In Case: Luciano Conde\n')