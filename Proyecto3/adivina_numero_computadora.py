import random


def adivina_el_numero_computadora(x):

    print("===============================")
    print("    Bienvenido(a) al Juego!    ")
    print("===============================")
    print(f"Selecciona un nuemero entre 1 y {x} para que la computadore intente adivinarlo... ")

    limite_inferior = 1
    limite_superior = x
    respuesta = ""

    while respuesta != "c":
        #gerenar
        if limite_inferior != limite_superior:
            prediccion = random.randint(limite_inferior, limite_superior)
        else:
            prediccion = limite_superior

        #obtener respuesta
        respuesta = input(f"""
                Mi predccion es {prediccion}.

                Si es muy alta ingresa(A).
                Si es muy baja ingresa (B).
                Si es correcta ingresa (C).
                ingrese respuesta: """).lower()

        if respuesta == "a":
            limite_superior = prediccion - 1
        elif respuesta == "b":
            limite_inferior = prediccion + 1
    print(f"SIII la computadore adivino corectamente: {prediccion}")


adivina_el_numero_computadora(10)
