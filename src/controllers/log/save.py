def save(path: str, file: str, data: str) -> None:
    '''
    Función para guardar datos en una carpeta y archivos específicos.
    '''
    with open(f"{path}/{file}", "a", encoding="UTF-8") as f:
        f.write(data)