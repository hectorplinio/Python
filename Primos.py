#3.- Escribe un programa que pida un número entero y diga si es primo, y de no serlo que lo descomponga en factores 
x= int(input("Escriba un número pasa saber si es primo: "))
z=1
contador=0
lista_p = [2]
lista_n = []
lista_f =[]
y=2
b=1
t=x
for i in range (x):
    if x %z==0:
        contador+=1
        lista_n.append(z)
        z=z+1
      
    else:
        z=z+1

if contador >2:
    print ("No es primo.")
    print ("Esta es la lista de divisores de " + str(x) + ":" + str(lista_n) )
    for i in range(x):
      if x%y==0:
        b = x//y
        lista_f.append(y)
        x=b
      if x%y!=0:
        y=y+1
    
    print ("Esta es tu lista de factores de "+ str(t) + ":" + str(lista_f))

if contador <3:
    print ("Es primo.")

