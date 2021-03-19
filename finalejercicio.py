import os
import time
class Producto:
    def __init__(self, codigo, nombre, precio, descuento, stock):
        self.codigo=codigo
        self.nombre=nombre
        self.precio=precio
        self.descuento=descuento
        self.stock=stock
    
    def alta (self):
        cod = input("Dime el codigo del producto: ")
        archivo = open("Almacen.txt","r")
        for lineas in archivo:
            lineas=lineas.strip("\n")
            lineas=lineas.split(";")
            if lineas[0] == cod:
                print("Este articulo ya esta en la lista, cambie el codigo.")
                cod=input("Dime el codigo del producto: ")
        self.codigo.append(cod)
        nom = input("Dime el nombre del producto: ")
        for lineas in archivo:
            lineas=lineas.strip("\n")
            lineas=lineas.split(";")
            if lineas[1] == nom:
                print("Este articulo ya esta en la lista, cambie el nombre.")
                nom=input("Dime el nombre del producto: ")
        nom=nom.capitalize()
        self.nombre.append(nom)
        self.precio.append(input("Dime el precio: "))
        self.descuento.append(input("Dime el descuento: "))
        self.stock.append(input("Dime el stock: "))
        archivo.close()
    
    

    
class Alimentacion(Producto):
    def __init__(self, codigo, nombre, precio, descuento, stock, fecha_caducidad):
        Producto.__init__(self,codigo, nombre, precio, descuento, stock)
        self.fecha_caducidad=fecha_caducidad

    def alta_alimento(self):
        archivo = open("Almacen.txt","a")
        print("Vas a dar de alta un alimento.")
        Producto.alta(self)
        self.fecha_caducidad.append(input("Dime la fecha: (DD/MM/AAAA)"))
        frase=self.codigo[-1]+";"+self.nombre[-1]+";"+self.precio[-1]+";"+self.descuento[-1]+";"+self.stock[-1]+";"+self.fecha_caducidad[-1]+";Alimento"
        archivo.write(frase+"\n")
        print("Ha añadido usted el producto "+self.nombre[-1]+" con un código "+self.codigo[-1]+" a un precio de "+self.precio[-1]+" €, con un dto de "+self.descuento[-1]+" y un total de unidades de "+self.stock[-1]+" con una fecha de caducidad de "+self.fecha_caducidad[-1])
        
        archivo.close()
    
    def listado_alimento(self):
        
        print("Codigo;Nombre;Precio;Descuento;Stock;Fecha_Caducidad")
        for i in range(len(self.codigo)):
            print(self.codigo[i]+";"+self.nombre[i]+";"+self.precio[i]+";"+self.descuento[i]+";"+self.stock[i]+";"+self.fecha_caducidad[i])

    def borrar_alimento (self):
        contador=0
        bor = input("Que nombre quieres borrar?:")
        bor=bor.capitalize()
        for i in self.nombre:
            if i == bor:
                self.codigo.pop(contador)
                self.nombre.pop(contador)
                self.precio.pop(contador)
                self.descuento.pop(contador)
                self.stock.pop(contador)
                self.fecha_caducidad.pop(contador)
            contador+=1

    def modificar_alimento(self):
        contador=0
        semaforo_modificar=True
        
        while semaforo_modificar == True:
            for i in lista_buscador:
                print(i)
            modificar = int(input("Que quieres cambiar?:"))
            if modificar == 1:
                cod= input("Dime el codigo del producto: ")
                cod2= input("Dime el nuevo codigo:")
                for i in self.codigo:
                    if i == cod:
                        self.codigo[contador]=cod2
                        semaforo_modificar=False
                    contador+=1
            elif modificar == 2:
                nom= input("Dime el nombre del producto: ")
                nom=nom.capitalize()
                nom2= input("Dime el nuevo nombre:")
                nom2=nom2.capitalize()
                for i in self.nombre:
                    if i == nom:
                        self.nombre[contador]=nom2
                        semaforo_modificar=False
                    contador+=1
            elif modificar == 3:
                nom= input("Dime el nombre del producto: ")
                nom=nom.capitalize()
                pre2= input("Dime el precio nuevo:")
                for i in self.nombre:
                    if i == nom:
                        self.precio[contador]=pre2
                        semaforo_modificar=False
                    contador+=1
            elif modificar == 4:
                nom= input("Dime el nombre del producto: ")
                nom=nom.capitalize()
                dto= input("Dime el nuevo descuento:")
                for i in self.nombre:
                    if i == nom:
                        self.descuento[contador]=dto
                        semaforo_modificar=False
                    contador+=1
            elif modificar == 5:
                nom= input("Dime el nombre del producto: ")
                nom=nom.capitalize()
                sto= input("Dime el stock nuevo:")
                for i in self.nombre:
                    if i == nom:
                        self.stock[contador]=sto
                        semaforo_modificar=False
                    contador+=1
            elif modificar == 6:
                nom= input("Dime el nombre del producto: ")
                nom=nom.capitalize()
                fecha= input("Dime la nueva fecha de caducidad:")
                for i in self.nombre:
                    if i == nom:
                        self.fecha_caducidad[contador]=fecha
                        semaforo_modificar=False
                    contador+=1
            elif modificar == 8:
                semaforo_modificar=False
            else:
                modificar=input("Esa opcion no es valida, ponga una opcion correcta :")

        semaforo_modificar=False

    def buscar_alimento(self):
        contador=0
        semaforo_buscar=True
        for i in lista_buscador:
            print(i)
        buscar = int(input("Que quieres buscar?:"))
        while semaforo_buscar == True:
            if buscar == 1:
                cod= input("Dime el codigo del producto: ")
                for i in self.codigo:
                    if i == cod:
                        print(self.codigo[contador]+";"+self.nombre[contador]+";"+self.precio[contador]+";"+self.descuento[contador]+";"+self.stock[contador]+";"+self.fecha_caducidad[contador]+";Alimento")
                        time.sleep(4)
                        semaforo_buscar=False
                    contador+=1
            elif buscar == 2:
                nom= input("Dime el nombre del producto: ")
                nom=nom.capitalize()
                for i in self.nombre:
                    if i == nom:
                        print(self.codigo[contador]+";"+self.nombre[contador]+";"+self.precio[contador]+";"+self.descuento[contador]+";"+self.stock[contador]+";"+self.fecha_caducidad[contador]+";Alimento")
                        time.sleep(4)
                        semaforo_buscar=False
                    contador+=1
            elif buscar == 3:
                pre= input("Dime el precio del producto: ")
                for i in self.nombre:
                    if i == pre:
                        print(self.codigo[contador]+";"+self.nombre[contador]+";"+self.precio[contador]+";"+self.descuento[contador]+";"+self.stock[contador]+";"+self.fecha_caducidad[contador]+";Alimento")
                        time.sleep(4)
                        semaforo_buscar=False
                    contador+=1
            elif buscar == 4:
                dto= input("Dime el descuento del producto: ")
                for i in self.nombre:
                    if i == dto:
                        print(self.codigo[contador]+";"+self.nombre[contador]+";"+self.precio[contador]+";"+self.descuento[contador]+";"+self.stock[contador]+";"+self.fecha_caducidad[contador]+";Alimento")
                        time.sleep(4)
                        semaforo_buscar=False
                    contador+=1
            elif buscar == 5:
                sto= input("Dime el stock del producto: ")
                for i in self.nombre:
                    if i == sto:
                        print(self.codigo[contador]+";"+self.nombre[contador]+";"+self.precio[contador]+";"+self.descuento[contador]+";"+self.stock[contador]+";"+self.fecha_caducidad[contador]+";Alimento")
                        time.sleep(4)
                        semaforo_buscar=False
                    contador+=1
            elif buscar == 6:
                fecha= input("Dime el fecha de caducidad del producto: ")
                for i in self.nombre:
                    if i == fecha:
                        print(self.codigo[contador]+";"+self.nombre[contador]+";"+self.precio[contador]+";"+self.descuento[contador]+";"+self.stock[contador]+";"+self.fecha_caducidad[contador]+";Alimento")
                        time.sleep(4)
                        semaforo_buscar=False
                    contador+=1
            elif buscar == 8:
                semaforo_buscar=False
            else:
                buscar=input("Esa opcion no es valida, ponga una opcion correcta :")

