# Función para separar el tanto recibido, devuelve número como integer y el palo de la carta.
def separar_tanto(string):
    # Desempaquetamos directamente el resultado de split en dos variables
    numero, palo = string.split(' de ')

    # Convertimos el número en entero y retornamos la lista
    return [int(numero), palo]