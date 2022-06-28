## 1
## 1
## 1
from re import I


class Persona: 
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad

    def get_nombre(self):
        return self.nombre

    def get_edad(self):
        return self.edad

    def set_nombre(self,dato):
         self.nombre = dato

    def set_edad(self,dato):
         self.edad = dato

    # @staticmethod
    # def es_mayor_que(person1, person2):
    #     if person1.edad > person2.edad:
    #         return f"{person1.nombre} es mayor que {person2.nombre}"
    #     else:
    #         return f"{person2.nombre} es mayor que {person1.nombre}"
    def es_mayor_que(self,otra_persona):
        if self.edad > otra_persona.edad:
            return "si es mayor"
        else:
            return "No es mayor"

    @staticmethod
    def get_mayor(persona1,persona2):
        if persona1.edad > persona2.edad:
            return f"{persona1.nombre} es mayor que {persona2.nombre}"
        else:
            return f"{persona2.nombre} es mayor que {persona1.nombre}"


class Alumnos:
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota
    def __str__(self):
        return f"nombre: {self.nombre} \nnota: {self.nota}"
    def aprobo(self):
        if self.nota > 4:
            return "Aprobo."
        else: 
            return "No aprobo." 


class Triangulo:
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c
    def tipo(self):
        if self.c == self.a == self.b:
            return "Es Equilatero"
        elif self.a == self.b or self.a == self.c or self.b== self.c:
            return "Es Isosceles"
        else: 
            return "Es Escaleno" 



class Calculadora:
    def __init__(self):
        self.n1 = int(input()) 
        self.n2 = int(input())
        
    def sumar(self):
        return self.n1 + self.n1

    def restar(self):
        return self.n1 - self.n1    
        
    def multiplicar(self):
        return self.n1 * self.n1

    def dividir(self):
        return self.n1 / self.n1

    def __str__(self):
        return f"Valores ingresados: {self.n1} {self.n1} \nsuma: {self.sumar()}\nresta: {self.restar()}\nmultipicar: {self.multiplicar()}\ndivicion: {self.dividir()}"

# prueba = Calculadora()
# print(prueba)

# class Agenda:
#     def __init__(self):
#         self.contactos = [{"99id":{"nombre":'lautaro',"numero":123,"email":'123'}},{"100id":{"nombre":'martin',"numero":123,"email":'123'}}]
#         self.id = 0

#     def iniciar_app(self):
#         run = True
#         print('Agenda abierta')
#         while run:
#             option = int(input('Opciones:\n1)agregar contacto \n2)eliminar contacto\n3)mostar contactos\n4)editar contacto\n5)cerrar agenda'))
#             if option == 1:
#                 self.agregar_contacto()
#             elif option == 2:
#                 self.eliminar_contacto()
#             elif option == 3:
#                  self.mostrar_contactos()
#             elif option == 4:
#                 self.editar_contacto()
#             elif option == 5:
#                 run = False
#                 print("app cerrada")
#             else:
#                 print("Opcion no valida")

#     def agregar_contacto(self):
#         nombre = str(input('ingrese nombre: '))
#         numero = int(input('ingrese numero: '))
#         email = str(input('ingrese email: '))
#         self.id += 1
#         keyid = f'{self.id}id'
#         self.contactos[keyid] = {'nombre': nombre,'numero': numero,'email': email}
#         c=input("presiona Enter para continuar...")
#         print("---------------------------")


#     def eliminar_contacto(self):
#         if len(self.contactos) <= 0:
#             print("no hay contactos")
#             c=input("presiona Enter para continuar...")
#             print("---------------------------")

#         else:
#             # eliminar = str(input('eliminar a: '))
#             for n in range(len(self.contactos)):
#                 # if self.contactos[n].values()
#                 print(list(self.contactos[n]))
#                 print(self.contactos[n]['name'])
#             # del self.contactos['99id']
#             # for (key,values) in self.contactos.items():

#             #     if values['nombre'] == eliminar:
#             #         del self.contactos[str(key)]
#             #         del self.contactos[key]                    
#             # c=input("presiona Enter para continuar...")
#             # print("---------------------------")




# # class ListaContactos:
# # class Contacto:

#     def editar_contacto(self):
#         editar = str(input('editar a: '))
#         for (key,values) in self.contactos:
#             if values['nombre'] == editar:
#                 # nombre = str(input('ingrese nombre: '))
#                 # numero = int(input('ingrese numero: '))
#                 # email = str(input('ingrese email: '))
#                 print(values)
#                 print(key)
#                 del key
#         print("---------------------------")
    