class Limpieza(Producto):
    def __init__(self, codigo, nombre, precio, descuento, stock, toxico):
        Producto.__init__(self,codigo, nombre, precio, descuento, stock)
        self.toxico=toxico

    def alta_limpieza(self):
        archivo = open("Almacen.txt","a")
        print("Vas a dar de alta un producto de limpieza.")
        Producto.alta(self)
        self.toxico.append(input("Dime si es toxico: (SI/NO)"))
        frase=self.codigo[-1]+";"+self.nombre[-1]+";"+self.precio[-1]+";"+self.descuento[-1]+";"+self.stock[-1]+";"+self.toxico[-1]+";Limpieza"
        archivo.write(frase+"\n")
        print("Ha añadido usted el producto "+self.nombre[-1]+" con un código "+self.codigo[-1]+" a un precio de "+self.precio[-1]+" €, con un dto de "+self.descuento[-1]+" y un total de unidades de "+self.stock[-1]+" y es toxico ( "+self.toxico[-1]+")")
        time.sleep(2)
        archivo.close()
    
    def listado_limpieza(self):
        print("Codigo;Nombre;Precio;Descuento;Stock;Toxico")
        for i in range(len(self.codigo)):
            print(self.codigo[i]+";"+self.nombre[i]+";"+self.precio[i]+";"+self.descuento[i]+";"+self.stock[i]+";"+self.toxico[i])

    def borrar_limpieza (self):
        contador=0
        bor = input("Que nombre quieres borrar?:")
        bor=bor.capitalize()
        for i in self.nombre:
            if i == bor:
                self.codigo.pop(contador)
                self.nombre.pop(contador)
                self.precio.pop(contador)
                self.descuento.pop(contador)
                self.stock.pop(contador)
                self.fecha_caducidad.pop(contador)
            contador+=1

    def modificar_limpieza(self):
        semaforo_modificar=True
        contador=0
        for i in lista_buscador:
            print(i)
        modificar = int(input("Que quieres cambiar?:"))
        while semaforo_modificar == True:
            if modificar == 1:
                cod= input("Dime el codigo del producto: ")
                cod2= input("Dime el nuevo codigo:")
                for i in self.codigo:
                    if i == cod:
                        self.codigo[contador]=cod2
                        semaforo_modificar=False
                    contador+=1
            elif modificar == 2:
                nom= input("Dime el nombre del producto: ")
                nom=nom.capitalize()
                nom2= input("Dime el nuevo nombre:")
                nom2=nom2.capitalize()
                for i in self.nombre:
                    if i == nom:
                        self.nombre[contador]=nom2
                        semaforo_modificar=False
                    contador+=1
            elif modificar == 3:
                nom= input("Dime el nombre del producto: ")
                nom=nom.capitalize()
                pre2= input("Dime el precio nuevo:")
                for i in self.nombre:
                    if i == nom:
                        self.precio[contador]=pre2
                        semaforo_modificar=False
                    contador+=1
            elif modificar == 4:
                nom= input("Dime el nombre del producto: ")
                nom=nom.capitalize()
                dto= input("Dime el nuevo descuento:")
                for i in self.nombre:
                    if i == cod:
                        self.descuento[contador]=dto
                        semaforo_modificar=False
                    contador+=1
            elif modificar == 5:
                nom= input("Dime el nombre del producto: ")
                nom=nom.capitalize()
                sto= input("Dime el stock nuevo:")
                for i in self.nombre:
                    if i == nom:
                        self.stock[contador]=sto
                        semaforo_modificar=False
                    contador+=1
            elif modificar == 7:
                nom= input("Dime el nombre del producto: ")
                nom=nom.capitalize()
                toxi= input("Dime la nueva toxicidad:")
                for i in self.nombre:
                    if i == cod:
                        self.toxico[contador]=toxi
                        semaforo_modificar=False
                    contador+=1
            elif modificar == 8:
                semaforo_modificar=False
            else:
                modificar=input("Esa opcion no es valida, ponga una opcion correcta :")
        
    def buscar_limpieza(self):
        contador=0
        semaforo_buscar=True
        for i in lista_buscador:
            print(i)
        buscar = int(input("Que quieres buscar?:"))
        while semaforo_buscar == True:
            if buscar == 1:
                cod= input("Dime el codigo del producto: ")
                for i in self.codigo:
                    if i == cod:
                        print(self.codigo[contador]+";"+self.nombre[contador]+";"+self.precio[contador]+";"+self.descuento[contador]+";"+self.stock[contador]+";"+self.toxico[contador]+";Limpieza")
                        time.sleep(4)
                        semaforo_buscar=False
                    contador+=1
            elif buscar == 2:
                nom= input("Dime el nombre del producto: ")
                nom=nom.capitalize()
                for i in self.nombre:
                    if i == nom:
                        print(self.codigo[contador]+";"+self.nombre[contador]+";"+self.precio[contador]+";"+self.descuento[contador]+";"+self.stock[contador]+";"+self.toxico[contador]+";Limpieza")
                        time.sleep(4)
                        semaforo_buscar=False
                    contador+=1
            elif buscar == 3:
                pre= input("Dime el precio del producto: ")
                for i in self.nombre:
                    if i == pre:
                        print(self.codigo[contador]+";"+self.nombre[contador]+";"+self.precio[contador]+";"+self.descuento[contador]+";"+self.stock[contador]+";"+self.toxico[contador]+";Limpieza")
                        time.sleep(4)
                        semaforo_buscar=False
                    contador+=1
            elif buscar == 4:
                dto= input("Dime el descuento del producto: ")
                for i in self.nombre:
                    if i == dto:
                        print(self.codigo[contador]+";"+self.nombre[contador]+";"+self.precio[contador]+";"+self.descuento[contador]+";"+self.stock[contador]+";"+self.toxico[contador]+";Limpieza")
                        time.sleep(4)
                        semaforo_buscar=False
                    contador+=1
            elif buscar == 5:
                sto= input("Dime el stock del producto: ")
                for i in self.nombre:
                    if i == sto:
                        print(self.codigo[contador]+";"+self.nombre[contador]+";"+self.precio[contador]+";"+self.descuento[contador]+";"+self.stock[contador]+";"+self.toxico[contador]+";Limpieza")
                        time.sleep(4)
                        semaforo_buscar=False
                    contador+=1
            elif buscar == 7:
                tox= input("Dime la toxicidad del producto: ")
                for i in self.nombre:
                    if i == tox:
                        print(self.codigo[contador]+";"+self.nombre[contador]+";"+self.precio[contador]+";"+self.descuento[contador]+";"+self.stock[contador]+";"+self.toxico[contador]+";Limpieza")
                        time.sleep(4)
                        semaforo_buscar=False
                    contador+=1
            elif buscar == 8:
                semaforo_buscar=False
            else:
                buscar=input("Esa opcion no es valida, ponga una opcion correcta :")
                

