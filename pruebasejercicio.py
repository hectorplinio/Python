semaforo=True
import os
import time
from datetime import date
from datetime import datetime
from datetime import timedelta
from tkinter import *
import tkinter
class Producto:
    def __init__(self, codigo, nombre, precio, descuento, stock):
        self.codigo=codigo
        self.nombre=nombre
        self.precio=precio
        self.descuento=descuento
        self.stock=stock
        self.fecha_caducidad=fecha_caducidad
        self.seccion=seccion
        
    def listado(self):
        os.system("clear")
        archivo= open("/media/HECTORNAVARRO/D0A5-EB0D/DAW/programacion/Segunda/Almacen.txt","r")
        #archivo=open("D:\DAW\programacion\Segunda\Almacen.txt","r")
        print("Has selecidado el listado, empecemos.")
        for linea in archivo:
            linea=linea.strip("\n")
            print(linea)
        time.sleep(2)
        
    def borrar(self):
        os.system("clear")
        archivo= open("/media/HECTORNAVARRO/D0A5-EB0D/DAW/programacion/Segunda/Almacen.txt","r+")
        #archivo=open("D:\DAW\programacion\Segunda\Almacen.txt","r+")
        print("Has seleccionado borrar un producto, empecemos.")
        bor=input("Dime el nombre que quieres borrar: ")
        bor=bor.capitalize()
        listas=[]
        for lineas in archivo:
            lineas=lineas.strip("\n")
            lineas=lineas.split(";")

            if lineas[1] == bor :
                pass 
            else:
                listas.append(lineas)

        archivo.close()
        archivo= open("/media/HECTORNAVARRO/D0A5-EB0D/DAW/programacion/Segunda/Almacen.txt","w")
        #archivo=open("D:\DAW\programacion\Segunda\Almacen.txt","w")
        for i in listas:
            for y in i:
                if y == i[6]:
                    archivo.write(y)
                else:
                    archivo.write(y+";")
            archivo.write("\n")
        archivo.close()
                
        time.sleep(2)

    def modificar(self):
        os.system("clear")
        archivo= open("/media/HECTORNAVARRO/D0A5-EB0D/DAW/programacion/Segunda/Almacen.txt","r+")
        #archivo=open("D:\DAW\programacion\Segunda\Almacen.txt","r+")
        print("Has seleccionado borrar un producto, empecemos.")
        mod=input("Dime el nombre que quieres modificar: ")
        pre=input("Diga el nuevo precio: ")
        mod=mod.capitalize()
        listas=[]
        for lineas in archivo:
            lineas=lineas.strip("\n")
            lineas=lineas.split(";")
            

            if lineas[1] == mod :
                lineas[2] = pre
                listas.append(lineas)
            else:
                listas.append(lineas)

        archivo.close()
        archivo= open("/media/HECTORNAVARRO/D0A5-EB0D/DAW/programacion/Segunda/Almacen.txt","w")
        #archivo=open("D:\DAW\programacion\Segunda\Almacen.txt","w")
        for i in listas:
            for y in i:
                if y == i[4]:
                    archivo.write(y)
                else:
                    archivo.write(y+";")
            archivo.write("\n")
        archivo.close()
                
        time.sleep(2)
    
    def buscador(self):
        global semaforo
        os.system("clear")
        print("Has seleccionado el buscador, puedes buscar por estos terminos: ")
        for i in lista_buscador:
            print(i)
        busq=input("Selecciona la opcion de busqueda: ")
        if busq == "1":
            archivo= open("/media/HECTORNAVARRO/D0A5-EB0D/DAW/programacion/Segunda/Almacen.txt","r")
            #archivo=open("D:\DAW\programacion\Segunda\Almacen.txt","r")
            cod=input("Ponga el codigo que quieras buscar: ")
            for lineas in archivo:
                lista_b=[]
                lineas=lineas.strip("\n")
                lineas=lineas.split(";")
                if lineas[0] == cod:
                    for i in lineas:
                        lista_b.append(i)
                    print(lista_b[0]+";"+lista_b[1]+";"+lista_b[2]+";"+lista_b[3]+";"+lista_b[4]+";"+lista_b[5]+";"+lista_b[6]+";")
                else:
                    pass
            time.sleep(2)
        if busq == "2":
            archivo= open("/media/HECTORNAVARRO/D0A5-EB0D/DAW/programacion/Segunda/Almacen.txt","r")
            #archivo=open("D:\DAW\programacion\Segunda\Almacen.txt","r")
            nom=input("Ponga el nombre que quieras buscar: ")
            nom=nom.capitalize()
            for lineas in archivo:
                lista_b=[]
                lineas=lineas.strip("\n")
                lineas=lineas.split(";")
                if lineas[1] == nom:
                    for i in lineas:
                        lista_b.append(i)
                    print(lista_b[0]+";"+lista_b[1]+";"+lista_b[2]+";"+lista_b[3]+";"+lista_b[4]+";"+lista_b[5]+";"+lista_b[6]+";")
                else:
                    pass
            time.sleep(2)
        if busq == "3":
            archivo= open("/media/HECTORNAVARRO/D0A5-EB0D/DAW/programacion/Segunda/Almacen.txt","r")
            #archivo=open("D:\DAW\programacion\Segunda\Almacen.txt","r")
            pre=input("Ponga el precio que quieras buscar: ")
            for lineas in archivo:
                lista_b=[]
                lineas=lineas.strip("\n")
                lineas=lineas.split(";")
                if lineas[2] == pre:
                    for i in lineas:
                        lista_b.append(i)
                    print(lista_b[0]+";"+lista_b[1]+";"+lista_b[2]+";"+lista_b[3]+";"+lista_b[4]+";"+lista_b[5]+";"+lista_b[6]+";")
                else:
                    pass
            time.sleep(2)
        if busq == "4":
            archivo= open("/media/HECTORNAVARRO/D0A5-EB0D/DAW/programacion/Segunda/Almacen.txt","r")
            #archivo=open("D:\DAW\programacion\Segunda\Almacen.txt","r")
            des=input("Ponga el descuento que quieras buscar: ")
            for lineas in archivo:
                lista_b=[]
                lineas=lineas.strip("\n")
                lineas=lineas.split(";")
                if lineas[3] == des:
                    for i in lineas:
                        lista_b.append(i)
                    print(lista_b[0]+";"+lista_b[1]+";"+lista_b[2]+";"+lista_b[3]+";"+lista_b[4]+";"+lista_b[5]+";"+lista_b[6]+";")
                else:
                    pass
            time.sleep(2)
        if busq == "5":
            archivo= open("/media/HECTORNAVARRO/D0A5-EB0D/DAW/programacion/Segunda/Almacen.txt","r")
            #archivo=open("D:\DAW\programacion\Segunda\Almacen.txt","r")
            sto=input("Ponga el stock que quieras buscar: ")
            for lineas in archivo:
                lista_b=[]
                lineas=lineas.strip("\n")
                lineas=lineas.split(";")
                if lineas[4] == sto:
                    for i in lineas:
                        lista_b.append(i)
                    print(lista_b[0]+";"+lista_b[1]+";"+lista_b[2]+";"+lista_b[3]+";"+lista_b[4]+";"+lista_b[5]+";"+lista_b[6]+";")
                else:
                    pass
            time.sleep(2)
        if busq == "6":
            archivo= open("/media/HECTORNAVARRO/D0A5-EB0D/DAW/programacion/Segunda/Almacen.txt","r")
            #archivo=open("D:\DAW\programacion\Segunda\Almacen.txt","r")
            fecha=input("Ponga la fecha de caducidad que quieras buscar (DD/MM/AAAA): ")
            for lineas in archivo:
                lista_b=[]
                lineas=lineas.strip("\n")
                lineas=lineas.split(";")
                if lineas[5] == fecha:
                    for i in lineas:
                        lista_b.append(i)
                    print(lista_b[0]+";"+lista_b[1]+";"+lista_b[2]+";"+lista_b[3]+";"+lista_b[4]+";"+lista_b[5]+";"+lista_b[6]+";")
                else:
                    pass
            time.sleep(2)
        if busq == "7":
            archivo= open("/media/HECTORNAVARRO/D0A5-EB0D/DAW/programacion/Segunda/Almacen.txt","r")
            #archivo=open("D:\DAW\programacion\Segunda\Almacen.txt","r")
            for i in lista_seccion:
                print(i)
            sec=input("Ponga la seccion que quieras buscar: ")
            if sec == "1":
                sec="Alimentacion"
            elif sec == "2":
                sec="Limpieza"
            elif sec == "3":
                sec="Bebidas"
            elif sec == "4":
                semaforo=False
            for lineas in archivo:
                lista_b=[]
                lineas=lineas.strip("\n")
                lineas=lineas.split(";")
                if lineas[6] == sec:
                    for i in lineas:
                        lista_b.append(i)
                    print(lista_b[0]+";"+lista_b[1]+";"+lista_b[2]+";"+lista_b[3]+";"+lista_b[4]+";"+lista_b[5]+";"+lista_b[6]+";")
                else:
                    pass
            time.sleep(2)

