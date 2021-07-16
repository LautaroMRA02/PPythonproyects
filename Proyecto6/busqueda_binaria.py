import random
import time


def busqueda_ingenua(lista, objetivo):
    for i in range(len(lista)):
        if lista[i] == objetivo:
            return i
    return -1



def busqueda_binaria(lista, objetivo, limite_inferio=None, limite_superio=None):
    if limite_inferio is None:
        limite_inferio = 0
    if limite_superio is None:
        limite_superio = len(lista) - 1

    if limite_superio < limite_inferio:
        return -1

    punto_medio = (limite_inferio + limite_superio) // 2

    if lista[punto_medio] == objetivo:
        return punto_medio
    elif objetivo < lista[punto_medio]:
        return busqueda_binaria(lista, objetivo, limite_inferio, punto_medio - 1)
    else:
        return  busqueda_binaria(lista, objetivo, punto_medio + 1, limite_superio)

if __name__=='__main__':

    tamaño = 10000
    conjunto_inicial = set()

    while len(conjunto_inicial) < tamaño:
        conjunto_inicial.add(random.randint(-3*tamaño, 3*tamaño))


    lista_ordenada = sorted(list(conjunto_inicial))


    inicio = time.time()
    for objetivo in lista_ordenada:
        busqueda_ingenua(lista_ordenada, objetivo)
    fin = time.time()
    print(f"Tiempo de busqueda ingenua: {fin - inicio} segundos")


    inicio =  time.time()
    for objetivo in lista_ordenada:
        busqueda_binaria(lista_ordenada, objetivo)
    fin = time.time()
    print(f"Tiempo de busqueda ingenua: {fin - inicio} segundos")

