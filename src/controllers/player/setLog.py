import sys

class DualOutput:
    def __init__(self, file):
        self.terminal = sys.stdout  # Guardar la salida estándar original (consola)
        self.file = file  # Archivo donde se escribirán los logs

    def write(self, message):
        self.terminal.write(message)  # Escribir en la consola
        self.file.write(message)  # Escribir en el archivo

    def flush(self):
        # Asegura que los datos se escriban inmediatamente
        self.terminal.flush()
        self.file.flush()

def setLog(path: str, func) -> bool:
    # Abrimos el archivo en modo A
    with open(path, 'a', encoding="UTF-8") as doc:
        dual_output = DualOutput(doc)  # Crear la salida dual
        original_stdout = sys.stdout  # Guardar la salida original
        sys.stdout = dual_output  # Redirigir stdout

        try:
            func()  # Ejecutar la función
        finally:
            sys.stdout = original_stdout  # Restaurar stdout

    return True