def menu(self):
    global semaforo

    os.system("clear")
    #os.systema("clear")
    for i in lista_menu:
        print(i)
    opcion=int(input("Qué quieres hacer?: "))
    if opcion == 1:
        for i in lista_seccion:
            print(i)
        print("Has selecionado dar de alta, empecemos.")
        familia=int(input("A que seccion pertenece: "))
        if familia == 1:
            a1.alta()
        elif familia == 2:
            l1.alta()
        elif familia == 3:
            b1.alta()
        elif familia == 4:
            semaforo = False
        else:
            familia=input("Esa opcion no es valida, ponga una opcion correcta :")
    elif opcion == 2:
        listado()
    elif opcion == 3:
        p1.borrar()
    elif opcion == 4:
        p1.modificar()
    elif opcion == 5:
        p1.buscador()
    elif opcion == 6:
        semaforo=False
    else:
        input("Esa opcion no es valida, ponga una que esta en la lista: ")


class Alimentacion(Producto):
    def __init__(self, codigo, nombre, precio, descuento, stock, fecha_caducidad):
        Producto.__init__(self,codigo, nombre, precio, descuento, stock)
        self.fecha_caducidad=fecha_caducidad
        

   
class Limpieza(Producto):
    def __init__(self, codigo, nombre, precio, descuento, stock, toxico):
        Producto.__init__(self,codigo, nombre, precio, descuento, stock)
        self.toxico=toxico
    
    def alta(self):
        os.system("clear")
        print("Has selecidado dar de alta un producto de limpieza, empecemos.")
        nom=input("Dime el nombre del producto: ")
        nom=nom.capitalize()
        archivo= open("/media/HECTORNAVARRO/D0A5-EB0D/DAW/programacion/Segunda/Almacen.txt","r")
        #archivo=open("D:\DAW\programacion\Segunda\Almacen.txt","r")
        for lineas in archivo:
            lineas=lineas.strip("\n")
            lineas=lineas.split(";")
            if lineas[1] == nom:
                print("Este articulo ya esta en la lista, cambie el nombre.")
                nom=input("Dime el nombre del producto: ")
                nom=nom.capitalize()
            else:
                pass
        p1.nombre.append(nom)
        cod=input("Dime el código de producto: ")
        archivo= open("/media/HECTORNAVARRO/D0A5-EB0D/DAW/programacion/Segunda/Almacen.txt","r")
        #archivo=open("D:\DAW\programacion\Segunda\Almacen.txt","r")
        for lineas in archivo:
            lineas=lineas.strip("\n")
            lineas=lineas.split(";")
            if lineas[0] == cod:
                print("Este articulo ya esta en la lista, cambie el codigo.")
                cod=input("Dime el codigo del producto: ")
                cod=cod.capitalize()
            else:
                pass
        p1.codigo.append(cod)
        pre=input("Dime el precio del producto: ")
        p1.precio.append(pre)
        des=input("Dime el descuento que tiene: ")
        p1.descuento.append(des)
        sto=input("Dime el numero de productos que hay: ")
        p1.stock.append(sto)
        dia=input("Dime la fecha de caducidad, introduce el dia: ")
        mes=input("Introduce el mes de caducidad: ")
        ano=input("Introduce el año de caducidad: ")
        fecha= dia+"/"+mes+"/"+ano
        p1.fecha_caducidad.append(fecha)
        seccion="Limpieza"
        lista.append(cod+";"+nom+";"+pre+";"+des+";"+sto+";"+fecha+";"+seccion+";")
        frase = cod+";"+nom+";"+pre+";"+des+";"+sto+";"+fecha+";"+seccion+";"
        archivo= open("/media/HECTORNAVARRO/D0A5-EB0D/DAW/programacion/Segunda/Almacen.txt","a")
        #archivo=open("D:\DAW\programacion\Segunda\Almacen.txt","a")
        archivo.write(frase+"\n")
        print("Ha añadido usted el producto "+nom+" con un código "+cod+" a un precio de "+pre+" €, con un dto de "+des+" y un total de unidades de "+sto+" con una fecha de caducidad de "+fecha+" en la seccion de "+seccion)
        time.sleep(2)
        archivo.close()

