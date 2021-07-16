import random
import string
from palabras import palabras
from ahorcado_diagramas import vidas_diccionario_visual


def obtener_palabra_valida(palabras):

    palabra = random.choice(palabras)

    while '-' in palabra or ' ' in palabra:
        palabra = random.choice(palabras)
    return  palabra.upper()


def ahorcado():

    print("======================================")
    print("=Bienvenida(a) al juego del ahoracado=")
    print("======================================")

    palabra = obtener_palabra_valida(palabras)

    letras_por_adivinar = set(palabra)
    letras_adivinadas   = set()
    abecedario          = set(string.ascii_uppercase)

    vidas = 7

    while len(letras_por_adivinar) > 0 and vidas > 0:
        print(f"te quedan {vidas} vidas y y has usado estas letras: {' '.join(letras_adivinadas)}")

        palabra_lista = [letra if letra in letras_adivinadas else '-' for letra in palabra ]
        print(vidas_diccionario_visual[vidas])
        print(f"Palabra: {' '.join(palabra_lista)}")

        letra_usuario = input("Escoge una letra: ").upper()

        if letra_usuario in abecedario - letras_adivinadas:
            letras_adivinadas.add(letra_usuario)

            if letra_usuario in letras_por_adivinar:
                letras_por_adivinar.remove(letra_usuario)
                print(' ')
            else:
                vidas = vidas - 1
                print(f"\n Tu letra no esta en la palabra. ")
        elif letra_usuario in letras_adivinadas:
            print("\nYa escogiste por favos escoge una  nueva. ")
        else:
            print(f"\nEsta letra no es valida. ")


    #cuando se adivina todo o se agota
    if vidas ==0:
        print(vidas_diccionario_visual[vidas])
        print(F"Ahorcado! Perdiste. La palabra era: {palabra}")
    else:
        print(f"Exelente adivinaste la palabra {palabra}!")


ahorcado()
