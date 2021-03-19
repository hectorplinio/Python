archivo= open("/media/HECTORNAVARRO/B092-7F82/daw2/programacion/Segunda/Localidades.txt","r")
nuevo= open("/media/HECTORNAVARRO/B092-7F82/daw2/programacion/Segunda/Orden_km-.txt","w+")
contador=0
x=int(input("Dime la cantidad de localidades a mostrar:"))
lista=[]
i=0
dc={}
lista_orden=[]

for linea in archivo:
    lista=linea.split(",")
    try:
        y=int(lista[3])
        dc[y]=lista[2]
        lista_orden.append(y)
        
        
    except:
        pass

nuevo.write("Esta es la lista ordenada de cercana a lejana. \n")

lista_orden.sort(reverse=True)
for i in lista_orden:
    u=str(i) + " " + dc[i] + "\n"
    nuevo.write(u)
    print(i,dc[i])
    x=x-1
    if x==0:
        break   
archivo.close()
nuevo.close()
