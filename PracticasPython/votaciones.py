def calculo():
    lista = []
    votos = int(input())
    
    for n in range(votos):
        votoString = str(input())
        votoString.capitalize()
        lista.append(votoString)

    listaSet = set(lista)
    lista2  = list(listaSet)
    contL=[0]*len(listaSet)
    for b in lista:
      candidatosVotos=b
      if candidatosVotos in lista2:
        pos=lista2.index(candidatosVotos)
        contL[pos]+=1
    contMax=max(contL)
    posCont=contL.index(contMax)
    ganador=lista2[posCont]
    print(ganador)

calculo()