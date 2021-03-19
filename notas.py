class Alumno:
    def __init__(self,id, nombre):
        self.numero=numero
        self.nombre=nombre
    
    def alta_alumno(self):
        alumnos = open("Alumnos.txt","r")
        for lineas in archivo:
            lineas=lineas.strip("\n")
            lineas=lineas.split(";")
            self.numero.append(lineas[0])
            self.nombre.append(lineas[1])

class Notas:
    def __init__(self, asigantura,codigo, nota):
        self.asignatura=asigantura
        self.codigo=codigo
        self.nota=nota
    
    def alta_nota(self):
        notas = open("notas.txt","r")
        for lineas in notas:
            lineas=lineas.strip("\n")
            lineas=lineas.split(";")
            self.asignatura.append(lineas[0])
            self.numero.append(lineas[1])
            self.nota.append(lineas[2])

class Boletin(Alumno, Notas):
    def __init__(self, numero,nombre, asignatura,codigo, nota):
        Alumno.__init__(self, numero, nombre)
        Notas.__init__(self, asignatura,codigo, nota)
    
    def comparar(self):
        nom=input("Dime el nombre del alumno:")
        nom=nom.capitalize()
        for i in b1.nombre:
            if i == nom:

def importar_datos():
    semaforo_importar=True
    contador=1
    alumnos = open("Alumnos.txt","r")
    notas = open("notas.txt","r")
    for lineas in alumnos:
        lineas=lineas.strip("\n")
        lineas=lineas.split(";")
        lista_alumnos.append(lineas)

    for lineas in notas:
        lineas=lineas.strip("\n")
        lineas=lineas.split(";")
        lista_notas.append(lineas)
    for i in range(lista_alumnos):
        if lista_notas[1] == 1:
            lista_conjunta=[lista_alumnos[0],lista_alumnos[1],lista_notas[0],lista_notas[2]]
    
def menu():
    importar_datos()
    alta_alumno()
    alta_nota()
    semaforo=True
    while semaforo == True:
        importar_datos()
        nom=input("Dime el nombre del alumno:")
        nom=nom.capitalize()

lista_alumnos=[]
lista_notas=[]
lista_conjunta=[]
b1=Boletin([],[],[],[],[])
menu()