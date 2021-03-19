archivo= open("/media/HECTORNAVARRO/B092-7F82/daw2/programacion/Segunda/Censo.txt","r")
contador=0
x=input("Dime una provincia:")
x=x.upper()
for linea in archivo:
    linea.count(x)
    if linea.count(x)>=1:
        print(linea)
        contador= contador+1
print(contador)
archivo.close()