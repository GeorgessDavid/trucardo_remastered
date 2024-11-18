import inquirer

def selectorMenu(options: list, title: str, returnType: str):
    '''
    Función para crear menú de selección de opciones.
    
    Parámetros:
    - options (Array): lista de opciones a seleccionar.
    - title (String): título del menú.
    - returnType (String): tipo de retorno de la función. Puede ser 'index', para recibir un integer con la posición de la opción, o 'value', para recibir la opción seleccionada.
    '''
    questions = [
        inquirer.List('option', message=title, choices=options)
    ]
    answer = inquirer.prompt(questions)
    
    if returnType == 'index':
        return options.index(answer['option'])
    
    return answer['option']