import random


def adivina_el_numero(x):
    print("================================")
    print("    !Bienvenido(a)al juego      ")
    print("================================")
    print("Tu meta es adivinar le numero generado por la computaodra.")

    numero_aleatorio = random.randint(1, x)
    prediccion = 0

    while prediccion != numero_aleatorio:
        #ingresa un nuemero 
        prediccion = int(input(f"Adivina un numero entre 1 y {x}: "))

        if prediccion  < numero_aleatorio:
            print("Intenta otra vez. esta numero ess muy pequeño. ")
        elif prediccion > numero_aleatorio:
            print("Intenta otra vez. este numero es muy grande.   ")

    print(f"!felicitaciones! Adivinaste el numero {numero_aleatorio} correctamente.  ")


adivina_el_numero(10)
