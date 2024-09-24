import random
from utilities.calcularTanto import calcular_tanto as calcular_tanto
from utilities.calcularPuntos import calcular_puntos as calcular_puntos
from utilities.determinarGanador import determinar_ganador as determinar_ganador
from utilities.repartirCartas import repartir_cartas as repartir_cartas
from utilities.crearMazo import crear_mazo as crear_mazo
from utilities.maquinaChoice import maquinaDecideSiCantar as maquinaDecideSiCantar
from data.constantes import JERARQUIA

# Función para jugar un truco
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
                        juego = input('Cantas truco, envido, real envido o falta envido? (escribí "truco", "envido", "real envido", "falta envido" o "no"): ').lower()
                    else:
                        #Aca llega si se canto envido anteriormente y no se quiso, o es el turno 2 y no se canto anteriormente truco
                        juego = input('Cantas truco? (Escribí "truco" o "no"):').lower().strip()
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
                    juego = input('Cantas truco? (escribí "truco" o "no"): ').lower().strip() #se agarra el input
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
                    confirmacion = input('Queres cantar retruco? (por "si" o por "no"): ').lower().strip()
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
                    confirmacion = input('Queres cantar vale cuatro? (por "si" o por "no"): ').lower().strip()
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
                confirmacion = input('Aceptas lo que cantó Jugador 2? (por "si" o por "no"): ').lower().strip()
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