import random

vidasOponente = 3
vidasJugador = 3
turnoOponente = True
armas = "Piedra","Papel","Tijeras"

def LoopPrincipal():
    global manoOponente
    global manoJugador
    manoJugador = 0
    while vidasJugador > 0 and vidasOponente > 0:
        MenuSeleccionMano()
        if turnoOponente == True:
            manoOponente = random.randint(0,2)
            Enfrentamiento()
    FinalJuego()

def MenuSeleccionMano():
    print(f"Vidas: {vidasJugador}   Vidas Oponente: {vidasOponente}")
    print("         Que elijes?\n1.Piedra  |  2.Papel  |  3.Tijeras")
    manoJugador = int(input())

def Enfrentamiento():
    if manoJugador - 1 == manoOponente:
        print(f"\nHa sido un empate\nEl oponente también sacó: {armas[manoOponente]}")
    elif manoJugador - 1 == 0 and manoOponente == 2 or manoJugador - 1 == 2 and manoOponente == 1 or manoJugador - 1 == 1 and manoOponente == 0:
        print(f"\nGanaste la ronda!\nEl oponente sacó: {armas[manoOponente]}")
        vidasOponente = vidasOponente - 1
    elif manoJugador - 1 == 0 and manoOponente == 1 or manoJugador - 1 == 1 and manoOponente == 2 or manoJugador - 1 == 2 and manoOponente == 0:
        print(f"\nPerdiste la ronda!\nEl oponente sacó: {armas[manoOponente]}")
        vidasJugador = vidasJugador - 1

def FinalJuego():
    if vidasJugador > 0:
        print("Ganaste la partida!\n\nRepetir? Y / N")
    else:
        print("Perdiste la partida!\n\nRepetir? Y / N")
    opcion = input().upper()
    if opcion == "Y":
        LoopPrincipal()
    
LoopPrincipal()
