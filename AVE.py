archivo= open("/media/HECTORNAVARRO/D0A5-EB0D/DAW/programacion/Segunda/Localidades.txt","r")
nuevo= open("/media/HECTORNAVARRO/D0A5-EB0D/DAW/programacion/Segunda/AVE.txt","w+")
lista_AVE=[]
contador=0
x=input("Dime si quieres saber si tiene AVE o no:")
x=x.upper()
lista=[]
u=0
if x == "SI":
    nuevo.write("Esta es la lista de ciudades con AVE.\n")
    for linea in archivo:
        lista=linea.split(",")
        for i in (lista[5].rstrip("\n")):
            if i=="1":
                print(lista[2])
                u=lista[2]
                lista_AVE.append(u)
                nuevo.write(u+"\n")
                contador= contador+1
            
else:
    nuevo.write("Esta es la lista de ciudades sin AVE.\n")
    for linea in archivo:
        lista=linea.split(",")
        for i in (lista[5].rstrip("\n")):
            if i=="0":
                print(lista[2])
                u=lista[2]
                lista_AVE.append(u)
                nuevo.write(u+"\n")
                contador= contador+1


u       
print("El número de resultados es " + str(contador))

archivo.close()