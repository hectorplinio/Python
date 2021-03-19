lista_alumnos=[]
lista_notas=[]
lista_asignatura=["Matematicas", "Lengua", "Ingles", "Historia", "Informatica", "Valenciano", "Gimnasia", "Dibujo"]
class Alumno:
    def __init__(self,numero, nombre):
        self.numero=numero
        self.nombre=nombre
    
    def alta_alumno(self):
        global lista_alumnos
        alumnos = open("Alumnos.txt","r")
        for lineas in alumnos:
            lineas=lineas.strip("\n")
            lineas=lineas.split(";")
            self.numero.append(lineas[0])
            self.nombre.append(lineas[1])
            lista_alumnos.append(lineas[0]+"-->"+lineas[1])

class Notas:
    def __init__(self, matematicas,lengua, ingles, historia, informatica, valenciano, gimnasia, dibujo, codigo, nota):
        self.matematicas=matematicas
        self.lengua=lengua
        self.ingles=ingles
        self.historia=historia
        self.informatica=informatica
        self.valenciano=valenciano
        self.gimnasia=gimnasia
        self.dibujo=dibujo
        self.codigo=codigo
        self.nota=nota
    
    def alta_nota(self):
        notas = open("notas.txt","r")
        for lineas in notas:
                lineas=lineas.strip("\n")
                lineas=lineas.split(";")
                if lineas[0] == "Matematicas":
                    self.matematicas.append(lineas[2])
                elif lineas[0] == "Lengua":
                    self.lengua.append(lineas[2])
                elif lineas[0] == "Ingles":
                    self.ingles.append(lineas[2])
                elif lineas[0] == "Historria":
                    self.historia.append(lineas[2])
                elif lineas[0] == "Informatica":
                    self.informatica.append(lineas[2])
                elif lineas[0] == "Valenciano":
                    self.valenciano.append(lineas[2])
                elif lineas[0] == "Gimnasia":
                    self.gimnasia.append(lineas[2])
                elif lineas[0] == "Dibujo":
                    self.dibujo.append(lineas[2])
                

class Boletin(Alumno, Notas):
    def __init__(self, numero,nombre, matematicas,lengua, ingles, historia, informatica, valenciano, gimnasia, dibujo,codigo, nota):
        Alumno.__init__(self, numero, nombre)
        Notas.__init__(self, matematicas,lengua, ingles, historia, informatica, valenciano, gimnasia, dibujo,codigo, nota)

    
def menu():
    global lista_alumnos
    archivo=open("Boletin.txt","w+")
    contador=0
    semaforo=True
    while semaforo == True:
        for i in lista_alumnos:
            print(i)
        nom=input("Dime el numero del alumno:")
        for i in b1.numero:
            if i == nom:
                print("Estas son las notas de "+b1.nombre[int(nom)])
                frase="Estas son las notas de "+b1.nombre[int(nom)]
                archivo.write(frase+"\n")
                nom=int(nom)
                nom=nom-1
                
                for i in lista_asignatura:
                    if i == "Matematicas":
                        print(i,b1.matematicas[int(nom)])
                        frase = "Matematicas: "+b1.matematicas[int(nom)]
                        archivo.write(frase+"\n")
                    elif i == "Lengua":
                        print(i,b1.lengua[int(nom)])
                        frase = "Lengua: "+b1.lengua[int(nom)]
                        archivo.write(frase+"\n")
                    elif i == "Ingles":
                        print(i,b1.ingles[int(nom)])
                        frase = "Ingles: "+b1.ingles[int(nom)]
                        archivo.write(frase+"\n")
                    elif i == "Historia":
                        print(i,b1.historia[int(nom)])
                        frase = "Historia: "+b1.historia[int(nom)]
                        archivo.write(frase+"\n")
                    elif i == "Informatica":
                        print(i,b1.informatica[int(nom)])
                        frase = "Informatica: "+b1.informatica[int(nom)]
                        archivo.write(frase+"\n")
                    elif i == "Valenciano":
                        print(i,b1.valenciano[int(nom)])
                        frase = "Valenciano: "+b1.valenciano[int(nom)]
                        archivo.write(frase+"\n")
                    elif i == "Gimnasia":
                        print(i,b1.gimnasia[int(nom)])
                        frase = "Gimnasia: "+b1.gimnasia[int(nom)]
                        archivo.write(frase+"\n")
                    elif i == "Dibujo":
                        print(i,b1.dibujo[int(nom)])
                        frase = "Dibujo: "+b1.dibujo[int(nom)]
                        archivo.write(frase+"\n")
                    
                media=(int(b1.matematicas[int(nom)])+int(b1.lengua[int(nom)])+int(b1.ingles[int(nom)])+int(b1.historia[int(nom)])+int(b1.informatica[int(nom)])+int(b1.valenciano[int(nom)])+int(b1.gimnasia[int(nom)])+int(b1.dibujo[int(nom)]))/8
                print("La nota media es de:",media)
                frase = "La nota media es de:" + str(media)
                archivo.write(frase +"\n")
                archivo.close()
                semaforo=False
            
                
                



b1=Boletin([],[],[],[],[],[],[],[],[],[],[],[])
b1.alta_alumno()
b1.alta_nota()
a1=Alumno([],[])
n1=Notas([],[],[],[],[],[],[],[],[],[],)
menu()