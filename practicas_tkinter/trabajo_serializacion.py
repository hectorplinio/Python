#Esta biblioteca sirve para crear archivos escritos en binario
import pickle
#Creamos una lista
lista_nombres=["Pedro", "Ana", "Maria", "Isabel"]
#Abrimos el archivo con wb que es WriteBinary
fichero_binario=open("lista_nombres","wb")
#Dump sirve para volver los datos en el fichero
pickle.dump(lista_nombres, fichero_binario)
#Cerramos el fichero
fichero_binario.close()

del(fichero_binario)