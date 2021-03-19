class Vehiculo():
    def __init__(self, marca, modelo):
        self.marca=marca
        self.modelo=modelo
        self.enmarcha=False
        self.acelera=False
        self.frena=False

    def arrancar(self):
        self.enmarcha=True
    
    def acelerar (self):
        self.acelera=True
    
    def frena (self):
        self.frena=True

    def estado (self):
        print("Marca: ",self.marca,"\nModelo: ", self.modelo, "\nEn Marcha: ",
        self.enmarcha, "\nAcelerando: ", self.acelera, "\nFrenando: ", self.frena)

class Moto(Vehiculo):
    hcaballito=""
    def caballito(self):
        self.hcaballito="Voy haciendo el caballito"
    
    def estado (self):
        print("Marca: ",self.marca,"\nModelo: ", self.modelo, "\nEn Marcha: ",
        self.enmarcha, "\nAcelerando: ", self.acelera, "\nFrenando: ", self.frena
        ,"\n", self.hcaballito)
    
class Furgoneta(Vehiculo):
    def carga(self, cargar):
        self.cargado=cargar
        if (self.cargado):
            return "La furgoneta esta cargada"
        else:
            return "La furgoneta no esta cargada"

class Velectricos():
    def __init__(self):
        self.autonomia=100

    def cargar_energia(self):
        self.cargando=True
    
class Bicicleta_electrica(Vehiculo,Velectricos):
    pass

miMoto=Moto("Honda", "CBR")

miMoto.caballito()
miMoto.estado()
miFurgoneta=Furgoneta("Mercedes", "Vito")
miFurgoneta.arrancar()
miFurgoneta.estado()
print(miFurgoneta.carga(True))
miBici=Bicicleta_electrica("Orbea", "HC1030")