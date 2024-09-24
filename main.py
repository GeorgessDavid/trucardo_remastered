import random

# Definimos la jerarquía de las cartas en el Truco.
JERARQUIA = [
    ['1 de Espadas'],
    ['1 de Bastos'],
    ['7 de Espadas'],
    ['7 de Oros'],
    tuple(['3 de Espadas', '3 de Oros', '3 de Copas', '3 de Bastos']),
    tuple(['2 de Espadas', '2 de Oros', '2 de Copas', '2 de Bastos']),
    tuple(['1 de Copas', '1 de Oros']),
    tuple(['12 de Espadas', '12 de Oros', '12 de Copas', '12 de Bastos']),
    tuple(['11 de Espadas', '11 de Oros', '11 de Copas', '11 de Bastos']),
    tuple(['10 de Espadas', '10 de Oros', '10 de Copas', '10 de Bastos']),
    tuple(['7 de Copas', '7 de Bastos']),
    tuple(['6 de Espadas', '6 de Oros', '6 de Copas', '6 de Bastos']),
    tuple(['5 de Espadas', '5 de Oros', '5 de Copas', '5 de Bastos']),
    tuple(['4 de Espadas', '4 de Oros', '4 de Copas', '4 de Bastos'])
]

def crear_mazo():
    palos = ('Espadas', 'Bastos', 'Oros', 'Copas')  # Usamos tupla ya que no se modificará
    valores = ('1', '2', '3', '4', '5', '6', '7', '10', '11', '12')  # También se convierte en tupla
    # Usamos comprensión de listas para generar el mazo
    return [f'{valor} de {palo}' for palo in palos for valor in valores]

# Función para definir la jerarquía de las cartas.
def obtener_jerarquia(carta):
    for i, grupo in enumerate(JERARQUIA):  # Enumeramos para obtener el índice y el grupo
        if carta in grupo:  # Verificamos si la carta está en el grupo
            return i

# Función para barajar y repartir las cartas
def repartir_cartas(mazo):
    random.shuffle(mazo)
    # Usamos slicing para asignar las cartas a cada jugador
    mano_jugador1 = mazo[:3]  # Las primeras tres cartas para el jugador 1
    mano_jugador2 = mazo[3:6]  # Las siguientes tres cartas para el jugador 2
    # Retornamos las manos y el mazo restante
    return [mano_jugador1, mano_jugador2, mazo[6:]]  # Devolvemos el mazo restante


def determinar_ganador(carta1, carta2):
    # Encontrar los índices de las cartas
    valor_carta1 = obtener_jerarquia(carta1)
    valor_carta2 = obtener_jerarquia(carta2)
    
     # Determinar el ganador
    if valor_carta1 < valor_carta2:
        ganadorUltimaRonda = 'Jugador 1'
    elif valor_carta2 < valor_carta1:
        ganadorUltimaRonda = 'Jugador 2'
    else:
        ganadorUltimaRonda = 'Empate'

    return ganadorUltimaRonda

# Función para separar el tanto recibido, devuelve número como integer y el palo de la carta.
def separar_tanto(string):
    # Desempaquetamos directamente el resultado de split en dos variables
    numero, palo = string.split(' de ')

    # Convertimos el número en entero y retornamos la lista
    return [int(numero), palo]

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

def calcular_puntos(juego, seQuiere, puntosjugador1, puntosjugador2, jugadorQueSuma):
    # Definir los puntos para cada tipo de juego
    puntos_juego = {
        'truco': [1, 2],
        'retruco': [2, 3],
        'vale cuatro': [3, 4],
        'envido': [1, 2],
        'real envido': [1, 4],
        'falta envido': [1, 999]
    }

    # Obtener los puntos según si se quiso o no
    puntos = puntos_juego.get(juego, [1, 1])[1 if seQuiere else 0]

    # Sumar los puntos al jugador correspondiente
    if jugadorQueSuma == 'Jugador 1':
        puntosjugador1 += puntos
    else:
        puntosjugador2 += puntos

    return [puntosjugador1, puntosjugador2]

