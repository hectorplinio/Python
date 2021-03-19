archivo= open("/media/HECTORNAVARRO/B092-7F82/daw2/programacion/Segunda/Censo.txt","r")
contador=0
x=input("Dime una provincia:")
x=x.upper()
lista=[]
for linea in archivo:
    lista=linea.split(",")
    for i in (lista):
        if i==x:
            print(linea)
            contador= contador+1
        
print(contador)
archivo.close()