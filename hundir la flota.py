import os
import time
from colorama import init,Fore
init(autoreset=True)
#Lista barcos
lista_n = [" ",  Fore.LIGHTYELLOW_EX+"1",   Fore.LIGHTYELLOW_EX+"2",   Fore.LIGHTYELLOW_EX+"3",   Fore.LIGHTYELLOW_EX+"4",   Fore.LIGHTYELLOW_EX+"5",   Fore.LIGHTYELLOW_EX+"6",   Fore.LIGHTYELLOW_EX+"7",   Fore.LIGHTYELLOW_EX+"8",   Fore.LIGHTYELLOW_EX+"9"  ]
lista_a = ["A", "*", "*", "*", "*", "O", "O", "*", "*", "*" ]
lista_b = ["B", "O", "O", "O", "*", "*", "*", "*", "*", "*" ]
lista_c = ["C", "*", "*", "*", "*", "*", "O", "*", "*", "*" ]
lista_d = ["D", "O", "O", "*", "*", "*", "O", "*", "*", "*" ]
lista_e = ["E", "*", "*", "*", "*", "*", "O", "*", "*", "*" ]
lista_f = ["F", "*", "*", "*", "*", "*", "*", "*", "O", "O" ]
lista_g = ["G", "*", "*", "*", "O", "O", "O", "*", "*", "*" ]
lista_h = ["H", "*", "*", "*", "*", "*", "*", "O", "O", "*" ]
lista_i = ["I", "*", "*", "O", "O", "*", "*", "*", "*", "*" ]
#lista_n = [" ",  Fore.LIGHTYELLOW_EX+"1",   Fore.LIGHTYELLOW_EX+"2",   Fore.LIGHTYELLOW_EX+"3",   Fore.LIGHTYELLOW_EX+"4",   Fore.LIGHTYELLOW_EX+"5",   Fore.LIGHTYELLOW_EX+"6",   Fore.LIGHTYELLOW_EX+"7",   Fore.LIGHTYELLOW_EX+"8",   Fore.LIGHTYELLOW_EX+"9"  ]
#lista_a = ["A", "", "", "", "", "", "", "", "", "" ]
#lista_b = ["B", "", "", "", "", "", "", "", "", "" ]
#lista_c = ["C", "", "", "", "", "", "", "", "", "" ]
#lista_d = ["D", "", "", "", "", "", "", "", "", "" ]
#lista_e = ["E", "", "", "", "", "", "", "", "", "" ]
#lista_f = ["F", "", "", "", "", "", "", "", "", "" ]
#lista_g = ["G", "", "", "", "", "", "", "", "", "" ]
#lista_h = ["H", "", "", "", "", "", "", "", "", "" ]
#lista_i = ["I", "", "", "", "", "", "", "", "", "" ]
#Lista vacia
lista_a2 = [Fore.LIGHTYELLOW_EX+"A", Fore.BLUE+"*", Fore.BLUE+"*", Fore.BLUE+"*", Fore.BLUE+"*", Fore.BLUE+"*", Fore.BLUE+"*", Fore.BLUE+"*", Fore.BLUE+"*", Fore.BLUE+"*" ]
lista_b2 = [Fore.LIGHTYELLOW_EX+"B", Fore.BLUE+"*", Fore.BLUE+"*", Fore.BLUE+"*", Fore.BLUE+"*", Fore.BLUE+"*", Fore.BLUE+"*", Fore.BLUE+"*", Fore.BLUE+"*", Fore.BLUE+"*" ]
lista_c2 = [Fore.LIGHTYELLOW_EX+"C", Fore.BLUE+"*", Fore.BLUE+"*", Fore.BLUE+"*", Fore.BLUE+"*", Fore.BLUE+"*", Fore.BLUE+"*", Fore.BLUE+"*", Fore.BLUE+"*", Fore.BLUE+"*" ]
lista_d2 = [Fore.LIGHTYELLOW_EX+"D", Fore.BLUE+"*", Fore.BLUE+"*", Fore.BLUE+"*", Fore.BLUE+"*", Fore.BLUE+"*", Fore.BLUE+"*", Fore.BLUE+"*", Fore.BLUE+"*", Fore.BLUE+"*" ]
lista_e2 = [Fore.LIGHTYELLOW_EX+"E", Fore.BLUE+"*", Fore.BLUE+"*", Fore.BLUE+"*", Fore.BLUE+"*", Fore.BLUE+"*", Fore.BLUE+"*", Fore.BLUE+"*", Fore.BLUE+"*", Fore.BLUE+"*" ]
lista_f2 = [Fore.LIGHTYELLOW_EX+"F", Fore.BLUE+"*", Fore.BLUE+"*", Fore.BLUE+"*", Fore.BLUE+"*", Fore.BLUE+"*", Fore.BLUE+"*", Fore.BLUE+"*", Fore.BLUE+"*", Fore.BLUE+"*" ]
lista_g2 = [Fore.LIGHTYELLOW_EX+"G", Fore.BLUE+"*", Fore.BLUE+"*", Fore.BLUE+"*", Fore.BLUE+"*", Fore.BLUE+"*", Fore.BLUE+"*", Fore.BLUE+"*", Fore.BLUE+"*", Fore.BLUE+"*" ]
lista_h2 = [Fore.LIGHTYELLOW_EX+"H", Fore.BLUE+"*", Fore.BLUE+"*", Fore.BLUE+"*", Fore.BLUE+"*", Fore.BLUE+"*", Fore.BLUE+"*", Fore.BLUE+"*", Fore.BLUE+"*", Fore.BLUE+"*" ]
lista_i2 = [Fore.LIGHTYELLOW_EX+"I", Fore.BLUE+"*", Fore.BLUE+"*", Fore.BLUE+"*", Fore.BLUE+"*", Fore.BLUE+"*", Fore.BLUE+"*", Fore.BLUE+"*", Fore.BLUE+"*", Fore.BLUE+"*" ]
#Imprimir tabla vacia
for i in range (len(lista_n)):
    print (lista_n [i], end=" ")
