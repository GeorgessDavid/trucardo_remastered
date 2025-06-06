# import random
import time
from utilities.calcularTanto import calcular_tanto
from utilities.calcularPuntos import calcular_puntos
from utilities.determinarGanador import determinar_ganador
from utilities.repartirCartas import repartir_cartas
from utilities.crearMazo import crear_mazo
from utilities.maquinaChoice import maquinaDecideSiCantar
# from src.constantes import JERARQUIA
from src.helper.colorLog import color as colorLog
# from src.helper.printError import printError as err
from src.helper.selectorMenu import selectorMenu
from src.controllers.log.save import save


# Función para jugar un truco
def jugar_truco(playerName: str, puntosjugador1: int, puntosjugador2: int, mazo: list, path: str, mano: int):
    '''
    Función que simula el juego del truco entre dos jugadores, el jugador  y la CPU.
    '''
    if(len(mazo) <= 10):
        mazo = crear_mazo()
    cartas = repartir_cartas(mazo)
    mano_jugador1 = cartas[0]
    mano_jugador2 = cartas[1]
    juego = ''
    turno = 1
    ganadorUltimaRonda = playerName #Default Jugador
    rondasGanadasJugador1 = 0
    rondasGanadasJugador2 = 0
    cantoMaquina = False
    cantoJugador = False
    envidoNoQuerido = False
    manosChicas = ('Primera', 'Segunda', 'Tercera')    
    
    while(turno < 4 and rondasGanadasJugador1 < 2 and rondasGanadasJugador2 < 2):
        
        print(colorLog(1, 37, 40, '\nCargando...'))
        time.sleep(0.5)
        
        if(len(mazo) <= 10):
            mazo = crear_mazo()
        
        confirmacion = ''
        cartaJugada = int(99) #Le pongo 99 porque para cumplir la condicion tiene que ser 0, 1 o 2
        print('\n================================')
        
        time.sleep(1)
        
        print(colorLog(1, 35, 40,f"\n{manosChicas[turno-1]}"))
        print(f"\n{colorLog(1,34,40, playerName)} tiene: {mano_jugador1}")
        print("\nComienza jugando:", ganadorUltimaRonda)
        
        if(ganadorUltimaRonda == 'La CPU'):
            #Si el La CPU gana la ultima ronda, comienza jugando, aca se ve si canta y que canta, si canta se pone la variable pivot "cantoMaquina" en True y "cantoJugador" en False
        
            if(cantoMaquina == False):
                cantaMaq = maquinaDecideSiCantar(turno, juego, False, mano_jugador2)
        
                if(cantaMaq != 'no'):
                    juego = cantaMaq
                    print('La CPU canta:', cantaMaq)
                    cantoMaquina = True
                    cantoJugador = False
        
                else:
                    print("La CPU juega:",mano_jugador2[0])
        
        #Pregunta si quiere cantar truco o envido, en el principio de cada manos
        if(cantoMaquina == False): # Si cantoMaquina = False, entonces nadie canto, o canto Jugador 1
        
            if(juego == '' or juego == 'no' and turno == 1):
                juego = ''
        
                while(juego != 'truco' and juego != 'no'):
        
                    if(juego != 'envido' and juego != 'real envido' and juego != 'falta envido' and turno == 1 and envidoNoQuerido == False):
                        #Este if es la posibilidad de no haber cantado ni truco ni envido anteriormente y es el 1er turno
                        juego = selectorMenu(['Truco', 'Envido', 'Real Envido', 'Falta Envido', 'No'], colorLog(1, 33, 40, 'Querés cantar algo?:'), 'value').lower()                         
        
                    else:
                        #Aca llega si se canto envido anteriormente y no se quiso, o es el turno 2 y no se canto anteriormente truco
                        juego = selectorMenu(['Truco', 'No'], colorLog(1, 33, 40, 'Querés cantar algo?:'), 'value').lower()
                    
                    if(juego == 'truco' or juego == 'envido' or juego == 'real envido' or juego == 'falta envido'):
                        #Como cantoMaquina = False, aca la maquina decide si acepta o no el juego cantado
                        confirmacion = maquinaDecideSiCantar(turno, juego, True, mano_jugador2)
        
                        if(confirmacion == 'no'):
                        #Si entra aca es que el La CPU no quiso el juego cantado
                            print('La CPU no quiso')
        
                            if(juego != 'envido' and juego != 'real envido' and juego != 'falta envido'):
                                resultado = calcular_puntos(playerName, juego, False, puntosjugador1, puntosjugador2, playerName)
                                puntosjugador1 = resultado[0]
                                puntosjugador2 = resultado[1]
                                return [puntosjugador1, puntosjugador2]                               
        
                            else: 
                                envidoNoQuerido = True
                                resultado = calcular_puntos(playerName, juego, False, puntosjugador1, puntosjugador2, playerName)
                                puntosjugador1 = resultado[0]
                                puntosjugador2 = resultado[1]
        
                        elif (juego == 'envido' or juego == 'real envido' or juego == 'falta envido'):
                        #Si entra aca, significa que el La CPU si quiso y el juego cantado fue envido
        
                            print(juego, 'querido')
                            tantoJugador1 = calcular_tanto(mano_jugador1)
                            tantoJugador2 = calcular_tanto(mano_jugador2)
        
                            if tantoJugador1 > tantoJugador2:
                                #Jugador 1 gana envido
                                resultado = calcular_puntos(playerName, juego, True, puntosjugador1, puntosjugador2, playerName)
                                print('Ganaste el envido: tenías '+str(tantoJugador1)+' y la CPU tenía '+str(tantoJugador2))
                                print(f'\nPuntos totales después del envido: \n{colorLog(1,34,40, playerName)}: ', resultado[0], '\nLa CPU: ', resultado[1])
                                puntosjugador1 = resultado[0]
                                puntosjugador2 = resultado[1]
        
                                if(juego == 'falta envido'):
                                    print(f'\nPartido finalizado, lo ganó {colorLog(1,34,40, playerName)}.')
                                    return [puntosjugador1, puntosjugador2]
        
                            elif tantoJugador2 > tantoJugador1:
                                #La CPU gana envido
                                resultado = calcular_puntos(playerName, juego, True, puntosjugador1, puntosjugador2, 'La CPU')
                                puntosjugador1 = resultado[0]
                                puntosjugador2 = resultado[1]
                                print('Perdiste el envido: la CPU tenía '+str(tantoJugador2)+' y tenías '+str(tantoJugador1))
        
                                if(juego == 'falta envido'):
                                    print('\nPartido finalizado, lo ganó La CPU.')
                                    return [puntosjugador1, puntosjugador2]
        
                            else:
                                #Empate envido
                                print(f'\n{playerName}: ', tantoJugador1)
                                print('\nLa CPU: ', tantoJugador2)
        
                                if ganadorUltimaRonda == playerName:
                                    resultado = calcular_puntos(playerName, juego, True, puntosjugador1, puntosjugador2, playerName)
                                    puntosjugador1 = resultado[0]
                                    puntosjugador2 = resultado[1]
                                    print('\nGanaste el envido por ser mano.')
        
                                else:
                                    resultado = calcular_puntos(playerName, juego, True, puntosjugador1, puntosjugador2, 'La CPU')
                                    puntosjugador1 = resultado[0]
                                    puntosjugador2 = resultado[1]
                                    print('\nLa CPU ganó el envido por ser mano.')
        
                        else:
                            #aca entra si se quiso un juego que no sea envido, real envido o falta envido
                            print('\nLa CPU quiso.')
                            cantoJugador = True
                            cantoMaquina = False

            elif(juego == '' or juego == 'no' and turno > 1): #este if es a partir del 2do turno y si no se canto truco
                juego = ''
                while(juego != 'truco' and juego != 'no'):
                    
                    juego = selectorMenu(['Truco', 'No'], colorLog(1, 33, 40, 'Querés cantar algo?:'), 'value').lower()
                    
                    if(juego == 'truco'): #si lo ingresado en el input es truco, La CPU decide si aceptar o no
                        
                        confirmacion = maquinaDecideSiCantar(turno, juego, True, mano_jugador2)
                        
                        if(confirmacion == 'no'):
                            print('La CPU no quiso')
                            resultado = calcular_puntos(playerName, juego, False, puntosjugador1, puntosjugador2, playerName)
                            puntosjugador1 = resultado[0]
                            puntosjugador2 = resultado[1]
                            return [puntosjugador1, puntosjugador2]
                        
                        else:
                            print('La CPU quiso')
                            cantoJugador = True
                            cantoMaquina = False
                            
            elif(juego == 'truco' and cantoJugador == False):
    
                #si esta cantado truco por La CPU, ya que cantoJugador esta en false, se pregunta si se quiere cantar retruco
                confirmacion = ''
                
                while(confirmacion != 'si' and confirmacion != 'no'):
                    
                    confirmacion = selectorMenu(['Si', 'No'],colorLog(1, 33, 40, 'Querés cantar retruco?'), 'value').lower()
                    
                    if(confirmacion == 'si'): #si se quiere retruco, se pregunta a La CPU
                        
                        juego = 'retruco'
                        confirmacion = maquinaDecideSiCantar(turno, juego, True, mano_jugador2)
                        
                        if(confirmacion == 'no'):
                            print('La CPU no quiso')
                            resultado = calcular_puntos(playerName, juego, False, puntosjugador1, puntosjugador2, playerName)
                            puntosjugador1 = resultado[0]
                            puntosjugador2 = resultado[1]
                            return [puntosjugador1, puntosjugador2]
                        
                        else:
                            print('La CPU quiso')
                            cantoJugador = True
                            cantoMaquina = False
                            
            elif(juego == 'retruco' and cantoJugador == False):
                #si esta cantado retruco por La CPU, ya que cantoJugador esta en false, se pregunta si se quiere cantar vale cuatro
                confirmacion = ''
                
                while(confirmacion != 'si' and confirmacion != 'no'):
                    # confirmacion = input('Queres cantar vale cuatro? (por "si" o por "no"): ').lower().strip()
                    confirmacion = selectorMenu(['Si', 'No'], colorLog(1, 33, 40, 'Querés cantar vale cuatro?'), 'value').lower()
                

                    if(confirmacion == 'si'): #si se quiere vale cuatro, se pregunta a La CPU
                        
                        juego = 'vale cuatro'
                        confirmacion = maquinaDecideSiCantar(turno, juego, True, mano_jugador2)
                        
                        if(confirmacion == 'no'):
                            print('La CPU no quiso')
                            resultado = calcular_puntos(playerName, juego, False, puntosjugador1, puntosjugador2, playerName)
                            puntosjugador1 = resultado[0]
                            puntosjugador2 = resultado[1]
                            return [puntosjugador1, puntosjugador2]
                        
                        else:
                            print('La CPU quiso')
                            cantoJugador = True
                            cantoMaquina = False
                            
        else:
            #si cantoMaquina = True, entonces se le pregunta al jugador 1 si quiere lo que canto La CPU
            confirmacion = ''
            while(confirmacion != 'si' and confirmacion != 'no'):
                confirmacion = selectorMenu(['Si', 'No'], colorLog(1, 33, 40, 'Aceptas lo que cantó La CPU?'), 'value').lower()

                if(confirmacion == 'no'):
                    resultado = calcular_puntos(playerName, juego, False, puntosjugador1, puntosjugador2, 'La CPU')
                    puntosjugador1 = resultado[0]
                    puntosjugador2 = resultado[1]
                    return [puntosjugador1, puntosjugador2]
                
                elif(confirmacion == 'si'):
                    print('se juega', juego)
                    print("La CPU juega: ",mano_jugador2[0])
                    cantoMaquina = False
                    
        # Pide al jugador que ingrese el numero de la posicion de la carta, se juega lo que la variable juego dice
        while(cartaJugada == '' or cartaJugada > len(mano_jugador1)-1 or cartaJugada <= -1):
            
            cartaJugada = selectorMenu(mano_jugador1, colorLog(1, 33, 40, 'Selecciona la carta que querés jugar') , 'index')
            save(path, 'playedCards.txt', f'Mano de {playerName}: {mano_jugador1}\nCarta jugada: {mano_jugador1[cartaJugada]}\n\n')
        
        #Se agarran las cartas jugadas y se usa la funcion para determinar ganador
        ganador = determinar_ganador(playerName, mano_jugador1[cartaJugada], mano_jugador2[0])
        print(f"{colorLog(1,34,40, playerName)} juega:",mano_jugador1[cartaJugada])
        
        if(ganadorUltimaRonda == playerName):
            print("La CPU juega: ", mano_jugador2[0])
        
        #Se sacan de la mano las cartas jugadas
        mano_jugador1.remove(mano_jugador1[cartaJugada])
        mano_jugador2.remove(mano_jugador2[0])
        print(f'El ganador de la {manosChicas[turno-1]} es {ganador}')
        
        if(ganador == playerName):
            rondasGanadasJugador1 = rondasGanadasJugador1 + 1
            
        elif(ganador == 'La CPU'):
            rondasGanadasJugador2 = rondasGanadasJugador2 + 1
        
        print(f'rondas ganadas por {colorLog(1,34,40, playerName)}: ', rondasGanadasJugador1)
        print('rondas ganadas por la CPU: ', rondasGanadasJugador2)

        
        
        turno = turno + 1
        if(ganador != 'Empate'):
            ganadorUltimaRonda = ganador

    if(rondasGanadasJugador1 > rondasGanadasJugador2):
        save(path, 'manoLogs.txt', f'\nMano {mano} ganada por {playerName}\n\tManos chicas ganadas: {rondasGanadasJugador1}\n')
        resultado = calcular_puntos(playerName, juego, True, puntosjugador1, puntosjugador2, playerName)
        puntosjugador1 = resultado[0]
        puntosjugador2 = resultado[1]
    
    elif(rondasGanadasJugador1 < rondasGanadasJugador2):
        save(path, 'manoLogs.txt', f'\nMano {mano} ganada por la CPU\n\tManos chicas ganadas: {rondasGanadasJugador1}\n')
        resultado = calcular_puntos(playerName, juego, True, puntosjugador1, puntosjugador2, 'La CPU')
        puntosjugador1 = resultado[0]
        puntosjugador2 = resultado[1]
    
    else:
        print('Empate, no se suman puntos')
        
    return [puntosjugador1, puntosjugador2]