def maquinaDecideSiCantar(turno, juegoActual, confirmacion):
    if not confirmacion:
        # Seleccionar los juegos posibles según el turno y el estado actual del juego
        if (juegoActual in ['', 'no'] and turno == 1):
            posiblesJuegos = ['truco', 'envido', 'real envido', 'falta envido', 'no']
        elif (juegoActual in ['', 'no'] and turno > 1):
            posiblesJuegos = ['truco', 'no']
        elif juegoActual == 'truco':
            posiblesJuegos = ['retruco', 'no']
        elif juegoActual == 'retruco':
            posiblesJuegos = ['vale cuatro', 'no']
        else:
            posiblesJuegos = ['no']
    else:
        posiblesJuegos = ['si', 'no']

    # Elegir un juego al azar de las opciones posibles
    return random.choice(posiblesJuegos)

def jugar_truco(puntosjugador1, puntosjugador2, mazo):
    if(len(mazo) <= 10):
        mazo = crear_mazo()
    cartas = repartir_cartas(mazo)
    mano_jugador1 = cartas[0]
    mano_jugador2 = cartas[1]
    juego = ''
    turno = 1
    ganadorUltimaRonda = 'Jugador 1' #Default Jugador 1
    rondasGanadasJugador1 = 0
    rondasGanadasJugador2 = 0
    cantoMaquina = False
    cantoJugador = False
    envidoNoQuerido = False
    
    
    while(turno < 4 and rondasGanadasJugador1 < 2 and rondasGanadasJugador2 < 2):
        if(len(mazo) <= 10):
            mazo = crear_mazo()
        confirmacion = ''
        cartaJugada = int(99) #Le pongo 99 porque para cumplir la condicion tiene que ser 0, 1 o 2
        print('\n================================')
        print("\nMano",turno)
        print("\nJugador 1 tiene:",mano_jugador1)
        print("\nComienza jugando:", ganadorUltimaRonda)
        if(ganadorUltimaRonda == 'Jugador 2'):
            #Si el Jugador 2 gana la ultima ronda, comienza jugando, aca se ve si canta y que canta, si canta se pone la variable pivot "cantoMaquina" en True y "cantoJugador" en False
            if(cantoMaquina == False):
                cantaMaq = maquinaDecideSiCantar(turno, juego, False)
                if(cantaMaq != 'no'):
                    juego = cantaMaq
                    print('Jugador 2 canta:', cantaMaq)
                    cantoMaquina = True
                    cantoJugador = False
                else:
                    print("Jugador 2 juega:",mano_jugador2[0])
        #Pregunta si quiere cantar truco o envido, en el principio de cada manos
        if(cantoMaquina == False): # Si cantoMaquina = False, entonces nadie canto, o canto Jugador 1
            if(juego == '' or juego == 'no' and turno == 1):
                juego = ''
                while(juego != 'truco' and juego != 'no'):
                    if(juego != 'envido' and juego != 'real envido' and juego != 'falta envido' and turno == 1 and envidoNoQuerido == False):
                        #Este if es la posibilidad de no haber cantado ni truco ni envido anteriormente y es el 1er turno
                        juego = input('Cantas truco, envido, real envido o falta envido? (escribí "truco", "envido", "real envido", "falta envido" o "no"): ')
                    else:
                        #Aca llega si se canto envido anteriormente y no se quiso, o es el turno 2 y no se canto anteriormente truco
                        juego = input('Cantas truco? (Escribí "truco" o "no"):')
                    if(juego != 'truco' and juego != 'envido' and juego != 'real envido' and juego != 'falta envido' and juego != 'no'):
                        #validacion para que se ingrese lo indicado
                        print('Lo que ingresaste no es valido, intenta de nuevo')
                    elif(juego == 'truco' or juego == 'envido' or juego == 'real envido' or juego == 'falta envido'):
                        #Como cantoMaquina = False, aca la maquina decide si acepta o no el juego cantado
                        confirmacion = maquinaDecideSiCantar(turno, juego, True)
                        if(confirmacion == 'no'):
                        #Si entra aca es que el Jugador 2 no quiso el juego cantado
                            print('Jugador 2 no quiso')
                            if(juego != 'envido' and juego != 'real envido' and juego != 'falta envido'):
                                resultado = calcular_puntos(juego, False, puntosjugador1, puntosjugador2, 'Jugador 1')
                                puntosjugador1 = resultado[0]
                                puntosjugador2 = resultado[1]
                                return [puntosjugador1, puntosjugador2]                               
                            else: 
                                envidoNoQuerido = True
                                resultado = calcular_puntos(juego, False, puntosjugador1, puntosjugador2, 'Jugador 1')
                                puntosjugador1 = resultado[0]
                                puntosjugador2 = resultado[1]
                        elif (juego == 'envido' or juego == 'real envido' or juego == 'falta envido'):
                        #Si entra aca, significa que el Jugador 2 si quiso y el juego cantado fue envido
                            print(juego, 'querido')
                            tantoJugador1 = calcular_tanto(mano_jugador1)
                            tantoJugador2 = calcular_tanto(mano_jugador2)
                            if tantoJugador1 > tantoJugador2:
                                #Jugador 1 gana envido
                                resultado = calcular_puntos(juego, True, puntosjugador1, puntosjugador2, 'Jugador 1')
                                print('Ganaste el envido: tenías '+str(tantoJugador1)+' y el Jugador 2 tenía '+str(tantoJugador2))
                                print('\nPuntos totales después del envido: \nJugador 1: ', resultado[0], '\nJugador 2: ', resultado[1])
                                puntosjugador1 = resultado[0]
                                puntosjugador2 = resultado[1]
                                if(juego == 'falta envido'):
                                    print('\nPartido finalizado, lo ganó el Jugador 1.')
                                    return [puntosjugador1, puntosjugador2]
                            elif tantoJugador2 > tantoJugador1:
                                #Jugador 2 gana envido
                                resultado = calcular_puntos(juego, True, puntosjugador1, puntosjugador2, 'Jugador 2')
                                puntosjugador1 = resultado[0]
                                puntosjugador2 = resultado[1]
                                print('Perdiste el envido: el Jugador 2 tenía '+str(tantoJugador2)+' y tenías '+str(tantoJugador1))
                                if(juego == 'falta envido'):
                                    print('\nPartido finalizado, lo ganó el Jugador 2.')
                                    return [puntosjugador1, puntosjugador2]
                            else:
                                #Empate envido
                                print('\nJugador 1: ', tantoJugador1)
                                print('\nJugador 2: ', tantoJugador2)
                                print('No hay puntos para nadie, es demasiada lógica calcular quién gana por mano.')
                        else:
                            #aca entra si se quiso un juego que no sea envido, real envido o falta envido
                            print('\nJugador 2 quiso.')
                            cantoJugador = True
                            cantoMaquina = False

            elif(juego == '' or juego == 'no' and turno > 1): #este if es a partir del 2do turno y si no se canto truco
                juego = ''
                while(juego != 'truco' and juego != 'no'):
                    juego = input('Cantas truco? (escribí "truco" o "no"): ') #se agarra el input
                    if(juego != 'truco' and juego != 'no'): # validacion para entradas no validas
                        print('Lo que ingresaste no es valido, intenta de nuevo')
                    elif(juego == 'truco'): #si lo ingresado en el input es truco, Jugador 2 decide si aceptar o no
                        confirmacion = maquinaDecideSiCantar(turno, juego, True)
                        if(confirmacion == 'no'):
                            print('Jugador 2 no quiso')
                            resultado = calcular_puntos(juego, False, puntosjugador1, puntosjugador2, 'Jugador 1')
                            puntosjugador1 = resultado[0]
                            puntosjugador2 = resultado[1]
                            return [puntosjugador1, puntosjugador2]
                        else:
                            print('Jugador 2 quiso')
                            cantoJugador = True
                            cantoMaquina = False
            elif(juego == 'truco' and cantoJugador == False):
                #si esta cantado truco por jugador 2, ya que cantoJugador esta en false, se pregunta si se quiere cantar retruco
                confirmacion = ''
                while(confirmacion != 'si' and confirmacion != 'no'):
                    confirmacion = input('Queres cantar retruco? (por "si" o por "no"): ')
                    if(confirmacion != 'si' and confirmacion != 'no'):
                        print('Lo que ingresaste no es valido, intenta de nuevo')
                    elif(confirmacion == 'si'): #si se quiere retruco, se pregunta a jugador 2
                        juego = 'retruco'
                        confirmacion = maquinaDecideSiCantar(turno, juego, True)
                        if(confirmacion == 'no'):
                            print('Jugador 2 no quiso')
                            resultado = calcular_puntos(juego, False, puntosjugador1, puntosjugador2, 'Jugador 1')
                            puntosjugador1 = resultado[0]
                            puntosjugador2 = resultado[1]
                            return [puntosjugador1, puntosjugador2]
                        else:
                            print('Jugador 2 quiso')
                            cantoJugador = True
                            cantoMaquina = False
            elif(juego == 'retruco' and cantoJugador == False):
                #si esta cantado retruco por jugador 2, ya que cantoJugador esta en false, se pregunta si se quiere cantar vale cuatro
                confirmacion = ''
                while(confirmacion != 'si' and confirmacion != 'no'):
                    confirmacion = input('Queres cantar vale cuatro? (por "si" o por "no"): ')
                    if(confirmacion != 'si' and confirmacion != 'no'):
                        print('Lo que ingresaste no es valido, intenta de nuevo')
                    elif(confirmacion == 'si'): #si se quiere vale cuatro, se pregunta a jugador 2
                        juego = 'vale cuatro'
                        confirmacion = maquinaDecideSiCantar(turno, juego, True)
                        if(confirmacion == 'no'):
                            print('Jugador 2 no quiso')
                            resultado = calcular_puntos(juego, False, puntosjugador1, puntosjugador2, 'Jugador 1')
                            puntosjugador1 = resultado[0]
                            puntosjugador2 = resultado[1]
                            return [puntosjugador1, puntosjugador2]
                        else:
                            print('Jugador 2 quiso')
                            cantoJugador = True
                            cantoMaquina = False
        else:
            #si cantoMaquina = True, entonces se le pregunta al jugador 1 si quiere lo que canto jugador 2
            confirmacion = ''
            while(confirmacion != 'si' and confirmacion != 'no'):
                confirmacion = input('Aceptas lo que cantó Jugador 2? (por "si" o por "no"): ')
                if(confirmacion != 'si' and confirmacion != 'no'):
                    print('Lo que ingresaste no es valido, intenta de nuevo')
                elif(confirmacion == 'no'):
                    resultado = calcular_puntos(juego, False, puntosjugador1, puntosjugador2, 'Jugador 2')
                    puntosjugador1 = resultado[0]
                    puntosjugador2 = resultado[1]
                    return [puntosjugador1, puntosjugador2]
                elif(confirmacion == 'si'):
                    print('se juega', juego)
                    print("Jugador 2 juega:",mano_jugador2[0])
                    cantoMaquina = False
        # Pide al jugador que ingrese el numero de la posicion de la carta, se juega lo que la variable juego dice
        while(cartaJugada == '' or cartaJugada > len(mano_jugador1)-1 or cartaJugada <= -1):
            cartaJugada = int(input('ingresa cual es la posicion de la carta que queres jugar (tenes '+str(len(mano_jugador1))+' cartas): ')) - 1
            if(cartaJugada > len(mano_jugador1)-1 or cartaJugada <= -1):
                print('posicion no valida')
        
        #Se agarran las cartas jugadas y se usa la funcion para determinar ganador
        ganador = determinar_ganador(mano_jugador1[cartaJugada], mano_jugador2[0])
        print("Jugador 1 juega:",mano_jugador1[cartaJugada])
        if(ganadorUltimaRonda == 'Jugador 1'):
            print("Jugador 2 juega:",mano_jugador2[0])
        
        #Se sacan de la mano las cartas jugadas
        mano_jugador1.remove(mano_jugador1[cartaJugada])
        mano_jugador2.remove(mano_jugador2[0])
        print("El ganador de la ronda es:",ganador)
        if(ganador == 'Jugador 1'):
            rondasGanadasJugador1 = rondasGanadasJugador1 + 1
        elif(ganador == 'Jugador 2'):
            rondasGanadasJugador2 = rondasGanadasJugador2 + 1
        print('rondas ganadas jugador 1:', rondasGanadasJugador1)
        print('rondas ganadas jugador 2:', rondasGanadasJugador2)
        turno = turno + 1
        if(ganador != 'Empate'):
            ganadorUltimaRonda = ganador

    if(rondasGanadasJugador1 > rondasGanadasJugador2):
        resultado = calcular_puntos(juego, True, puntosjugador1, puntosjugador2, 'Jugador 1')
        puntosjugador1 = resultado[0]
        puntosjugador2 = resultado[1]
    elif(rondasGanadasJugador1 < rondasGanadasJugador2):
        resultado = calcular_puntos(juego, True, puntosjugador1, puntosjugador2, 'Jugador 2')
        puntosjugador1 = resultado[0]
        puntosjugador2 = resultado[1]
    else:
        print('Empate, no se suman puntos')
        
    return [puntosjugador1, puntosjugador2]