class Bebidas(Producto):
    def __init__(self, codigo, nombre, precio, descuento, stock, fecha_caducidad, alcohol):
        Producto.__init__(self,codigo, nombre, precio, descuento, stock)
        self.fecha_caducidad=fecha_caducidad
        self.alcohol=alcohol
    
    def alta_bebida(self):
        archivo = open("Almacen.txt","a")
        print("Vas a dar de alta una bebida.")
        Producto.alta(self)
        self.fecha_caducidad.append(input("Dime la fecha: (DD/MM/AAAA)"))
        self.alcohol.append(input("Dime si lleva alcohol: (SI/NO)"))
        frase=self.codigo[-1]+";"+self.nombre[-1]+";"+self.precio[-1]+";"+self.descuento[-1]+";"+self.stock[-1]+";"+self.fecha_caducidad[-1]+";"+self.alcohol[-1]+";Bebida"
        archivo.write(frase+"\n")
        print("Ha añadido usted el producto "+self.nombre[-1]+" con un código "+self.codigo[-1]+" a un precio de "+self.precio[-1]+" €, con un dto de "+self.descuento[-1]+" y un total de unidades de "+self.stock[-1]+" con una fecha de caducidad de "+self.fecha_caducidad[-1]+"y lleva alcohol ("+self.alcohol[-1]+").")
        time.sleep(2)
        archivo.close()

    def listado_bebida(self):
        print("Codigo;Nombre;Precio;Descuento;Stock;Fecha_Caducidad;Alcohol")
        for i in range(len(self.codigo)):
            print(self.codigo[i]+";"+self.nombre[i]+";"+self.precio[i]+";"+self.descuento[i]+";"+self.stock[i]+";"+self.fecha_caducidad[i]+";"+self.alcohol[i])

    def borrar_bebida (self):
        contador=0
        bor = input("Que nombre quieres borrar?:")
        bor=bor.capitalize()
        for i in self.nombre:
            if i == bor:
                self.codigo.pop(contador)
                self.nombre.pop(contador)
                self.precio.pop(contador)
                self.descuento.pop(contador)
                self.stock.pop(contador)
                self.fecha_caducidad.pop(contador)
                self.alcohol.pop(contador)
            contador+=1

    def modificar_bebida(self):
        contador=0
        semaforo_modificar=True
        for i in lista_buscador:
            print(i)
        modificar = int(input("Que quieres cambiar?:"))
        while semaforo_modificar == True:
            if modificar == 1:
                cod= input("Dime el codigo del producto: ")
                cod2= input("Dime el nuevo codigo:")
                for i in self.codigo:
                    if i == cod:
                        self.codigo[contador]=cod2
                        semaforo_modificar=False
                    contador+=1
            elif modificar == 2:
                nom= input("Dime el nombre del producto: ")
                nom=nom.capitalize()
                nom2= input("Dime el nuevo nombre:")
                nom2=nom2.capitalize()
                for i in self.nombre:
                    if i == nom:
                        self.nombre[contador]=nom2
                        semaforo_modificar=False
                    contador+=1
            elif modificar == 3:
                nom= input("Dime el nombre del producto: ")
                nom=nom.capitalize()
                pre2= input("Dime el precio nuevo:")
                for i in self.nombre:
                    if i == nom:
                        self.precio[contador]=pre2
                        semaforo_modificar=False
                    contador+=1
            elif modificar == 4:
                nom= input("Dime el nombre del producto: ")
                nom=nom.capitalize()
                dto= input("Dime el nuevo descuento:")
                for i in self.nombre:
                    if i == nom:
                        self.descuento[contador]=dto
                        semaforo_modificar=False
                    contador+=1
            elif modificar == 5:
                nom= input("Dime el nombre del producto: ")
                nom=nom.capitalize()
                sto= input("Dime el stock nuevo:")
                for i in self.nombre:
                    if i == nom:
                        self.stock[contador]=sto
                        semaforo_modificar=False
                    contador+=1
            elif modificar == 6:
                nom= input("Dime el nombre del producto: ")
                nom=nom.capitalize()
                fecha= input("Dime la nueva fecha de caducidad:")
                for i in self.nombre:
                    if i == nom:
                        self.fecha_caducidad[contador]=fecha
                        semaforo_modificar=False
                    contador+=1
            elif modificar == 8:
                nom= input("Dime el nombre del producto: ")
                nom=nom.capitalize()
                alco= input("Dime la si lleva alcohol:")
                for i in self.nombre:
                    if i == nom:
                        self.alcohol[contador]=alco
                        semaforo_modificar=False
                    contador+=1
            elif modificar == 9:
                semaforo_modificar=False
            else:
                modificar=input("Esa opcion no es valida, ponga una opcion correcta :")

    def buscar_bebida(self):
        contador=0
        semaforo_buscar=True
        for i in lista_buscador:
            print(i)
        buscar = int(input("Que quieres buscar?:"))
        while semaforo_buscar == True:
            if buscar == 1:
                cod= input("Dime el codigo del producto: ")
                for i in self.codigo:
                    if i == cod:
                        print(self.codigo[contador]+";"+self.nombre[contador]+";"+self.precio[contador]+";"+self.descuento[contador]+";"+self.stock[contador]+";"+self.fecha_caducidad[contador]+self.alcohol[contador]+";Bebida")
                        time.sleep(4)
                        semaforo_buscar=False
                    contador+=1
            elif buscar == 2:
                nom= input("Dime el nombre del producto: ")
                nom=nom.capitalize()
                for i in self.nombre:
                    if i == nom:
                        print(self.codigo[contador]+";"+self.nombre[contador]+";"+self.precio[contador]+";"+self.descuento[contador]+";"+self.stock[contador]+";"+self.fecha_caducidad[contador]+self.alcohol[contador]+";Bebida")
                        time.sleep(4)
                        semaforo_buscar=False
                    contador+=1
            elif buscar == 3:
                nom= input("Dime el precio del producto: ")
                for i in self.nombre:
                    if i == nom:
                        print(self.codigo[contador]+";"+self.nombre[contador]+";"+self.precio[contador]+";"+self.descuento[contador]+";"+self.stock[contador]+";"+self.fecha_caducidad[contador]+self.alcohol[contador]+";Bebida")
                        time.sleep(4)
                        semaforo_buscar=False
                    contador+=1
            elif buscar == 4:
                nom= input("Dime el descuento del producto: ")
                for i in self.nombre:
                    if i == cod:
                        print(self.codigo[contador]+";"+self.nombre[contador]+";"+self.precio[contador]+";"+self.descuento[contador]+";"+self.stock[contador]+";"+self.fecha_caducidad[contador]+self.alcohol[contador]+";Bebida")
                        time.sleep(4)
                        semaforo_buscar=False
                    contador+=1
            elif buscar == 5:
                nom= input("Dime el stock del producto: ")
                for i in self.nombre:
                    if i == nom:
                        print(self.codigo[contador]+";"+self.nombre[contador]+";"+self.precio[contador]+";"+self.descuento[contador]+";"+self.stock[contador]+";"+self.fecha_caducidad[contador]+self.alcohol[contador]+";Bebida")
                        time.sleep(4)
                        semaforo_buscar=False
                    contador+=1
            elif buscar == 6:
                nom= input("Dime el fecha de caducidad del producto: ")
                for i in self.nombre:
                    if i == cod:
                        print(self.codigo[contador]+";"+self.nombre[contador]+";"+self.precio[contador]+";"+self.descuento[contador]+";"+self.stock[contador]+";"+self.fecha_caducidad[contador]+self.alcohol[contador]+";Bebida")
                        time.sleep(4)
                        semaforo_buscar=False
                    contador+=1
            elif buscar == 8:
                nom= input("Dime el alcohol del producto: ")
                for i in self.nombre:
                    if i == cod:
                        print(self.codigo[contador]+";"+self.nombre[contador]+";"+self.precio[contador]+";"+self.descuento[contador]+";"+self.stock[contador]+";"+self.fecha_caducidad[contador]+self.alcohol[contador]+";Bebida")
                        time.sleep(4)
                        semaforo_buscar=False
                    contador+=1
            elif buscar == 9:
                semaforo_buscar=False
            else:
                buscar=input("Esa opcion no es valida, ponga una opcion correcta :")