print()
for i in range (len(lista_a2)):
    print (lista_a2 [i], end=" ")
print()
for i in range (len(lista_b2)):
    print (lista_b2 [i], end=" ")
print()
for i in range (len(lista_c2)):
    print (lista_c2 [i], end=" ")
print()
for i in range (len(lista_d2)):
    print (lista_d2 [i], end=" ")
print()
for i in range (len(lista_e2)):
    print (lista_e2 [i], end=" ")
print()
for i in range (len(lista_f2)):
    print (lista_f2 [i], end=" ")
print()
for i in range (len(lista_g2)):
    print (lista_g2 [i], end=" ")
print()
for i in range (len(lista_h2)):
    print (lista_h2 [i], end=" ")
print()
for i in range (len(lista_i2)):
    print (lista_i2 [i], end=" ")
print()
print()


print (Fore.GREEN + "Bienvenido a hundir la flota, vamos a jugar:")
y= str(input ("Escribe una letra de la A a la I:"))
x= int(input ("Escribe un número del 1 al 9:"))


lista_p=[]
lista_historial=[]
contador = int(0)
z=int(0)
#barcos totales
b=int(19)
t=0
for i in range (x):
    while y!="SALIR" or z==1:
        if y=="A" or y=="a":
            
            t=y.upper()
            y=lista_a
            if lista_a[x]=="O":
                lista_p.append (str(t)+str(x)) 
                print ("Has dado en el blanco, uno menos!")
                b=b-1
                print ("Te quedan "  +str(b)+ " barcos.")
                z=z+1
                contador += 1
                print ("Llevas " + str(contador) + " intentos")
                print ("Coordenadas de barcos destruidos " + str(lista_p) )
                print ("Historial de disparos fallidos: " + str(lista_historial))
                lista_a2[x] = (Fore.RED+"O")
                for i in range (len(lista_n)):
                    print (lista_n [i], end=" ")
                print()
                for i in range (len(lista_a2)):
                    print (lista_a2 [i], end=" ")
                print()
                for i in range (len(lista_b2)):
                    print (lista_b2 [i], end=" ")
                print()
                for i in range (len(lista_c2)):
                    print (lista_c2 [i], end=" ")
                print()
                for i in range (len(lista_d2)):
                    print (lista_d2 [i], end=" ")
                print()
                for i in range (len(lista_e2)):
                    print (lista_e2 [i], end=" ")
                print()
                for i in range (len(lista_f2)):
                    print (lista_f2 [i], end=" ")
                print()
                for i in range (len(lista_g2)):
                    print (lista_g2 [i], end=" ")
                print()
                for i in range (len(lista_h2)):
                    print (lista_h2 [i], end=" ")
                print()
                for i in range (len(lista_i2)):
                    print (lista_i2 [i], end=" ")
                print()
                print()
                    
            if lista_a[x]!="O":
                lista_historial.append (str(t)+str(x)) 
                print ("Mala suerte, sigue probando suerte!")
                z=z+1
                print ("Te quedan "  +str(b)+ " barcos.")
                contador += 1
                print ("Llevas " + str(contador) + " intentos")
                print ("Coordenadas de barcos destruidos " + str(lista_p) )
                print ("Historial de disparos fallidos: " + str(lista_historial))
                lista_a2[x] = (Fore.BLUE+"~")
                for i in range (len(lista_n)):
                    print (lista_n [i], end=" ")
                print()
                for i in range (len(lista_a2)):
                    print (lista_a2 [i], end=" ")
                print()
                for i in range (len(lista_b2)):
                    print (lista_b2 [i], end=" ")
                print()
                for i in range (len(lista_c2)):
                    print (lista_c2 [i], end=" ")
                print()
                for i in range (len(lista_d2)):
                    print (lista_d2 [i], end=" ")
                print()
                for i in range (len(lista_e2)):
                    print (lista_e2 [i], end=" ")
                print()
                for i in range (len(lista_f2)):
                    print (lista_f2 [i], end=" ")
                print()
                for i in range (len(lista_g2)):
                    print (lista_g2 [i], end=" ")
                print()
                for i in range (len(lista_h2)):
                    print (lista_h2 [i], end=" ")
                print()
                for i in range (len(lista_i2)):
                    print (lista_i2 [i], end=" ")
                print()
                print()

            lista_a[x]="*"
            
            
        elif y=="B" or y=="b": 
            t=y.upper()
            y=lista_b
            if lista_b[x]=="O":
                lista_p.append (str(t)+str(x))
                print ("Has dado en el blanco, uno menos!")
                b=b-1
                print ("Te quedan "  +str(b)+ " barcos.")
                z=z+1
                contador += 1
                print ("Llevas " + str(contador) + " intentos")
                print ("Coordenadas de barcos destruidos " + str(lista_p) )
                print ("Historial de disparos fallidos: " + str(lista_historial))
                lista_b2[x] = (Fore.RED+"O")
                for i in range (len(lista_n)):
                    print (lista_n [i], end=" ")
                print()
                for i in range (len(lista_a2)):
                    print (lista_a2 [i], end=" ")
                print()
                for i in range (len(lista_b2)):
                    print (lista_b2 [i], end=" ")
                print()
                for i in range (len(lista_c2)):
                    print (lista_c2 [i], end=" ")
                print()
                for i in range (len(lista_d2)):
                    print (lista_d2 [i], end=" ")
                print()
                for i in range (len(lista_e2)):
                    print (lista_e2 [i], end=" ")
                print()
                for i in range (len(lista_f2)):
                    print (lista_f2 [i], end=" ")
                print()
                for i in range (len(lista_g2)):
                    print (lista_g2 [i], end=" ")
                print()
                for i in range (len(lista_h2)):
                    print (lista_h2 [i], end=" ")
                print()
                for i in range (len(lista_i2)):
                    print (lista_i2 [i], end=" ")
                print()
                print()
                
            if lista_b[x]!="O":
                lista_historial.append (str(t)+str(x))
                print ("Mala suerte, sigue probando suerte!")
                z=z+1
                print ("Te quedan "  +str(b)+ " barcos.")
                contador += 1
                print ("Llevas " + str(contador) + " intentos")
                print ("Coordenadas de barcos destruidos " + str(lista_p) )
                print ("Historial de disparos fallidos: " + str(lista_historial))
                lista_b2[x] = (Fore.BLUE+"~")
                for i in range (len(lista_n)):
                    print (lista_n [i], end=" ")
                print()
                for i in range (len(lista_a2)):
                    print (lista_a2 [i], end=" ")
                print()
                for i in range (len(lista_b2)):
                    print (lista_b2 [i], end=" ")
                print()
                for i in range (len(lista_c2)):
                    print (lista_c2 [i], end=" ")
                print()
                for i in range (len(lista_d2)):
                    print (lista_d2 [i], end=" ")
                print()
                for i in range (len(lista_e2)):
                    print (lista_e2 [i], end=" ")
                print()
                for i in range (len(lista_f2)):
                    print (lista_f2 [i], end=" ")
                print()
                for i in range (len(lista_g2)):
                    print (lista_g2 [i], end=" ")
                print()
                for i in range (len(lista_h2)):
                    print (lista_h2 [i], end=" ")
                print()
                for i in range (len(lista_i2)):
                    print (lista_i2 [i], end=" ")
                print()
                print()


            lista_b[x]="*"

        elif y =="C" or y=="c":
            t=y.upper()
            y=lista_c
            if lista_c[x]=="O":
                lista_p.append (str(t)+str(x))
                print ("Has dado en el blanco, uno menos!")
                b=b-1
                print ("Te quedan "  +str(b)+ " barcos.")
                z=z+1
                contador += 1
                print ("Llevas " + str(contador) + " intentos")
                print ("Coordenadas de barcos destruidos " + str(lista_p) )
                print ("Historial de disparos fallidos: " + str(lista_historial))
                lista_c2[x] = (Fore.RED+"O")
                for i in range (len(lista_n)):
                    print (lista_n [i], end=" ")
                print()
                for i in range (len(lista_a2)):
                    print (lista_a2 [i], end=" ")
                print()
                for i in range (len(lista_b2)):
                    print (lista_b2 [i], end=" ")
                print()
                for i in range (len(lista_c2)):
                    print (lista_c2 [i], end=" ")
                print()
                for i in range (len(lista_d2)):
                    print (lista_d2 [i], end=" ")
                print()
                for i in range (len(lista_e2)):
                    print (lista_e2 [i], end=" ")
                print()
                for i in range (len(lista_f2)):
                    print (lista_f2 [i], end=" ")
                print()
                for i in range (len(lista_g2)):
                    print (lista_g2 [i], end=" ")
                print()
                for i in range (len(lista_h2)):
                    print (lista_h2 [i], end=" ")
                print()
                for i in range (len(lista_i2)):
                    print (lista_i2 [i], end=" ")
                print()
                print()
                
            if lista_c[x]!="O":
                lista_historial.append (str(t)+str(x))
                print ("Mala suerte, sigue probando suerte!")
                z=z+1
                print ("Te quedan "  +str(b)+ " barcos.")
                contador += 1
                print ("Llevas " + str(contador) + " intentos")
                print ("Coordenadas de barcos destruidos " + str(lista_p) )
                print ("Historial de disparos fallidos: " + str(lista_historial))
                lista_c2[x] = (Fore.BLUE+"~")
                for i in range (len(lista_n)):
                    print (lista_n [i], end=" ")
                print()
                for i in range (len(lista_a2)):
                    print (lista_a2 [i], end=" ")
                print()
                for i in range (len(lista_b2)):
                    print (lista_b2 [i], end=" ")
                print()
                for i in range (len(lista_c2)):
                    print (lista_c2 [i], end=" ")
                print()
                for i in range (len(lista_d2)):
                    print (lista_d2 [i], end=" ")
                print()
                for i in range (len(lista_e2)):
                    print (lista_e2 [i], end=" ")
                print()
                for i in range (len(lista_f2)):
                    print (lista_f2 [i], end=" ")
                print()
                for i in range (len(lista_g2)):
                    print (lista_g2 [i], end=" ")
                print()
                for i in range (len(lista_h2)):
                    print (lista_h2 [i], end=" ")
                print()
                for i in range (len(lista_i2)):
                    print (lista_i2 [i], end=" ")
                print()
                print()


            lista_c[x]="*"

        elif y =="D" or y=="d":
            t=y.upper()
            y=lista_d
            if lista_d[x]=="O":
                lista_p.append (str(t)+str(x))
                print ("Has dado en el blanco, uno menos!")
                b=b-1
                print ("Te quedan "  +str(b)+ " barcos.")
                z=z+1
                contador += 1
                print ("Llevas " + str(contador) + " intentos")
                print ("Coordenadas de barcos destruidos " + str(lista_p) )
                print ("Historial de disparos fallidos: " + str(lista_historial))
                lista_d2[x] = (Fore.RED+"O")
                
                for i in range (len(lista_n)):
                    print (lista_n [i], end=" ")
                print()
                for i in range (len(lista_a2)):
                    print (lista_a2 [i], end=" ")
                print()
                for i in range (len(lista_b2)):
                    print (lista_b2 [i], end=" ")
                print()
                for i in range (len(lista_c2)):
                    print (lista_c2 [i], end=" ")
                print()
                for i in range (len(lista_d2)):
                    print (lista_d2 [i], end=" ")
                print()
                for i in range (len(lista_e2)):
                    print (lista_e2 [i], end=" ")
                print()
                for i in range (len(lista_f2)):
                    print (lista_f2 [i], end=" ")
                print()
                for i in range (len(lista_g2)):
                    print (lista_g2 [i], end=" ")
                print()
                for i in range (len(lista_h2)):
                    print (lista_h2 [i], end=" ")
                print()
                for i in range (len(lista_i2)):
                    print (lista_i2 [i], end=" ")
                print()
                print()

                
            if lista_d[x]!="O":
                lista_historial.append (str(t)+str(x))
                print ("Mala suerte, sigue probando suerte!")
                z=z+1
                print ("Te quedan "  +str(b)+ " barcos.")
                contador += 1
                print ("Llevas " + str(contador) + " intentos")
                print ("Coordenadas de barcos destruidos " + str(lista_p) )
                print ("Historial de disparos fallidos: " + str(lista_historial))
                lista_d2[x] = (Fore.BLUE+"~")
                for i in range (len(lista_n)):
                    print (lista_n [i], end=" ")
                print()
                for i in range (len(lista_a2)):
                    print (lista_a2 [i], end=" ")
                print()
                for i in range (len(lista_b2)):
                    print (lista_b2 [i], end=" ")
                print()
                for i in range (len(lista_c2)):
                    print (lista_c2 [i], end=" ")
                print()
                for i in range (len(lista_d2)):
                    print (lista_d2 [i], end=" ")
                print()
                for i in range (len(lista_e2)):
                    print (lista_e2 [i], end=" ")
                print()
                for i in range (len(lista_f2)):
                    print (lista_f2 [i], end=" ")
                print()
                for i in range (len(lista_g2)):
                    print (lista_g2 [i], end=" ")
                print()
                for i in range (len(lista_h2)):
                    print (lista_h2 [i], end=" ")
                print()
                for i in range (len(lista_i2)):
                    print (lista_i2 [i], end=" ")
                print()
                print()

            lista_d[x]="*"

        elif y== "E" or y=="e":
            t=y.upper()
            y=lista_e
            if lista_e[x]=="O":
                lista_p.append (str(t)+str(x))
                print ("Has dado en el blanco, uno menos!")
                b=b-1
                print ("Te quedan "  +str(b)+ " barcos.")
                z=z+1
                contador += 1
                print ("Llevas " + str(contador) + " intentos")
                print ("Coordenadas de barcos destruidos " + str(lista_p) )
                print ("Historial de disparos fallidos: " + str(lista_historial))
                lista_e2[x] = (Fore.RED+"O")
                for i in range (len(lista_n)):
                    print (lista_n [i], end=" ")
                print()
                for i in range (len(lista_a2)):
                    print (lista_a2 [i], end=" ")
                print()
                for i in range (len(lista_b2)):
                    print (lista_b2 [i], end=" ")
                print()
                for i in range (len(lista_c2)):
                    print (lista_c2 [i], end=" ")
                print()
                for i in range (len(lista_d2)):
                    print (lista_d2 [i], end=" ")
                print()
                for i in range (len(lista_e2)):
                    print (lista_e2 [i], end=" ")
                print()
                for i in range (len(lista_f2)):
                    print (lista_f2 [i], end=" ")
                print()
                for i in range (len(lista_g2)):
                    print (lista_g2 [i], end=" ")
                print()
                for i in range (len(lista_h2)):
                    print (lista_h2 [i], end=" ")
                print()
                for i in range (len(lista_i2)):
                    print (lista_i2 [i], end=" ")
                print()
                print()

                
            if lista_e[x]!="O":
                lista_historial.append (str(t)+str(x))
                print ("Mala suerte, sigue probando suerte!")
                z=z+1
                print ("Te quedan "  +str(b)+ " barcos.")
                contador += 1
                print ("Llevas " + str(contador) + " intentos")
                print ("Coordenadas de barcos destruidos " + str(lista_p) )
                print ("Historial de disparos fallidos: " + str(lista_historial))
                lista_e2[x] = (Fore.BLUE+"~")
                for i in range (len(lista_n)):
                    print (lista_n [i], end=" ")
                print()
                for i in range (len(lista_a2)):
                    print (lista_a2 [i], end=" ")
                print()
                for i in range (len(lista_b2)):
                    print (lista_b2 [i], end=" ")
                print()
                for i in range (len(lista_c2)):
                    print (lista_c2 [i], end=" ")
                print()
                for i in range (len(lista_d2)):
                    print (lista_d2 [i], end=" ")
                print()
                for i in range (len(lista_e2)):
                    print (lista_e2 [i], end=" ")
                print()
                for i in range (len(lista_f2)):
                    print (lista_f2 [i], end=" ")
                print()
                for i in range (len(lista_g2)):
                    print (lista_g2 [i], end=" ")
                print()
                for i in range (len(lista_h2)):
                    print (lista_h2 [i], end=" ")
                print()
                for i in range (len(lista_i2)):
                    print (lista_i2 [i], end=" ")
                print()
                print()
        


            lista_e[x]="*"

        elif y== "F" or y=="f":
            t=y.upper()
            y=lista_f
            if lista_f[x]=="O":
                lista_p.append (str(t)+str(x))
                print ("Has dado en el blanco, uno menos!")
                b=b-1
                print ("Te quedan "  +str(b)+ " barcos.")
                z=z+1
                contador += 1
                print ("Llevas " + str(contador) + " intentos")
                print ("Coordenadas de barcos destruidos " + str(lista_p) )
                print ("Historial de disparos fallidos: " + str(lista_historial))
                lista_f2[x] = (Fore.RED+"O")
                for i in range (len(lista_n)):
                    print (lista_n [i], end=" ")
                print()
                for i in range (len(lista_a2)):
                    print (lista_a2 [i], end=" ")
                print()
                for i in range (len(lista_b2)):
                    print (lista_b2 [i], end=" ")
                print()
                for i in range (len(lista_c2)):
                    print (lista_c2 [i], end=" ")
                print()
                for i in range (len(lista_d2)):
                    print (lista_d2 [i], end=" ")
                print()
                for i in range (len(lista_e2)):
                    print (lista_e2 [i], end=" ")
                print()
                for i in range (len(lista_f2)):
                    print (lista_f2 [i], end=" ")
                print()
                for i in range (len(lista_g2)):
                    print (lista_g2 [i], end=" ")
                print()
                for i in range (len(lista_h2)):
                    print (lista_h2 [i], end=" ")
                print()
                for i in range (len(lista_i2)):
                    print (lista_i2 [i], end=" ")
                print()
                print()

                
            if lista_f[x]!="O":
                lista_historial.append (str(t)+str(x))
                print ("Mala suerte, sigue probando suerte!")
                z=z+1
                print ("Te quedan "  +str(b)+ " barcos.")
                contador += 1
                print ("Llevas " + str(contador) + " intentos")
                print ("Coordenadas de barcos destruidos " + str(lista_p) )
                print ("Historial de disparos fallidos: " + str(lista_historial))
                lista_f2[x] = (Fore.BLUE+"~")
                for i in range (len(lista_n)):
                    print (lista_n [i], end=" ")
                print()
                for i in range (len(lista_a2)):
                    print (lista_a2 [i], end=" ")
                print()
                for i in range (len(lista_b2)):
                    print (lista_b2 [i], end=" ")
                print()
                for i in range (len(lista_c2)):
                    print (lista_c2 [i], end=" ")
                print()
                for i in range (len(lista_d2)):
                    print (lista_d2 [i], end=" ")
                print()
                for i in range (len(lista_e2)):
                    print (lista_e2 [i], end=" ")
                print()
                for i in range (len(lista_f2)):
                    print (lista_f2 [i], end=" ")
                print()
                for i in range (len(lista_g2)):
                    print (lista_g2 [i], end=" ")
                print()
                for i in range (len(lista_h2)):
                    print (lista_h2 [i], end=" ")
                print()
                for i in range (len(lista_i2)):
                    print (lista_i2 [i], end=" ")
                print()
                print()

            lista_f[x]="*"

        elif y=="G" or y=="g":
            t=y.upper()
            y=lista_g
            if lista_g[x]=="O":
                lista_p.append (str(t)+str(x))
                print ("Has dado en el blanco, uno menos!")
                b=b-1
                print ("Te quedan "  +str(b)+ " barcos.")
                z=z+1
                contador += 1
                print ("Llevas " + str(contador) + " intentos")
                print ("Coordenadas de barcos destruidos " + str(lista_p) )
                print ("Historial de disparos fallidos: " + str(lista_historial))
                lista_g2[x] = (Fore.RED+"O")
                for i in range (len(lista_n)):
                    print (lista_n [i], end=" ")
                print()
                for i in range (len(lista_a2)):
                    print (lista_a2 [i], end=" ")
                print()
                for i in range (len(lista_b2)):
                    print (lista_b2 [i], end=" ")
                print()
                for i in range (len(lista_c2)):
                    print (lista_c2 [i], end=" ")
                print()
                for i in range (len(lista_d2)):
                    print (lista_d2 [i], end=" ")
                print()
                for i in range (len(lista_e2)):
                    print (lista_e2 [i], end=" ")
                print()
                for i in range (len(lista_f2)):
                    print (lista_f2 [i], end=" ")
                print()
                for i in range (len(lista_g2)):
                    print (lista_g2 [i], end=" ")
                print()
                for i in range (len(lista_h2)):
                    print (lista_h2 [i], end=" ")
                print()
                for i in range (len(lista_i2)):
                    print (lista_i2 [i], end=" ")
                print()
                print()

                
            if lista_g[x]!="O":
                lista_historial.append (str(t)+str(x))
                print ("Mala suerte, sigue probando suerte!")
                z=z+1
                print ("Te quedan "  +str(b)+ " barcos.")
                contador += 1
                print ("Llevas " + str(contador) + " intentos")
                print ("Coordenadas de barcos destruidos " + str(lista_p) )
                print ("Historial de disparos fallidos: " + str(lista_historial))
                lista_a2[x] = (Fore.BLUE+"~")
                for i in range (len(lista_n)):
                    print (lista_n [i], end=" ")
                print()
                for i in range (len(lista_a2)):
                    print (lista_a2 [i], end=" ")
                print()
                for i in range (len(lista_b2)):
                    print (lista_b2 [i], end=" ")
                print()
                for i in range (len(lista_c2)):
                    print (lista_c2 [i], end=" ")
                print()
                for i in range (len(lista_d2)):
                    print (lista_d2 [i], end=" ")
                print()
                for i in range (len(lista_e2)):
                    print (lista_e2 [i], end=" ")
                print()
                for i in range (len(lista_f2)):
                    print (lista_f2 [i], end=" ")
                print()
                for i in range (len(lista_g2)):
                    print (lista_g2 [i], end=" ")
                print()
                for i in range (len(lista_h2)):
                    print (lista_h2 [i], end=" ")
                print()
                for i in range (len(lista_i2)):
                    print (lista_i2 [i], end=" ")
                print()
                print()

            lista_g[x]="*"

        elif y=="H" or y=="h":
            t=y.upper()
            y=lista_h
            if lista_h[x]=="O":
                lista_p.append (str(t)+str(x))
                print ("Has dado en el blanco, uno menos!")
                b=b-1
                print ("Te quedan "  +str(b)+ " barcos.")
                z=z+1
                contador += 1
                print ("Llevas " + str(contador) + " intentos")
                print ("Coordenadas de barcos destruidos " + str(lista_p) )
                print ("Historial de disparos fallidos: " + str(lista_historial))
                lista_h2[x] = (Fore.RED+"O")
                for i in range (len(lista_n)):
                    print (lista_n [i], end=" ")
                print()
                for i in range (len(lista_a2)):
                    print (lista_a2 [i], end=" ")
                print()
                for i in range (len(lista_b2)):
                    print (lista_b2 [i], end=" ")
                print()
                for i in range (len(lista_c2)):
                    print (lista_c2 [i], end=" ")
                print()
                for i in range (len(lista_d2)):
                    print (lista_d2 [i], end=" ")
                print()
                for i in range (len(lista_e2)):
                    print (lista_e2 [i], end=" ")
                print()
                for i in range (len(lista_f2)):
                    print (lista_f2 [i], end=" ")
                print()
                for i in range (len(lista_g2)):
                    print (lista_g2 [i], end=" ")
                print()
                for i in range (len(lista_h2)):
                    print (lista_h2 [i], end=" ")
                print()
                for i in range (len(lista_i2)):
                    print (lista_i2 [i], end=" ")
                print()
                print()

                
            if lista_h[x]!="O":
                lista_historial.append (str(t)+str(x))
                print ("Mala suerte, sigue probando suerte!")
                z=z+1
                print ("Te quedan "  +str(b)+ " barcos.")
                contador += 1
                print ("Llevas " + str(contador) + " intentos")
                print ("Coordenadas de barcos destruidos " + str(lista_p) )
                print ("Historial de disparos fallidos: " + str(lista_historial))
                lista_h2[x] = (Fore.BLUE+"~")
                for i in range (len(lista_n)):
                    print (lista_n [i], end=" ")
                print()
                for i in range (len(lista_a2)):
                    print (lista_a2 [i], end=" ")
                print()
                for i in range (len(lista_b2)):
                    print (lista_b2 [i], end=" ")
                print()
                for i in range (len(lista_c2)):
                    print (lista_c2 [i], end=" ")
                print()
                for i in range (len(lista_d2)):
                    print (lista_d2 [i], end=" ")
                print()
                for i in range (len(lista_e2)):
                    print (lista_e2 [i], end=" ")
                print()
                for i in range (len(lista_f2)):
                    print (lista_f2 [i], end=" ")
                print()
                for i in range (len(lista_g2)):
                    print (lista_g2 [i], end=" ")
                print()
                for i in range (len(lista_h2)):
                    print (lista_h2 [i], end=" ")
                print()
                for i in range (len(lista_i2)):
                    print (lista_i2 [i], end=" ")
                print()
                print()

            lista_h[x]="*"

        elif y=="I" or y=="i":
            t=y.upper()
            y=lista_i
            if lista_i[x]=="O":
                lista_p.append (str(t)+str(x))
                print ("Has dado en el blanco, uno menos!")
                b=b-1
                print ("Te quedan "  +str(b)+ " barcos.")
                z=z+1
                contador += 1
                print ("Llevas " + str(contador) + " intentos")
                print ("Coordenadas de barcos destruidos " + str(lista_p) )
                print ("Historial de disparos fallidos: " + str(lista_historial))
                lista_i2[x] = (Fore.RED+"O")
                for i in range (len(lista_n)):
                    print (lista_n [i], end=" ")
                print()
                for i in range (len(lista_a2)):
                    print (lista_a2 [i], end=" ")
                print()
                for i in range (len(lista_b2)):
                    print (lista_b2 [i], end=" ")
                print()
                for i in range (len(lista_c2)):
                    print (lista_c2 [i], end=" ")
                print()
                for i in range (len(lista_d2)):
                    print (lista_d2 [i], end=" ")
                print()
                for i in range (len(lista_e2)):
                    print (lista_e2 [i], end=" ")
                print()
                for i in range (len(lista_f2)):
                    print (lista_f2 [i], end=" ")
                print()
                for i in range (len(lista_g2)):
                    print (lista_g2 [i], end=" ")
                print()
                for i in range (len(lista_h2)):
                    print (lista_h2 [i], end=" ")
                print()
                for i in range (len(lista_i2)):
                    print (lista_i2 [i], end=" ")
                print()
                print()

                
            if lista_i[x]!="O":
                lista_historial.append (str(t)+str(x))
                print ("Mala suerte, sigue probando suerte!")
                z=z+1
                print ("Te quedan "  +str(b)+ " barcos.")
                contador += 1
                print ("Llevas " + str(contador) + " intentos")
                print ("Coordenadas de barcos destruidos " + str(lista_p) )
                print ("Historial de disparos fallidos: " + str(lista_historial))
                lista_i2[x] = (Fore.BLUE+"~")
                for i in range (len(lista_n)):
                    print (lista_n [i], end=" ")
                print()
                for i in range (len(lista_a2)):
                    print (lista_a2 [i], end=" ")
                print()
                for i in range (len(lista_b2)):
                    print (lista_b2 [i], end=" ")
                print()
                for i in range (len(lista_c2)):
                    print (lista_c2 [i], end=" ")
                print()
                for i in range (len(lista_d2)):
                    print (lista_d2 [i], end=" ")
                print()
                for i in range (len(lista_e2)):
                    print (lista_e2 [i], end=" ")
                print()
                for i in range (len(lista_f2)):
                    print (lista_f2 [i], end=" ")
                print()
                for i in range (len(lista_g2)):
                    print (lista_g2 [i], end=" ")
                print()
                for i in range (len(lista_h2)):
                    print (lista_h2 [i], end=" ")
                print()
                for i in range (len(lista_i2)):
                    print (lista_i2 [i], end=" ")
                print()
                print()

            lista_i[x]="*"

        else:
            y= str(input ("Escribe una letra de la A a la I:"))
            x= int(input ("Escribe un número del 1 al 9:"))
        
            os.system ("clear")

while b ==0:
    print ("Has destruido todos los barcos.")
    break



