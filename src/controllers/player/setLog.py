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
        # Normalizar cualquier tipo de salto de línea a "\n"
        message = message.replace("\r\n", "\n").replace("\r", "\n")
        
        # Eliminar secuencias ANSI estándar
        message = re.sub(r"\x1b\[[0-9;]*[A-Za-z]", "", message)
        
        # Eliminar secuencias específicas como "(B" y otros patrones no deseados
        message = re.sub(r"\x1b\(B", "", message)
        message = re.sub(r"\[?\?", "", message)
        
        # Eliminar "]" del principio de las líneas
        message = re.sub(r"^\] ", "", message, flags=re.MULTILINE)
        
        # Retornar con saltos de línea normalizados
        return message

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