def ejecutar_truco(name: str, path: str):
    # Ejecutar el juego
    puntosJuego = 0
    while(puntosJuego != 30 and puntosJuego != 15):
        
        puntosJuego = selectorMenu([15, 30], colorLog(1, 37, 40, 'Selecciona a cuántos puntos va a ser el truco.'), 'value')
        save(path, 'gameConfig.txt', f'Esta partida se jugó a {puntosJuego} puntos.')
        print(f'\nSe juega hasta {puntosJuego} puntos.')
        
    puntosjugador1 = 0
    puntosjugador2 = 0
    
    # Creamos el mazo de cartas
    mazo = crear_mazo()
    
    mano = 1
    while(puntosjugador1 < puntosJuego and puntosjugador2 < puntosJuego):
        resultado = jugar_truco(name, puntosjugador1, puntosjugador2, mazo, path, mano)
        puntosjugador1 = resultado[0]
        puntosjugador2 = resultado[1]
        time.sleep(0.5)
        print('\n================================\n')
        print(colorLog(1, 36, 40, f'\nMano {mano} finalizada'))
        print(f'Puntos de {colorLog(1,34,40, name)}: {puntosjugador1}')
        print('Puntos de La CPU:', puntosjugador2)
        mano+=1

    #si los dos pasan el puntaje a alcanzar, gana el que tenga mas puntos
    if(puntosjugador1 >= puntosJuego and puntosjugador2 >= puntosJuego):
    
        if(puntosjugador1 > puntosjugador2):
            print(f'Ganador: {colorLog(1,34,40, name)}')

        else:
            print('Ganador: La CPU')

    elif(puntosjugador1 >= puntosJuego):
        save(path, 'gameWinner.txt', f'Esta partida la ganó {name}.\n\n\t{name}: {puntosjugador1}\n\tCPU: {puntosjugador2}\n\nLa partida se jugaba a {puntosJuego}')
        print(f'Ganador: {colorLog(1,34,40, name)}')
    
    else:
        save(path, 'gameWinner.txt', f'Esta partida la ganó la CPU.\n\n\t{name}: {puntosjugador1}\n\tCPU: {puntosjugador2}\n\nLa partida se jugaba a {puntosJuego}')
        print('Ganador: La CPU')