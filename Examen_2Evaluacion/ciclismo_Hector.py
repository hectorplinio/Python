ruta="/media/HECTORNAVARRO/F2ED-8508/DAW/programacion/Segunda/examen/"
class Ciclista():
    def __init__(self, dorsal, nombre, edad, equipo):
        self.dorsal=dorsal
        self.nombre=nombre
        self.edad=edad
        self.equipo=equipo
    
    def inicializar_equipo(self,equipo):
        self.equipo=equipo

    def alta_ciclista(self):
        archivo=open(ruta+"ciclista.txt","r+")
        for linea in archivo:
            linea=linea.strip("\n")
            linea=linea.split(";")
            self.dorsal.append(linea[0])
            self.nombre.append(linea[1])
            self.edad.append(linea[2])
            self.equipo.append(linea[3])


class Equipo():
    def __init__(self, codigo_equipo, equipo, director):
        self.codigo_equipo=codigo_equipo
        self.equipo=equipo
        self.director=director
    
    def alta_equipo(self):
        archivo=open(ruta+"equipo.txt","r")
        for linea in archivo:
            linea=linea.strip("\n")
            linea=linea.split(";")
            self.codigo_equipo.append(linea[0])
            self.equipo.append(linea[1])
            self.director.append(linea[2])
    
    def lista_equipos(self):
        for i in self.equipo:
            print(contador, i)
    
    

