from src.constantes import JERARQUIA

def obtener_jerarquia(carta):
    for i, grupo in enumerate(JERARQUIA):  # Enumeramos para obtener el índice y el grupo
        if carta in grupo:  # Verificamos si la carta está en el grupo
            return i