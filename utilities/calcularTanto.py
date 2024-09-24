from utilities.separarTanto import separar_tanto as separar_tanto

def calcular_tanto(cartas):
    while len(cartas) >= 2: 
        num = []
        palo = []
        # separamos los números y los palos
        for i in range(len(cartas)):
            naipe = separar_tanto(cartas[i])
            num.append(naipe[0])
            palo.append(naipe[1])
            
        tanto = 0

        # Caso particular de que las 3 cartas sean del mismo palo ya que no se utiliza la flor.
        if palo[0] == palo[1] == palo[2]:
            masAlta1 = 0
            masAlta2 = 0
            if num[0] < 10: 
                masAlta1 = num[0]

            if num[1] > masAlta1 and num[1] < 10:
                masAlta2 = masAlta1
                masAlta1 = num[1]
            if num[2] > masAlta1 and num[2] < 10:
                masAlta2 = masAlta1
                masAlta1 = num[2]
            elif num[2] > masAlta2 and num[2] < 10:
                masAlta2 = num[2]
            tanto = 20 + masAlta1 + masAlta2
            return tanto
        
        # Caso 1: Dos cartas del mismo palo y sin figuras
        if palo[0] == palo[1] and num[0] < 10 and num[1] < 10:
            tanto = 20 + num[0] + num[1]
            return tanto
        elif palo[0] == palo[2] and num[0] < 10 and num[2] < 10:
            tanto = 20 + num[0] + num[2]
            return tanto
        elif palo[1] == palo[2] and num[1] < 10 and num[2] < 10:
            tanto = 20 + num[1] + num[2]
            return tanto

        # Caso 2 Dos cartas del mismo palo y con almenos una figura
    
        elif palo[0] == palo[1]:
            if num[0] >= 10 and num[1] >= 10:
                tanto = 20
            elif num[0] >= 10:
                tanto = 20 + num[1]
            elif num[1] >= 10:
                tanto = 20 + num[0]
            return tanto
        elif palo[0] == palo[2]:
            if num[0] >= 10 and num[2] >= 10:
                tanto = 20
            elif num[0] >= 10:
                tanto = 20 + num[2]
            elif num[2] >= 10:
                tanto = 20 + num[0]
            return tanto
        elif palo[1] == palo[2]:
            if num[1] >= 10 and num[2] >= 10:
                tanto = 20
            elif num[1] >= 10:
                tanto = 20 + num[2]
            elif num[2] >= 10:
                tanto = 20 + num[1]
            return tanto

        # Caso 3 Ningún par de cartas del mismo palo
        else:
            cartaMasAlta = 0
            if (num[0] < 10):
                cartaMasAlta = num[0]
            
            if (num[1] < 10) and (num[1] >= cartaMasAlta):
                cartaMasAlta = num[1]
                            
            if (num[2] < 10) and (num[2] >= cartaMasAlta):
                cartaMasAlta = num[2]
            
            tanto = cartaMasAlta
            return tanto
""" 
print(calcular_tanto(['2 de Espadas', '3 de Espadas', '10 de Espadas'])) #Esperado: 25 - Obtenido: 13
print(calcular_tanto(['2 de Espadas', '10 de Espadas', '3 de Espadas']))#Esperado: 25 - Obtenido: 13
print(calcular_tanto(['10 de Espadas', '2 de Espadas', '3 de Espadas']))#Esperado: 25 - Obtenido: 13
print(calcular_tanto(['10 de Espadas', '2 de Espadas', '11 de Espadas'])) #Esperado: 22 - Obtenido: 21
print(calcular_tanto(['10 de Espadas', '2 de Espadas', '11 de Oros'])) #Esperado: 22 - Obtenido: 2 """