# Ejecutar el juego
puntosJuego = 0
while(puntosJuego != 30 and puntosJuego != 15 and puntosJuego != 50):
    puntosJuego = int(input('\nIndica a cuantos puntos va a ser el truco ("15", "30" o "50"): '))
    if(puntosJuego != 30 and puntosJuego != 15 and puntosJuego != 50):
        print('No es valido lo que ingresaste, intenta de nuevo')

puntosjugador1 = 0
puntosjugador2 = 0
# Creamos el mazo de cartas
mazo = crear_mazo()
while(puntosjugador1 < puntosJuego and puntosjugador2 < puntosJuego):
    resultado = jugar_truco(puntosjugador1, puntosjugador2, mazo)
    puntosjugador1 = resultado[0]
    puntosjugador2 = resultado[1]
    print('\n================================\n')
    print('Puntos de Jugador 1:', puntosjugador1)
    print('Puntos de Jugador 2:', puntosjugador2)

#si los dos pasan el puntaje a alcanzar, gana el que tenga mas puntos
if(puntosjugador1 >= puntosJuego and puntosjugador2 >= puntosJuego):
    if(puntosjugador1 > puntosjugador2):
        print('Ganador: Jugador 1')
    else:
        print('Ganador: Jugador 2')
elif(puntosjugador1 >= puntosJuego):
    print('Ganador: Jugador 1')
else:
    print('Ganador: Jugador 2')
print('\nCopyright (r) LVA - La Vagancia Avanza - 2024. Todos los derechos reservados.\nTrucardoLVA')
print('\nCréditos: \nProduct Owner: Georges David  \nProject Manager: Iván Díaz \nContent Creator: Felipe Iván Figueredo Alarcón\nCommunity Manager: Luca Ravello Benito\nGod: Lionel Andrés Messi Cuccitinni\n---------------------\nTech Adviser: Franco Martorella - Grupo 3\nLawyer - Just In Case: Luciano Conde - Grupo 3\n')
aprobamos = input('\nPor si o por no, aprobamos?:\n')

while(aprobamos != 'si' and aprobamos != 'Si' and aprobamos != "SI" and aprobamos != "sI"):
    aprobamos = input('\nDaaaaale, nos aprobás?:\n')

print('\nGracias! Nos vemos en progra I ;)\n')
print('\nprint(break)\n')