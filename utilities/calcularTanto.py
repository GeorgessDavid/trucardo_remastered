from utilities.separarTanto import separar_tanto as separar_tanto

def calcular_tanto(cartas):
    if len(cartas) < 2:
        print('Error, se esperaba un arreglo de dos o más cartas')
        return 0

    # Separamos los números y los palos
    num = []
    palo = []
    for carta in cartas:
        naipe = separar_tanto(carta)
        num.append(naipe[0])
        palo.append(naipe[1])

    tanto = 0

    # Caso cuando las tres cartas son del mismo palo
    if palo[0] == palo[1] == palo[2]:
        mas_alta = max(num)
        num.remove(mas_alta)
        tanto = mas_alta + max(num)
        return tanto

    # Caso 1: Dos cartas del mismo palo y sin figuras
    for i in range(3):
        for j in range(i + 1, 3):
            if palo[i] == palo[j] and num[i] < 10 and num[j] < 10:
                tanto = 20 + num[i] + num[j]

            # Caso 2: Dos cartas del mismo palo con al menos una figura
            elif palo[i] == palo[j]:
                if num[i] > 10 or num[j] > 10:
                    tanto = 20 + min(num[i], num[j])

    # Caso 3: Ningún par de cartas del mismo palo
    if tanto == 0:
        tanto = max([n for n in num if n < 10], default=0)

    return tanto