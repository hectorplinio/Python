semaforo=True
import os
import time
class Producto:
    def __init__(self, codigo, nombre, precio, descuento, stock):
        self.codigo=codigo
        self.nombre=nombre
        self.precio=precio
        self.descuento=descuento
        self.stock=stock

    def alta(self):
        
        print("Has selecidado dar de alta, empecemos.")
        nom=input("Dime el nombre del producto: ")
        nom=nom.capitalize()
        archivo=open("D:\DAW\programacion\Segunda\Almacen.txt","r")
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
        archivo=open("D:\DAW\programacion\Segunda\Almacen.txt","r")
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
        lista.append(cod+";"+nom+";"+pre+";"+des+";"+sto+";")
        frase = cod+";"+nom+";"+pre+";"+des+";"+sto
        archivo=open("D:\DAW\programacion\Segunda\Almacen.txt","a")
        archivo.write(frase+"\n")
        print("Ha añadido usted el producto "+nom+" con un código "+cod+" a un precio de "+pre+" €, con un dto de "+des+" y un total de unidades de "+sto)
        time.sleep(2)
        archivo.close()
        
    def listado(self):
        archivo=open("D:\DAW\programacion\Segunda\Almacen.txt","r")
        print("Has selecidado el listado, empecemos.")
        for linea in archivo:
            print(linea)
        time.sleep(2)
        
    def borrar(self):
        
        archivo=open("D:\DAW\programacion\Segunda\Almacen.txt","r+")
        print("Has seleccionado borrar un producto, empecemos.")
        bor=input("Dime el nombre que quieres borrar: ")
        bor=bor.capitalize()
        listas=[]
        for lineas in archivo:
            lineas=lineas.strip("\n")
            lineas=lineas.split(";")

            if lineas[1] == bor :
                pass
            if lineas == "":
                pass   
            else:
                listas.append(lineas)

        archivo.close()
        archivo=open("D:\DAW\programacion\Segunda\Almacen.txt","w")
        for i in listas:
            for y in i:
                if y == i[4]:
                    archivo.write(y)
                else:
                    archivo.write(y+";")
            archivo.write("\n")
        archivo.close()
                
        time.sleep(2)

    def modificar(self):
        archivo=open("D:\DAW\programacion\Segunda\Almacen.txt","r+")
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
        archivo=open("D:\DAW\programacion\Segunda\Almacen.txt","w")
        for i in listas:
            for y in i:
                if y == i[4]:
                    archivo.write(y)
                else:
                    archivo.write(y+";")
            archivo.write("\n")
        archivo.close()
                
        time.sleep(2)
    

    def menu(self):
        global semaforo

        os.system("cls")
        #os.systema("clear")
        for i in lista_menu:
            print(i)
        opcion=int(input("Qué quieres hacer?: "))
        if opcion == 1:
            p1.alta()
        elif opcion == 2:
            p1.listado()
        elif opcion == 3:
            p1.borrar()
        elif opcion == 4:
            p1.modificar()
        elif opcion == 5:
            semaforo=False
        else:
            input("Esa opcion no es valida, ponga una que esta en la lista: ")


"""class Alimentacion(Producto):

class Limpieza(Producto):

class Bebidas(Producto):"""

#archivo= open("/media/HECTORNAVARRO/D0A5-EB0D/DAW/programacion/Segunda/Almacen.txt","a")
archivo=open("D:\DAW\programacion\Segunda\Almacen.txt","a")
nom=0
p1=Producto([],[],[],[],[])
lista=[]
listas=[]
lista_menu=["Menu Principal", "1- Alta de producto" ,"2- Listado", "3- Borrar producto", "4- Modificar PVP", "5- Salir"]
while semaforo==True:
    p1.menu()
archivo.close()