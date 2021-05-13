def piedra_papel_tijera():
    print("Piedra, Papel o Tijeras")
    jugador1 = input("Jugador 1 elige entre Piedra, Papel o Tijeras: ")
    jugador1 = jugador1.lower()
    jugador1 = jugador1.strip()
    jugador1 = jugador1[:2:]
    jugador2 = input("Jugador 2 elige entre Piedra, Papel o Tijeras: ")
    jugador2 = jugador2.lower()
    jugador2 = jugador2.strip()
    jugador2 = jugador2[:2:]
    if jugador1 == jugador2:
        print("Empate")
    elif jugador1 == "pi" and jugador2 == "ti":
        print("gana el Jugador 1")
    elif jugador1 == "pi" and jugador2 == "pa":
        print("gana el Jugador 2")
    elif jugador1 == "pa" and jugador2 == "ti":
        print("gana el Jugador 2")
    elif jugador1 == "pa" and jugador2 == "pi":
        print("gana el Jugador 1")
    elif jugador1 == "ti" and jugador2 == "pi":
        print("gana el Jugador 2")
    elif jugador1 == "ti" and jugador2 == "pa":
        print("gana el Jugador 1")
    else:
        print("Los Jugadores no eligieron una opcion valida")

if __name__ == '__main__':
    piedra_papel_tijera()