class Bebidas(Producto):
    def __init__(self, codigo, nombre, precio, descuento, stock, fecha_caducidad, alcohol):
        Producto.__init__(self,codigo, nombre, precio, descuento, stock)
        self.fecha_caducidad=fecha_caducidad
        self.alcohol=alcohol
        
    def alta(self):
        os.system("clear")
        print("Has selecidado dar de alta un producto de bebidas, empecemos.")
        nom=input("Dime el nombre del producto: ")
        nom=nom.capitalize()
        archivo= open("/media/HECTORNAVARRO/D0A5-EB0D/DAW/programacion/Segunda/Almacen.txt","r")
        #archivo=open("D:\DAW\programacion\Segunda\Almacen.txt","r")
        for lineas in archivo:
            lineas=lineas.strip("\n")
            lineas=lineas.split(";")
            if lineas[1] == nom:
                print("Este articulo ya esta en la lista, cambie el nombre.")
                nom=input("Dime el nombre del producto: ")
                nom=nom.capitalize()
            else:
                pass
        p1.nombre.append(nom)
        cod=input("Dime el código de producto: ")
        archivo= open("/media/HECTORNAVARRO/D0A5-EB0D/DAW/programacion/Segunda/Almacen.txt","r")
        #archivo=open("D:\DAW\programacion\Segunda\Almacen.txt","r")
        for lineas in archivo:
            lineas=lineas.strip("\n")
            lineas=lineas.split(";")
            if lineas[0] == cod:
                print("Este articulo ya esta en la lista, cambie el codigo.")
                cod=input("Dime el codigo del producto: ")
                cod=cod.capitalize()
            else:
                pass
        p1.codigo.append(cod)
        pre=input("Dime el precio del producto: ")
        p1.precio.append(pre)
        des=input("Dime el descuento que tiene: ")
        p1.descuento.append(des)
        sto=input("Dime el numero de productos que hay: ")
        p1.stock.append(sto)
        dia=input("Dime la fecha de caducidad, introduce el dia: ")
        mes=input("Introduce el mes de caducidad: ")
        ano=input("Introduce el año de caducidad: ")
        fecha= dia+"/"+mes+"/"+ano
        p1.fecha_caducidad.append(fecha)
        seccion="Bebidas"
        lista.append(cod+";"+nom+";"+pre+";"+des+";"+sto+";"+fecha+";"+seccion+";")
        frase = cod+";"+nom+";"+pre+";"+des+";"+sto+";"+fecha+";"+seccion+";"
        archivo= open("/media/HECTORNAVARRO/D0A5-EB0D/DAW/programacion/Segunda/Almacen.txt","a")
        #archivo=open("D:\DAW\programacion\Segunda\Almacen.txt","a")
        archivo.write(frase+"\n")
        print("Ha añadido usted el producto "+nom+" con un código "+cod+" a un precio de "+pre+" €, con un dto de "+des+" y un total de unidades de "+sto+" con una fecha de caducidad de "+fecha+" en la seccion de "+seccion)
        time.sleep(2)
        archivo.close()

