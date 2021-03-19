semaforo=True
class Cliente:
    def __init__(self, nombre, cantidad):
        self.nombre=nombre
        self.cantidad=cantidad

    def depositar(self):
        global t
        nom=input("Introduzca su nombre: ")
        can=int(input("Introduzca la cantidad: "))
        self.nombre.append(nom)
        self.cantidad.append(can)
        print(self.nombre[t-1]+" ha ingresado la cantidad de " + str(self.cantidad[t-1]) + "€.")
        t=t+1

    def extraer(self):
        global t 
        nom=input("Introduzca su nombre: ")
        can=int(input("Introduzca la cantidad: "))
        self.nombre.append(nom)
        can=can*-1
        self.cantidad.append(can)
        print(self.nombre[t-1]+" ha extraido la cantidad de " + str(self.cantidad[t-1]) + "€.")
        
        
        t=t+1
    
    def mostrar_total(self):
        w=input("Que nombre quieres buscar: ")
        resultado=0
        total=0
        for i in (self.nombre):
            if i == w:
                total=self.cantidad[resultado]+total

            resultado=resultado+1
        print("Tiene un total en la cuenta de" , total, "€.")

class Banco():
    def __init__(self, cliente, cantidad ):
        self.cliente=cliente
        self.cantidad=cantidad
    
    def operar(self):
        q=input("Dime el nombre del cliente que quieres que te muestre informacion: ")
        tot=0
        for i in (self.cliente):
            if i == q:
                print("El cliente",i, "ha hecho esta opercacion", self.cantidad[tot],)
            tot=tot+1
    def deposito_total(self):
        dep=0
        depo=0
        for i in (self.cantidad):
            dep=i+depo
            depo=dep
        print("El banco ha generado ",dep," €.")




c1=Cliente([],[])
b1=Banco(c1.nombre,c1.cantidad)
def menu():
    global semaforo
    x=input("Introduzca si es cliente, banco o salir: ")
    if x == "cliente":
        for i in (lista_cliente):
            print(i)
        p=int(input("Que operacion quieres hacer?: "))
        if p == 1:
            c1.depositar()
        elif p == 2:
            c1.extraer()
        elif p == 3:
            c1.mostrar_total()
        else:
            p=int(input("Pon una opcion correcta: "))
    if x == "banco":
        for i in (lista_banco):
            print(i)
        s=int(input("Que operacion quieres hacer?: "))
        if s == 1:
            b1.operar()
        if s == 2:
            b1.deposito_total()
    if x == "salir":
        semaforo=False




    


lista_cliente= ["1- Depositar", "2- Extraer", "3- Mostrar total", "4- Salir"]
lista_banco= ["1- Operaciones", "2- Deposito total", "3- Salir"]
t=1
while semaforo == True:
    menu()
else:
    print("Has seleccionado salir, adiós.")
    exit