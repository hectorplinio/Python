import time
import os


x=str(input("Dime una palabra:"))
os.system ("cls")
lista_palabra=[]
lista_barra=[]
lista_descubierta=[]
intentos=5

t=0

def separar(): 
    global lista_palabra
    for i in x:
        lista_palabra.append(i)

def dibujar_lineas():
    global lista_barra
    for i in range (len(lista_palabra)):
        lista_barra.append("_")
    t=i
        
    for i in range (len(lista_barra)):
        print(lista_barra[i],end=" ")
    print()

def lineas_descubiertas():
    for i in range (len(lista_barra)):
        print(lista_barra[i],end=" ")
    print()

def descubrir_letras():
    global intentos
    contador=0
    y=str(input("Dime una letra:"))
    for i in range (len(lista_palabra)):
        z=lista_palabra[i]
        if y == z:
            lista_barra[i]=y
            contador=contador+1
            pass
    if contador== 0:
        print("Tu letra no esta en la palabra")
        intentos= intentos-1
        print("Te quedan",intentos,"intentos.")


    
    
    
separar()
dibujar_lineas()
os.system ("cls")
while intentos!=0 and t==0:
    lineas_descubiertas()
    descubrir_letras()
while intentos==0:
    print("Lo siento has perdido, tienes",intentos,"intentos")
    break
    