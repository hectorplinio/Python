#3.- Escribe un programa que pida un número entero y diga si es primo, y de no serlo que lo descomponga en factores 
x= int(input("Escriba un número pasa saber si es primo: "))
z=1
contador=0
lista_p = [2]
lista_n = []
lista_f = []
y=1
for i in range (x):
    if x %z==0:
        contador+=1
        lista_n.append(z)
        z=z+1
    if x>0:
        if x%2==0 or x%3==0 or x%5==0 or x%7==0:
            lista_f.append(x)
            y=x/2
        if y%2==0 or x%3==0 or x%5==0 or x%7==0:
            

    else:
        z=z+1

if contador >2:
    print ("No es primo.")
    print (lista_n)
    
if contador <3:
    print ("Es primo.")

