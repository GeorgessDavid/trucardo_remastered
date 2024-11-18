import inquirer
def selectorMenu(options: list, title: str, returnType: str):
    questions = [
        inquirer.List('option', message=title, choices=options)
    ]
    answer = inquirer.prompt(questions)
    
    if returnType == 'index':
        return options.index(answer['option'])
    
    return answer['option']