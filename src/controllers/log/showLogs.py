import inquirer
import os
import time
from src.helper.colorLog import color as colorLog
from src.helper.selectorMenu import selectorMenu

def showLogs():
    options = [
        'Volver'
    ]

    try:
        games = os.listdir('logs')
        
        for game in games:
            options.insert(0, game)
    except FileNotFoundError:
        print("La carpeta no existe")

    selected = selectorMenu(options, 'Seleccione una partida', 'value')

    if selected != 'Volver':
        try:
            fileOptions = [
                'Volver'
            ]
            
            files = os.listdir(f'logs/{selected}') 
            print(files)
            
            for file in files: fileOptions.insert(0, file)
                

            fileSelect = selectorMenu(fileOptions, 'Elija una opción', 'value')

            showLogs() if fileSelect is 'Volver' else None

            with open(f'logs/{selected}/{fileSelect}', 'r', encoding="UTF-8") as doc:
                print(colorLog(1,32,40, f"Cargando la partida..."))
                time.sleep(2)
                print(colorLog(1,32,40, f"Archivo: {fileSelect}"))
                time.sleep(1)
                print("\n====================\n")
                print(doc.read())
                print("\n====================\n")
                showLogs()
        except FileNotFoundError:
            print("El archivo no existe")
    else:
        return True