a1=Alimentacion([],[],[],[],[],[]) 
l1=Limpieza([],[],[],[],[],[])
b1=Bebidas([],[],[],[],[],[],[])  



def importar_datos():
    archivo = open("Almacen.txt","r")
    for lineas in archivo:
        lineas=lineas.strip("\n")
        lineas=lineas.split(";")
        if "Alimento" in lineas:
            a1.codigo.append(lineas[0])
            a1.nombre.append(lineas[1])
            a1.precio.append(lineas[2])
            a1.descuento.append(lineas[3])
            a1.stock.append(lineas[4])
            a1.fecha_caducidad.append(lineas[5])
        elif "Limpieza" in lineas:
            l1.codigo.append(lineas[0])
            l1.nombre.append(lineas[1])
            l1.precio.append(lineas[2])
            l1.descuento.append(lineas[3])
            l1.stock.append(lineas[4])
            l1.toxico.append(lineas[5])
        elif "Bebida" in lineas:
            b1.codigo.append(lineas[0])
            b1.nombre.append(lineas[1])
            b1.precio.append(lineas[2])
            b1.descuento.append(lineas[3])
            b1.stock.append(lineas[4])
            b1.fecha_caducidad.append(lineas[5])
            b1.alcohol.append(lineas[6])

def actualizar_txt():
    contenido_txt = []
    archivo = open("Almacen.txt","r+")
    for i in range(len(a1.nombre)):
        lista=[a1.codigo[i], a1.nombre[i],a1.precio[i], a1.descuento[i],a1.stock[i], a1.fecha_caducidad[i],"Alimento"]
        contenido_txt.append(lista)
    for i in range(len(l1.nombre)):
        lista=[l1.codigo[i], l1.nombre[i],l1.precio[i], l1.descuento[i],l1.stock[i], l1.toxico[i],"Limpieza"]
        contenido_txt.append(lista)
    for i in range(len(b1.nombre)):
        lista=[b1.codigo[i], b1.nombre[i],b1.precio[i], b1.descuento[i],b1.stock[i], b1.fecha_caducidad[i], b1.alcohol[i],"Bebida"]
        contenido_txt.append(lista)


