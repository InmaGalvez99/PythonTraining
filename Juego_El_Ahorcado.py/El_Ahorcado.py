import random
import string
from palabras import palabras

def palabra_válida(lista_palabras):
    # Seleccionar una palabra al azar de la lista de palabras válidas
    palabra = random.choice(lista_palabras)
    while '_' in palabra or ' ' in palabra:
        palabra = random.choice(lista_palabras)
    return palabra.upper()


def ahorcado():
    print(" !Bienvenido(a) al juego del Ahorcado! ")
    palabra = palabra_válida(palabras)
    letras_por_adivinar = set(palabra)
    letras_adivinadas = set()
    abecedario = set(string.ascii_uppercase) #lista de todas las letras del abdecedario (menos Ñ) en mayúsucula
    vidas = 7

    while len(letras_por_adivinar) > 0 and vidas > 0:
        print(f"Te quedan {vidas} vidas y has usado estas letras: {' '.join(letras_adivinadas)} ")

        # Mostrar el estado actual de la palabra
        palabra_lista = [letra if letra in letras_adivinadas else '-' for letra in palabra]