class Generar(Ciclista,Equipo):
    def __init__(self,dorsal, nombre, edad, equipo, director, codigo_equipo):
        Ciclista.__init__(self, dorsal, nombre, edad, equipo)
        Equipo.__init__(self,codigo_equipo, equipo, director)
    
    def alta_generar(self):
        self.dorsal=ciclista.dorsal
        self.nombre=ciclista.nombre
        self.edad=ciclista.edad
        self.equipo=ciclista.equipo
        self.director=equipo.director
        self.codigo_equipo=equipo.codigo_equipo
    
    def listado(self):

        archivo=open(ruta+"equipos.html","a+")
        for i in lista_equipo:
            print(i)
        opcion =int(input("Seleccione una opcion: "))
        print("Dorsal;Corredor;Edad;Equipo;Director")
        archivo.write("Dorsal;Corredor;Edad;Equipo;Director"+"\n")
        if opcion == 1:
            x=0
            for i in self.equipo:
                if i == '"Amore Vita"':
                    print(self.dorsal[x]+";"+self.nombre[x]+";"+self.edad[x]+";"+self.equipo[x]+";Ricardo Padacci")
                    frase=self.dorsal[x]+";"+self.nombre[x]+";"+self.edad[x]+";"+self.equipo[x]+";Ricardo Padacci"
                    archivo.write(frase+"\n")
                else:
                    x+=1
        elif opcion == 2:
            x=0
            for i in self.equipo:
                
                if i == '"Artiach"':
                    print(self.dorsal[x]+";"+self.nombre[x]+";"+self.edad[x]+";"+self.equipo[x]+";José Pérez")
                    frase=self.dorsal[x]+";"+self.nombre[x]+";"+self.edad[x]+";"+self.equipo[x]+";José Pérez"
                    archivo.write(frase+"\n")
                else:
                    x+=1
        elif opcion == 3:
            x=0
            for i in self.equipo:
                
                if i == '"Banesto"':
                    print(self.dorsal[x]+";"+self.nombre[x]+";"+self.edad[x]+";"+self.equipo[x]+";Miguel Echevarría")
                    frase=self.dorsal[x]+";"+self.nombre[x]+";"+self.edad[x]+";"+self.equipo[x]+";Miguel Echevarría"
                    archivo.write(frase+"\n")
                else:
                    x+=1
        elif opcion == 4:
            x=0
            for i in self.equipo:
                
                if i == '"Bresciali-Refin"':
                    print(self.dorsal[x]+";"+self.nombre[x]+";"+self.edad[x]+";"+self.equipo[x]+";Pietro Armani")
                    frase=self.dorsal[x]+";"+self.nombre[x]+";"+self.edad[x]+";"+self.equipo[x]+";Pietro Armani"
                    archivo.write(frase+"\n")
                else:
                    x+=1
        elif opcion == 5:
            x=0
            for i in self.equipo:
                
                if i == '"Carrera"':
                    print(self.dorsal[x]+";"+self.nombre[x]+";"+self.edad[x]+";"+self.equipo[x]+";Luigi Petroni")
                    frase=self.dorsal[x]+";"+self.nombre[x]+";"+self.edad[x]+";"+self.equipo[x]+";Luigi Petroni"
                    archivo.write(frase+"\n")
                else:
                    x+=1
        elif opcion == 6:
            x=0
            for i in self.equipo:
                
                if i == '"Castorama"':
                    print(self.dorsal[x]+";"+self.nombre[x]+";"+self.edad[x]+";"+self.equipo[x]+";Jean Philip")
                    frase=self.dorsal[x]+";"+self.nombre[x]+";"+self.edad[x]+";"+self.equipo[x]+";Jean Philip"
                    archivo.write(frase+"\n")
                else:
                    x+=1
        elif opcion == 7:
            x=0
            for i in self.equipo:
                
                if i == '"Euskadi"':
                    print(self.dorsal[x]+";"+self.nombre[x]+";"+self.edad[x]+";"+self.equipo[x]+";Pedro Txucaru")
                    frase=self.dorsal[x]+";"+self.nombre[x]+";"+self.edad[x]+";"+self.equipo[x]+";Pedro Txucaru"
                    archivo.write(frase+"\n")
                else:
                    x+=1
        elif opcion == 8:
            x=0
            for i in self.equipo:
                
                if i == '"Gatorade"':
                    print(self.dorsal[x]+";"+self.nombre[x]+";"+self.edad[x]+";"+self.equipo[x]+";Gian Luca Pacceli")
                    frase=self.dorsal[x]+";"+self.nombre[x]+";"+self.edad[x]+";"+self.equipo[x]+";Gian Luca Pacceli"
                    archivo.write(frase+"\n")
                else:
                    x+=1
        elif opcion == 9:
            x=0
            for i in self.equipo:
                
                if i == '"Gewiss"':
                    print(self.dorsal[x]+";"+self.nombre[x]+";"+self.edad[x]+";"+self.equipo[x]+";Moreno Argentin")
                    frase=self.dorsal[x]+";"+self.nombre[x]+";"+self.edad[x]+";"+self.equipo[x]+";Moreno Argentin"
                    archivo.write(frase+"\n")
                else:
                    x+=1
        elif opcion == 10:
            x=0
            for i in self.equipo:
                
                if i == '"Jolly Club"':
                    print(self.dorsal[x]+";"+self.nombre[x]+";"+self.edad[x]+";"+self.equipo[x]+";Johan Richard")
                    frase=self.dorsal[x]+";"+self.nombre[x]+";"+self.edad[x]+";"+self.equipo[x]+";Johan Richard"
                    archivo.write(frase+"\n")
                else:
                    x+=1
        elif opcion == 11:
            x=0
            for i in self.equipo:
                
                if i == '"Kelme"':
                    print(self.dorsal[x]+";"+self.nombre[x]+";"+self.edad[x]+";"+self.equipo[x]+";Álvaro Pino")
                    frase=self.dorsal[x]+";"+self.nombre[x]+";"+self.edad[x]+";"+self.equipo[x]+";Álvaro Pino"
                    archivo.write(frase+"\n")
                else:
                    x+=1
        elif opcion == 12:
            x=0
            for i in self.equipo:
                
                if i == '"Lotus Festina"':
                    print(self.dorsal[x]+";"+self.nombre[x]+";"+self.edad[x]+";"+self.equipo[x]+";Suárez Cuevas")
                    frase=self.dorsal[x]+";"+self.nombre[x]+";"+self.edad[x]+";"+self.equipo[x]+";Suárez Cuevas"
                    archivo.write(frase+"\n")
                else:
                    x+=1
        elif opcion == 13:
            x=0
            for i in self.equipo:
                
                if i == '"Mapei-Clas"':
                    print(self.dorsal[x]+";"+self.nombre[x]+";"+self.edad[x]+";"+self.equipo[x]+";Juan Fernández")
                    frase=self.dorsal[x]+";"+self.nombre[x]+";"+self.edad[x]+";"+self.equipo[x]+";Juan Fernández"
                    archivo.write(frase+"\n")
                else:
                    x+=1
        elif opcion == 14:
            x=0
            for i in self.equipo:
                
                if i == '"Mercatone Uno"':
                    print(self.dorsal[x]+";"+self.nombre[x]+";"+self.edad[x]+";"+self.equipo[x]+";Ettore Romano")
                    frase=self.dorsal[x]+";"+self.nombre[x]+";"+self.edad[x]+";"+self.equipo[x]+";Ettore Romano"
                    archivo.write(frase+"\n")
                else:
                    x+=1
        elif opcion == 15:
            x=0
            for i in self.equipo:
                
                if i == '"Motorola"':
                    print(self.dorsal[x]+";"+self.nombre[x]+";"+self.edad[x]+";"+self.equipo[x]+";John Fidwell")
                    frase=self.dorsal[x]+";"+self.nombre[x]+";"+self.edad[x]+";"+self.equipo[x]+";John Fidwell"
                    archivo.write(frase+"\n")
                else:
                    x+=1
        elif opcion == 16:
            x=0
            for i in self.equipo:
                
                if i == '"Navigare"':
                    print(self.dorsal[x]+";"+self.nombre[x]+";"+self.edad[x]+";"+self.equipo[x]+";Lonrenzo Sciacci")
                    frase=self.dorsal[x]+";"+self.nombre[x]+";"+self.edad[x]+";"+self.equipo[x]+";Lonrenzo Sciacci"
                    archivo.write(frase+"\n")
                else:
                    x+=1
        elif opcion == 17:
            x=0
            for i in self.equipo:
                
                if i == '"ONCE"':
                    print(self.dorsal[x]+";"+self.nombre[x]+";"+self.edad[x]+";"+self.equipo[x]+";Manuel Sainz")
                    frase=self.dorsal[x]+";"+self.nombre[x]+";"+self.edad[x]+";"+self.equipo[x]+";Manuel Sainz"
                    archivo.write(frase+"\n")
                else:
                    x+=1
        elif opcion == 18:
            x=0
            for i in self.equipo:
                
                if i == '"PDM"':
                    print(self.dorsal[x]+";"+self.nombre[x]+";"+self.edad[x]+";"+self.equipo[x]+";Piet Van Der Kruis")
                    frase=self.dorsal[x]+";"+self.nombre[x]+";"+self.edad[x]+";"+self.equipo[x]+";Piet Van Der Kruis"
                    archivo.write(frase+"\n")
                else:
                    x+=1
        elif opcion == 19:
            x=0
            for i in self.equipo:
                
                if i == '"Seguros Amaya"':
                    print(self.dorsal[x]+";"+self.nombre[x]+";"+self.edad[x]+";"+self.equipo[x]+";Mínguez")
                    frase=self.dorsal[x]+";"+self.nombre[x]+";"+self.edad[x]+";"+self.equipo[x]+";Mínguez"
                    archivo.write(frase+"\n")
                else:
                    x+=1
        elif opcion == 20:
            x=0
            for i in self.equipo:
                
                if i == '"Telecom"':
                    print(self.dorsal[x]+";"+self.nombre[x]+";"+self.edad[x]+";"+self.equipo[x]+";Morgan Reikcard")
                    frase=self.dorsal[x]+";"+self.nombre[x]+";"+self.edad[x]+";"+self.equipo[x]+";Morgan Reikcard"
                    archivo.write(frase+"\n")
                else:
                    x+=1
        elif opcion == 21:
            x=0
            for i in self.equipo:
                
                if i == '"TVM"':
                    print(self.dorsal[x]+";"+self.nombre[x]+";"+self.edad[x]+";"+self.equipo[x]+";Steveens Henk")
                    frase=self.dorsal[x]+";"+self.nombre[x]+";"+self.edad[x]+";"+self.equipo[x]+";Steveens Henk"
                    archivo.write(frase+"\n")
                else:
                    x+=1
        elif opcion == 22:
            x=0
            for i in self.equipo:
                
                if i == '"Wordperfect"':
                    print(self.dorsal[x]+";"+self.nombre[x]+";"+self.edad[x]+";"+self.equipo[x]+";Bill Gates")
                    frase=self.dorsal[x]+";"+self.nombre[x]+";"+self.edad[x]+";"+self.equipo[x]+";Bill Gates"
                    archivo.write(frase+"\n")
                else:
                    x+=1
        else:
            opcion =int(input("Seleccione una opcion correcta: "))  
        archivo.close()


        

    def generar_html(self):
        nom=input("Seleccione el nombre del que quiere hacer la consulta:")
        nom=nom.capitalize()
        contador=0
        for i in self.equipo:
            if nom == i:
                print("Equipo"+nom+ "Director:"+self.director[contador])
                
            else:
                contador+=1