def menu():
    semaforo = True
    
    while semaforo == True:
        actualizar_txt()
        for i in lista_menu:
            print(i)
        opcion=int(input("Qué quieres hacer?: "))
        if opcion == 1:
            semaforo_alta=True
            while semaforo_alta == True:
                os.system("cls")
                for i in lista_seccion:
                    print(i)
                print("Has selecionado dar de alta, empecemos.")
                familia=int(input("A que seccion pertenece: "))
                if familia == 1:
                    os.system("cls")
                    a1.alta_alimento()
                    semaforo_alta = False
                elif familia == 2:
                    os.system("cls")
                    l1.alta_limpieza()
                    semaforo_alta = False
                elif familia == 3:
                    os.system("cls")
                    b1.alta_bebida()
                    semaforo_alta = False
                elif familia == 4:
                    os.system("cls")
                    semaforo_alta = False
                else:
                    familia=input("Esa opcion no es valida, ponga una opcion correcta :")
        elif opcion == 2:
            os.system("cls")
            a1.listado_alimento()
            l1.listado_limpieza()
            b1.listado_bebida()
        elif opcion == 3:
            semaforo_borrar =True
            while semaforo_borrar == True:
                os.system("cls")
                for i in lista_seccion:
                    print(i)
                seleccion= int(input("De que seccion quieres borrar?:"))
                if seleccion == 1:
                    os.system("cls")
                    a1.borrar_alimento()
                elif seleccion == 2:
                    os.system("cls")
                    l1.borrar_limpieza()
                elif seleccion == 3:
                    os.system("cls")
                    b1.borrar_bebida()
                elif seleccion == 4:
                    os.system("cls")
                    semaforo_borrar = False
                else:
                    seleccion=input("Esa opcion no es valida, ponga una opcion correcta :")

        elif opcion == 4:
            semaforo_modificar =True
            while semaforo_modificar == True:
                os.system("cls")
                for i in lista_seccion:
                    print(i)
                seleccion= int(input("De que seccion quieres modificar?:"))
                if seleccion == 1:
                    os.system("cls")
                    a1.modificar_alimento()
                elif seleccion == 2:
                    os.system("cls")
                    l1.modificar_limpieza()
                elif seleccion == 3:
                    os.system("cls")
                    b1.modificar_bebida()
                elif seleccion == 4:
                    os.system("cls")
                    semaforo_modificar = False
                else:
                    seleccion=input("Esa opcion no es valida, ponga una opcion correcta :")
        elif opcion == 5:
            semaforo_buscar =True
            while semaforo_buscar == True:
                os.system("cls")
                for i in lista_seccion:
                    print(i)
                seleccion= int(input("De que seccion quieres buscar?:"))
                if seleccion == 1:
                    os.system("cls")
                    a1.buscar_alimento()
                elif seleccion == 2:
                    os.system("cls")
                    l1.buscar_limpieza()
                elif seleccion == 3:
                    os.system("cls")
                    b1.buscar_bebida()
                elif seleccion == 4:
                    os.system("cls")
                    semaforo_buscar = False
                else:
                    seleccion=input("Esa opcion no es valida, ponga una opcion correcta :")
        elif opcion == 6:
            semaforo=False
        else:
            opcion=input("Esa opcion no es valida, ponga una que esta en la lista: ")

lista_menu=["Menu Principal", "1- Alta de producto" ,"2- Listado", "3- Borrar producto", "4- Modificar PVP", "5- Buscador", "6- Salir"]
lista_seccion=["1- Alimentacion", "2- Limpieza", "3- Bebidas", "4- Salir"]
lista_buscador=["1- Codigo", "2- Nombre", "3- Precio", "4- Descuento", "5- Stock", "6- Fecha caducidad", "7- Toxico", "8- Alcohol", "9- Salir"]
importar_datos()    
menu()
