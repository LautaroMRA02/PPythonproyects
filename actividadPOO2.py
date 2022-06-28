# 1
# 1
# 1


class Vehiculo:
    def __init__(self,color,ruedas):
        self.color = color
        self.ruedas = ruedas
    def __str__(self):
        return f"color {self.color} - ruedas {self.ruedas} "

class Auto(Vehiculo):
    def __init__(self, color, ruedas, velocidad):
        super().__init__(color, ruedas)
        self.velocidad = velocidad
    def __str__(self):
        return super().__str__() + f"- velocidad {self.velocidad} " 


class Camioneta(Auto):
    def __init__(self, color, ruedas, velocidad, carga):
        super().__init__(color, ruedas, velocidad)
        self.carga = carga
    def __str__(self):
        return super().__str__() + f"- carga {self.carga}"

class Bicicleta(Vehiculo):
    def __init__(self, color, ruedas, tipo):
        super().__init__(color, ruedas)
        self.tipo = tipo
    def __str__(self):
        return super().__str__() + f"- tipo {self.tipo} "

class Motocicleta(Bicicleta):
    def __init__(self, color, ruedas, tipo, velocidad, cilindrada):
        super().__init__(color, ruedas, tipo)
        self.velocidad = velocidad
        self.cilindrada = cilindrada
    def __str__(self):
        return super().__str__() + f"- velociada {self.velocidad} - cilindrada {self.cilindrada} "

    
Vehiculos = [
    Auto("rojo",4,180),
    Camioneta("verde",4,170,1000),
    Bicicleta("Negra",2,"Urbana"),
    Motocicleta("Blanca", 2, "Urbana", 300, 350)
]

def Catalogar(DATA):
    for vehiculo in DATA:
        print(vehiculo)

# Catalogar(Vehiculos)

def CatalogarRuedas(DATA,ruedas = 0):
    encontrados = 0
    for vehiculo in DATA:
        if vehiculo.ruedas == ruedas:
            encontrados+=1
            print(vehiculo)
    print(f"Se han encontrado {encontrados} vehículos con {ruedas} ruedas")

# CatalogarRuedas(Vehiculos,2)