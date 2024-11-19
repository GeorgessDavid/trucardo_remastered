import sys
import re

class DualOutput:
    def __init__(self, file):
        self.terminal = sys.stdout  # Guardar la salida estándar original (consola)
        self.file = file  # Archivo donde se escribirán los logs

    @staticmethod
    def sanitize_message(message: str):
        """
        Sanitiza un mensaje limpiando los símbolos especiales devueltos por la función color.
        """
        
        sanitized = re.sub(r"\[\w+|\(\w", "", sanitized)
        sanitized = re.sub(r"\x1b\[[0-9;]*[a-zA-Z]", "", message)
        return sanitized
        # return re.sub(r"(\[\d;\d+;\d+m)|(\[\dm)", "", message.replace("\x1b", ""))

    def write(self, message: str):
        self.terminal.write(message)  # Escribir en la consola
        self.file.write(self.sanitize_message(message)) # Escribir en el archivo
        
    
    def flush(self):
        # Asegura que los datos se escriban inmediatamente
        self.terminal.flush()
        self.file.flush()

def setLog(path: str, func, name:str ) -> bool:
    # Abrimos el archivo en modo A
    with open(path, 'a', encoding="UTF-8") as doc:
        dual_output = DualOutput(doc)  # Crear la salida dual
        original_stdout = sys.stdout  # Guardar la salida original
        sys.stdout = dual_output  # Redirigir stdout

        try:
            func(name)  # Ejecutar la función
        finally:
            sys.stdout = original_stdout  # Restaurar stdout

    return True
