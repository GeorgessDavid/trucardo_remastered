from game_logic import jugar_truco as jugar_truco
from utilities.crearMazo import crear_mazo as crear_mazo

# Ejecutar el juego
puntosJuego = 0
while(puntosJuego != 30 and puntosJuego != 15 and puntosJuego != 50):
    puntosJuego = input('\nIndica a cuantos puntos va a ser el truco ("15", "30" o "50"): ')
    if(puntosJuego != "30" and puntosJuego != "15" and puntosJuego != "50"):
        print('No es valido lo que ingresaste, intenta de nuevo')
    else:
        puntosJuego=int(puntosJuego)
    
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