lista_menu=["1- Listado equipos", "2- Generar HTML ", "3- Salir"]
lista_equipo=["1- Amore Vita","2- Artiach","3- Banesto", "4- Bresciali-Refin", "5- Carrera", "6- Castorama", "7- Euskadi", "8- Gatorade", "9- Gewiss", "10- Jolly Club", "11- Kelme", "12- Lotus Festina", "13- Mapei-Clas", "14- Mercatone Uno", "15- Motorola", "16- Navigare", "17- ONCE", "18- PDM", "19- Seguros Amaya" , "20- Telecom", "21- TVM", "22- Wordperfect" ]
ciclista=Ciclista([],[],[],[])
equipo=Equipo([],[],[])
generar=Generar([],[],[],[],[],[])
ciclista.alta_ciclista()
equipo.alta_equipo()
generar.alta_generar()


def menu():
    semaforo=True
    while semaforo == True:
        print("Bienvenido al menu de consultas de la Vuelta a España.")
        for i in lista_menu:
            print(i)
        opcion=int(input("Seleccione una opcion para empezar."))
        if opcion == 1:
            generar.listado()
        elif opcion == 2:
            generar.generar_html()
        elif opcion == 3:
            semaforo=False
        else:
            opcion=int(input("Seleccione una opcion correcta empezar."))

menu()