#     def mostrar_contactos(self):
#         print("---------------------------")
#         for (key,values) in self.contactos:
#             print("---------------------------")
#             print(f"nombre {values['nombre']}\nnumero: {values['numero']}\nemail:{values['email']}")
#         print("---------------------------")
#         c=input("presiona Enter para continuar...")


# # prueba = Agenda()

# # prueba.iniciar_app()


class Contacto:
    def __init__(self):
        self.nombre = str(input('nombre: '))
        self.numero = int(input('numero: '))
        self.email  = str(input('email: '))
    def __str__(self):
        return f"| nombre: {self.nombre} | numero: {self.numero} | email: {self.email} |"
    def editar_data(self):
        self.nombre = str(input(f'cambiar nombre de {self.nombre} a:  '))
        self.numero = int(input(f'cambiar numero de {self.numero} a: '))
        self.email  = str(input(f'cambiar email de {self.email} a: '))

class Agenta_App:
    def __init__(self):
        self.contactos = []
        self.run_app()
    def agregar_contacto(self):
        self.contactos.append(Contacto())
    def editar_contacto(self):
        editar = str(input('Editar a: '))
        for n in self.contactos:
            if n.nombre == editar:
                n.editar_data()
            else:
                print('contacto no encontrado...')
    def eliminar_contacto(self):
        eliminar = str(input('eliminar a: '))
        existe = False
        for n in self.contactos:
            if n.nombre == eliminar:
                existe = True
            else:
                print('contacto no encontrado...')
        if existe:
            new_list = list(filter(lambda x: x.nombre != eliminar , self.contactos))
            print(new_list)
            self.contactos = new_list
    def mostrar_contactos(self):
        if len(self.contactos) <= 0:
            print('-----------------------------------------------------')
            print('No hay contactos agendados...')
            print('-----------------------------------------------------')
        else:
            print('-----------------------------------------------------')
            for n in self.contactos:
                print(n)
            print('-----------------------------------------------------')
    def run_app(self):
        run = True
        while run:
            print("\n1) agregar contacto\n2) eliminar contacto \n3) editar contacto\n4) mostrar contactos\n5) cerrar\n")
            orden = int(input("opcion: "))
            if orden == 1:
                self.agregar_contacto()
            elif orden == 2:
                self.eliminar_contacto()
            elif orden == 3:
                self.editar_contacto()
            elif orden == 4:
                self.mostrar_contactos()
            elif orden == 5:
                run = False  
                print('cerrando agenda')
            else:
                print('opcion invalida...')

# app = Agenta_App()


class Usucario_Bancario():
    def __init__(self,nombre):
        self.nombre = nombre
        self.cuenta = 500

    def extraer(self,cantidad):
        if cantidad > self.cuenta:
            print("saldo insuficiente...")
        else:
            print(f"saldo extraido de {cantidad}")
            self.cuenta -= cantidad
            print(f"saldo es de {self.cuenta}...")

    def depositar(self,cantidad):
        if cantidad > 1:
            self.cuenta += cantidad
            print(f"saldo de {cantidad} acreditado...")
    def mostrar_total(self):
        print(f"saldo de: {self.cuenta}")

class Banco:
    def __init__(self):
        self.usuarios = [Usucario_Bancario("Lautaro"),Usucario_Bancario("Maria"),Usucario_Bancario("Matias")]
        self.operar()

    def operar(self):
        run = True
        while run:
            print('1) Operar usuario\n2) deposito total\n3) Cerrar')
            accion = int(input("operacion: "))
            if accion == 1:
                usuario = (input("ingrese usuario: "))
                for n in self.usuarios:
                    if n.nombre == usuario:
                        self.run_usuario(n)
                        break
            elif accion == 2: 
                total = 0
                print('-----------------')
                for n in self.usuarios:
                    print(f"{n.cuenta}  {n.nombre}")
                    total += n.cuenta
                print(f'total: {total}')
                print('-----------------')
            elif accion == 3 :
                run = False
            else:
                print("accion invalida...")                
    def run_usuario(self,usuario):
        runn = True
        while runn:
            print(f"usuario: {usuario.nombre}")
            print("\n    1)depositar\n    2) extraer\n    3) cerrar")
            operacion = int(input())
            if operacion == 1:
                cantidad_dep = int(input('cantida: '))
                usuario.depositar(cantidad_dep)
            elif operacion == 2:
                cantidad_ext = int(input('cantida: '))
                usuario.extraer(cantidad_ext)
            elif operacion == 3:
                runn = False
            else:
                print("accion invalida...")

prueba = Banco()