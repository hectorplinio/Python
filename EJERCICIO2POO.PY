class Persona:
    def __init__(self, nombre, edad):
        self.nombre=nombre
        self.edad=edad
    
    def imprimir (self):
        print (self.nombre)
    
    def mayor (self):
        if self.edad >= 18:
            print ("Es mayor de edad.")
        else:
            print ("No es mayor de edad.")

p1=Persona("Alberto", 16)
p1.imprimir()
p1.mayor()