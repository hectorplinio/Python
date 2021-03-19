import pickle
#lo abrimos con rb por ReadBinary
fichero=open("lista_nombres","rb")
#sirve para cargar la informacion binaria
lista=pickle.load(fichero)

print(lista)