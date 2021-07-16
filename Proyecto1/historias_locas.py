#concatenar cadenas de caracteres.
# Supongamos que queremos crear una cadena que diga:
# Aprende a programar con _________.

#organizacion = "freeCodeCamp"

#print("aprende a programar con " + organizacion)
#print("Aprende a programar con {}".format(organizacion))
#print(f"Aprende a programar con {organizacion}")
adj = input("Adjetivo: ")
verbo1 = input("Verbo: ")
verbo2 = input("Verbo: ")
sustantivo_plural = input("sustantivo(plural): ")

madlib = f"Programar es tan {adj}!, Siempre me emociona por que me encanta {verbo1} problemas. Aprende a {verbo2} con freeCodeCamp y alcanza tus {sustantivo_plural}!"

print(madlib)
