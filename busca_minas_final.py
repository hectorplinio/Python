import random
import time
import os
from colorama import init,Fore
init(autoreset=True)

num_minas_click = 0

num_minas_totales = 0

bucle_principal = True

pos_x = 0
pos_y = 0

x = 0
y = 0

lista_mapa_jug = []
lista_mapa = []

#Inicio de la creacion de mapas

#Funcion para aber las dimensiones de nuestro mapa
def dimesiones():
    global x
    global y
    bucle_respuesta = True
    while bucle_respuesta == True:

        print("\"Principiante = 1\" \"Avanzado = 2\" \"Experto = 3\" \"Personalizado = 4\"")
        respuesta = input("Que tipo de mapa quieres jugar? ")
                
        if respuesta == "1":
            print("Has elegido el modo Principiante (8x8)")   
            x = 8
            y = 8    
            bucle_respuesta = False
            time.sleep(1)
        elif respuesta == "2":
            print("Has elegido el modo Avanzado (16x16)")
            x = 16
            y = 16
            bucle_respuesta = False
            time.sleep(1)
        elif respuesta == "3":
            print("Has elegido el modo Experto (16x30)")
            x = 16
            y = 30
            bucle_respuesta = False
            time.sleep(1)
        elif respuesta == "4":
            print("Has elegido el modo Personalizado")

            bucle_x = True
            bucle_y = True

            while bucle_x == True:
                try:
                    x = int(input("x: "))
                    if x >= x:
                        bucle_x = False
                    else:
                        print("Te has equivocado")
                except:
                    print("Te has equivocado")
            while bucle_y == True:
                try:
                    y = int(input("y: "))
                    if y >= y:
                        bucle_y = False
                    else:
                        print("Te has equivocado")
                except:
                    print("Te has equivocado")

                print("(", x, "x", y, ")")
                bucle_respuesta = False
                time.sleep(1)
        else:
            print("Te has equivocado.")
            time.sleep(1)

dimesiones()

#Para crear el mapa que el jugador va a ver y modificar

for i in range(x+2):
    lista_mapa_jug.append([str(i)])
    for j in range(y+1):
        if i == (x+1):
            lista_mapa_jug[i].append(" ")
        elif i == 0:
            lista_mapa_jug[i].append(str(j+1))
        else:
            lista_mapa_jug[i].append(Fore.BLUE+"■")

for i in range(x+2):
    lista_mapa_jug[i].append(" ")

#Para crear el mapa con las bombas

for i in range(x+2):
    lista_mapa.append([str(i)])
    for j in range(y+1):
        if i == (x+1):
            lista_mapa[i].append(" ")
        elif i == 0:
            lista_mapa[i].append(str(j+1))
        else:
            num_al = random.randint(1,5)
            if num_al == 1:
                lista_mapa[i].append("¤")
            else:
                lista_mapa[i].append(0)

for i in range(x+2):
    lista_mapa[i].append(" ")
#Final de la creacion de mapas

#Funcion para indicar las coordenadas que queramos
def coordenadas_dadas_usuario():
    global num_minas_click

    global pos_x
    global pos_y

    bucle_x = True
    bucle_y = True

    num_minas_click = 0
    print("Dime la posicion")
    while bucle_x == True:
        try:
            pos_x = int(input("x: "))
            if x >= pos_x:
                bucle_x = False
            else:
                print("Te has equivocado")
        except:
            print("Te has equivocado")
    while bucle_y == True:
        try:
            pos_y = int(input("y: "))
            if y >= pos_y:
                bucle_y = False
            else:
                print("Te has equivocado")
        except:
            print("Te has equivocado")


def comprobacion_bombas(y_pos, x_pos, incognita):

    global lista_mapa
    global lista_mapa_jug

    if lista_mapa[y_pos][x_pos] == incognita:
        try:
            if incognita == "¤":
                lista_mapa[y_pos][x_pos-1] += 1
        except:
            pass
        try:
            if incognita == "¤":
                lista_mapa[y_pos+1][x_pos-1] += 1
        except:
            pass
        try:
            if incognita == "¤":
                lista_mapa[y_pos-1][x_pos-1] += 1
        except:
            pass
        try:
            if incognita == "¤":
                lista_mapa[y_pos-1][x_pos] += 1
        except:
            pass
        try:
            if incognita == "¤":
                lista_mapa[y_pos+1][x_pos] += 1
        except:
            pass
        try:
            if incognita == "¤":
                lista_mapa[y_pos-1][x_pos+1] += 1
        except:
            pass
        try:
            if incognita == "¤":
                lista_mapa[y_pos][x_pos+1] += 1
        except:
            pass
        try:
            if incognita == "¤":
                lista_mapa[y_pos+1][x_pos+1] += 1
        except:
            pass


for i in range(x+1):
    for j in range(y+1):
        comprobacion_bombas(i, j, "¤")

def funcion_ceros(lista_mapa, lista_mapa_jug, y, x, fil, col, val):

    ceros = [(y,x)]
    while len(ceros) > 0:
        y, x = ceros.pop()
        for i in [-1, 0, 1]:
            for j in [-1, 0, 1]:
                if 0 <= y+i <= fil-1 and 0 <= x+j <= col-1:
                    if lista_mapa_jug[y+i][x+j] == val and lista_mapa[y+i][x+j] == 0:
                        lista_mapa_jug[y+i][x+j] = 0
                        if (y+i, x+j) not in ceros:
                            ceros.append((y+i, x+j))
                            
                    else:
                        lista_mapa_jug[y+i][x+j] = lista_mapa[y+i][x+j]
    
    return lista_mapa_jug

#Funcion para saber si hay una mina en la posicion que le digamos
def click_num_minas_click():
    global num_minas_click

    global pos_x
    global pos_y

    global bucle_principal

    global lista_mapa
    global lista_mapa_jug

    coordenadas_dadas_usuario()
    if lista_mapa[pos_y][pos_x] == "¤":
        lista_mapa_jug[pos_y][pos_x] ="B"
        bucle_principal = False
    if lista_mapa[pos_y][pos_x] == 0:
        lista_mapa_jug = funcion_ceros(lista_mapa, lista_mapa_jug, pos_y, pos_x, (y+1), (x+1), "■")

    else:    
        lista_mapa_jug[pos_y][pos_x] = lista_mapa[pos_y][pos_x]

#Funcion para imprimir el mapa que el jugador va a ver
def imprimir_mapa_jug():
    for l in range(x+1):
        for f in range(y+1):
            if l > 9 and f == 0:
                print(lista_mapa_jug[l][f], end=" ")
            elif f > 9 and l != 0:
                print(lista_mapa_jug[l][f], end="   ")
            else:
                print(lista_mapa_jug[l][f], end="  ")
        print()

#Funcion para imprimir el mapa sobre el que vamos ha operar
def imprimir_mapa():
    for l in range(x+1):
        for f in range(y+1):
            if l > 9 and f == 0:
                print(lista_mapa[l][f], end=" ")
            elif f > 9 and l != 0:
                print(lista_mapa[l][f], end="   ")
            else:
                print(lista_mapa[l][f], end="  ")
        print()

imprimir_mapa_jug()
while bucle_principal == True:
    click_num_minas_click()
    os.system("cls")
    imprimir_mapa_jug()
    print(imprimir_mapa)
print("El juego ha acabado")