archivo= open("/media/HECTORNAVARRO/D0A5-EB0D/DAW/programacion/Segunda/Almacen.txt","a")
#archivo=open("D:\DAW\programacion\Segunda\Almacen.txt","a")

a1=Alimentacion([],[],[],[],[],[],[])
l1=Limpieza([],[],[],[],[],[],[])
b1=Bebidas([],[],[],[],[],[],[])
lista=[]
listas=[]
lista_b=[]
lista_menu=["Menu Principal", "1- Alta de producto" ,"2- Listado", "3- Borrar producto", "4- Modificar PVP", "5- Buscador", "6- Salir"]
lista_seccion=["1- Alimentacion", "2- Limpieza", "3- Bebidas", "4- Salir"]
lista_buscador=["1- Codigo", "2- Nombre", "3- Precio", "4- Descuento", "5- Stock", "6- Fecha caducidad", "7- Seccion", "8- Salir"]
"""ventana = tkinter.Tk()
ventana.geometry("400x400")
etiqueta = tkinter.Label(ventana, text="Programa de Hector")
etiqueta.pack()
etiqueta.pack(fill= tkinter.X)
boton_codigo=tkinter.Button(ventana, text ="Código")
boton_codigo.pack()
ventana.mainloop()"""

while semaforo==True:
    p1.menu()
archivo.close()