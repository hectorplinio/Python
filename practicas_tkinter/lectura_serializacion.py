import pickle
from serializar_objetos import Vehiculo

ficheroApertura=open("losCoches","rb")
#Cargamos los datos
misCoches=pickle.load(ficheroApertura)

ficheroApertura.close()

for c in misCoches:
    print(c.estado())