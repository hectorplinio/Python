archivo= open("/media/HECTORNAVARRO/B092-7F82/daw2/programacion/Segunda/Prueba.txt","r+")
copia_respuesta= str(input("Dime el nombre de el nuevo archivo: "))
copia=open(copia_respuesta +".txt","w+")
for linea in archivo:
    copia.write(linea)
#Cada vez que se trabaja con el archivo hay que cerrarlo y volver a abrirlo.
archivo.close()
copia.close()
archivo= open("/media/HECTORNAVARRO/B092-7F82/daw2/programacion/Segunda/Prueba.txt","r+")
copia=open(copia_respuesta +".txt","r")
for linea in archivo:
    print(linea)
for linea in copia:
    print(linea)
archivo.close()
copia.close()
