import random

def jugar():
    usuario = input("""

Escoge una opcion:

Piedra'pi'.
Papel 'pa'.
Tijera'ti'.   ->""").lower()

    computadora = random.choice(['pi', 'pa', 'ti'])

    if usuario == computadora:
        return 'Empate!'
    if gano_el_jugador(usuario, computadora):
        return 'Ganaste!'
    return 'Perdiste!'


def gano_el_jugador(jugador,oponente):
    #restunar True si gana el playaer
    #Piedra gana Tijera
    #Tijera gana Papal
    #Papel gana Piedra
    if(    (jugador == 'pi' and oponente == 'ti')
        or (jugador == 'ti' and oponente == 'pa')
        or (jugador == 'pa' and oponente == 'pi')):
        return True
    else:
        return False



print(jugar())
