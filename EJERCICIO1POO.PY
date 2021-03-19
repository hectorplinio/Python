class Alumno:
    def __init__(self, nombre, nota):
        self.nombre=nombre
        self.nota=nota
    
    def imprimir(self):
        print(self.nombre)

    def notas(self):
        if self.nota >= 5:
            print ("Has aprobado")
        else:
            print ("Has suspendido")
    
p1=Alumno("Sergio", 4)
p1.imprimir()
p1.notas()


