import random


def jugar():
    usuario = input("Elige una opción: 'pi' para piedra, 'pa' para papel y 'ti' para tijera.\n").lower()
    ordenador = random.choice(['pi', 'pa', 'ti'])

    if usuario == ordenador: 
        return "¡Empate!"
    
    if gana_el_jugador(usuario, ordenador):
        return "¡Has ganado :) !"
    
    return "¡Has perdido :( !"


def gana_el_jugador(jugador, oponente):
    # Devuelve True si gana el jugador
    # Si piedra gana a tijera (pi>ti)
    # Si tijera gana a papel (ti>pa)
    # Si pape gana a piedra (pa>pi)
    if ((jugador == 'pi' and oponente == 'ti')
        or (jugador == 'ti' and oponente == 'pa')
        or (jugador == 'pa' and oponente == 'pi' )):
        return True
    else:
        return False
    

print(jugar())