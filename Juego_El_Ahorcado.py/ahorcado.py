import random
import string
from palabras import palabras
from diagramas import vidas_visual

def palabra_válida(lista_palabras):
    # Seleccionar una palabra al azar de la lista de palabras válidas
    palabra = random.choice(lista_palabras)
    while '_' in palabra or ' ' in palabra:
        palabra = random.choice(lista_palabras)
    return palabra.upper()


def ahorcado():
    print(" ¡Bienvenido(a) al juego del Ahorcado! ")
    palabra = palabra_válida(palabras)
    letras_por_adivinar = set(palabra)
    letras_adivinadas = set()
    abecedario = set(string.ascii_uppercase) #lista de todas las letras del abdecedario (menos Ñ) en mayúsucula
    vidas = 7

    while len(letras_por_adivinar) > 0 and vidas > 0:
        print(f"Te quedan {vidas} vidas y has usado estas letras: {' '.join(letras_adivinadas)} ")

        # Mostrar el estado actual de la palabra
        palabra_lista = [letra if letra in letras_adivinadas else '-' for letra in palabra]
        # Mostrar estado del ahorcado
        print(vidas_visual[vidas])
        # Mostrar las letras separadas por un espacio
        print(f"Palabra: {' '.join(palabra_lista)}")

        letra_usuario = input("Introduce una letra: ").upper()

        # Si la letra introducida por el usuario está en el abecedario y no está en el conjunto de 
        # letras ya adivinadas, se añade al conjunto de letras introducidas sea correcta o no pero ya fue introducida
        if letra_usuario in abecedario - letras_adivinadas:
            letras_adivinadas.add(letra_usuario)

            # Si la letra está en la palabra a adivinar, se quita la letra del conjunto de letras por adivinar;
            # sino, quitar una vida al usuario por la equivocación
            if letra_usuario in letras_por_adivinar:
                letras_por_adivinar.remove(letra_usuario)
                print(' ')
            else:
                vidas = vidas - 1
                print(f"\nTu letra, {letra_usuario} no está en la palabra.")

        # La letra del usuario ya ha sido introducida
        elif letra_usuario in letras_adivinadas:
            print("\nYa has introducido esa letra. Por favor, elige otra letra.")
        else:
            print("\nEsta letra no es válida")

    # Llegamos aquí cuando se adivinan todas las letras de la palabra o el jugador se queda sin vidas.
    if vidas == 0:
        print(vidas_visual[vidas])
        print(f"¡Ahorcado! Has perdido. La palabra era: {palabra}")
    else:
        print(f"¡Has adivinado la palabra {palabra}!")

ahorcado()