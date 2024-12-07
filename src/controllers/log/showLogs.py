import inquirer
import os
import time
from src.helper.colorLog import color as colorLog

def showLogs():
    options = [
        'Volver'
    ]

    try:
        files = os.listdir('logs')
        
        for file in files:
            options.insert(0, file)
    except FileNotFoundError:
        print("La carpeta no existe")

    questions = [
        inquirer.List('option', message=colorLog(1,32,40,"Elije una partida"), choices=options)
    ]

    answer = inquirer.prompt(questions)

    if answer['option'] != 'Volver':
        try:
            with open(f'logs/{answer["option"]}', 'r', encoding="UTF-8") as doc:
                print(colorLog(1,32,40, f"Cargando la partida..."))
                time.sleep(2)
                print(colorLog(1,32,40, f"Partida: {answer['option']}"))
                time.sleep(1)
                print("\n====================\n")
                print(doc.read())
                print("\n====================\n")
                showLogs()
        except FileNotFoundError:
            print("El archivo no existe")
    else:
        return True