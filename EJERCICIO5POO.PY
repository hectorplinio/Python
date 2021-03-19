semaforo=True
class Agenda:
    def __init__(self, nombre, telefono, email):
        self.nombre=nombre
        self.telefono=telefono
        self.email=email

    

    def add(self):
        global t
        print("Has seleccionado añadir un nuevo contacto.")
        nom=input("Ponga el nombre:")
        tel=input("Ponga el numero de telefono: ")
        ema=input("Ponga el correo electronico: ")
        self.nombre.append(nom)
        self.telefono.append(tel)
        self.email.append(ema)
        print("El nombre es " + self.nombre[0+t], "el numero de telefono es " + self.telefono[0+t], "y el correo es " + self.email[0+t])
        t=t+1

    def lista(self):
        print("Has selecionado lista de contactos.")
        for i in range(len(self.nombre)):
            print("El nombre es " + self.nombre[i], "el numero de telefono es " + self.telefono[i], "y el correo es " + self.email[i])


    
    def buscar(self):
        print("Has selecionado buscar un contacto.")
        y=int(input("Que contacto quieres buscar? "))
        print("El nombre es " + self.nombre[y-1], "el numero de telefono es " + self.telefono[y-1], "y el correo es " + self.email[y-1])

    def editar(self):
        print("Has selecionado editar un contacto.")
        z= int(input("Que contacto quieres editar? "))
        print("El nombre es " + self.nombre[z-1], "el numero de telefono es " + self.telefono[z-1], "y el correo es " + self.email[z-1])
        nom=input("Dame el nombre nuevo: ")
        tel=input("Dime el numero: ")
        ema=input("Dime el correo: ")
        self.nombre[z-1]=nom
        self.telefono[z-1]=tel
        self.email[z-1]=ema

    def salir(self):
        global semaforo
        print("Has selecionado salir. ADIOS")
        semaforo=False

c1=Agenda([],[],[])
def pantalla():
    global lista
    for i in (lista):
        print (i)
    x=int(input("Diga una opcion:"))
    if x == 1:
        c1.add()
    elif x == 2:
        c1.lista()
    elif x == 3:
        c1.buscar()
    elif x == 4:
        c1.editar()
    elif x == 5:
        c1.salir()

lista=["Agenda Personal", "1. Añadir un contacto", "2. Lista de contactos", "3. Buscar un contacto", "4. Editar un contacto", "5. Cerrar agenda"]

x=0
t=0
while semaforo == True:
    pantalla()