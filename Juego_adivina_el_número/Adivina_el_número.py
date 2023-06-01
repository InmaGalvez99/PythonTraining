import random 

def adivinia_el_número(x):

    print("=========================")
    print(" ¡Bienvenido/a al juego! ")
    print("=========================")

    nombre = input("¿Cómo te llamas?: ").capitalize()
    vidas = 5
    print(f"{nombre}, tu objetivo es adivinar el número entre 1 y 30.\nTienes {vidas} intentos.\n¿Ready?")

    número_aleatorio = random.randint(1,x) # número aleatorio entre 1 y x

    número = 0

    while número != número_aleatorio and vidas > 0:
        número = int(input(f"Adivina el número entre 1 y {x}: "))

        # Si el jugador ingresa un número fuera del rango
        if número not in range(1,x+1):
            print(f"{nombre}, ese número no se encuentra dentro del rango 1 a 30")

        # Distintos escenarios según el jugador ingrese un número mayor o menor del que es el correcto.
        # A la vez se quitan intentos
        elif número < número_aleatorio:
            vidas = vidas - 1
            print(f"Este número es muy pequeño. Inténtalo de nuevo. Te quedan {vidas} intentos.")
        elif número > número_aleatorio:
            vidas = vidas - 1
            print(f"Este número es muy grande. Inténtalo de nuevo. Te quedan {vidas} intentos.")


    # Si el jugador agota los 5 intentos
    if vidas == 0:
        print(f"¡Vaya! Has agotado los intentos {nombre}")
        print(f"El número era {número_aleatorio}")
        # Preguntar al jugador si quiere volver a jugar e intentar ganar
        jugar = input("¿Quieres volver a jugar? Si o no: ").capitalize()
        respuesta = "Si"
        if jugar == respuesta:
            adivinia_el_número(30)
        else:
            print(f"¡Gracias por jugar {nombre}!\n¡Hasta pronto!") 

    else:
        print(f"¡ENHORABUENA {nombre}! Has adivinado el número {número_aleatorio}")

adivinia_el_número(30)