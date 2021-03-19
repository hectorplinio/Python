class Persona():
    def __init__(self, identificador, nombre, telefono):
        self.identificador=identificador
        self.nombre=nombre
        self.telefono=telefono

    def alta(self):
        nom=input("Dime el nombre de la persona: ")
        nom=nom.capitalize()
        self.nombre.append(nom)
        tel=input("Dime el numero de telefono la persona:")
        self.telefono.append(tel)


class Profesor(Persona):
    def __init__(self, identificador, nombre, telefono, departamento):
        Persona.__init__(self,identificador, nombre, telefono)
        self.departamento=departamento

    def alta_profesor(self):
        print("Has seleccionado dar de alta un profesor.")
        cod=input("Dime el identificador de la persona: ")
        profes= open("Profes.txt", "a+")
        for i in range(len(self.nombre)):
            if self.identificador[i] == cod:
                print("Este profesor ya esta en la lista, cambie el codigo.")
                cod=input("Dime el codigo del profesor: ")
        self.identificador.append(cod)
        Persona.alta(self)
        dep=input("Dime el departamento al que pertenece: ")
        dep=dep.capitalize()
        self.departamento.append(dep)
        frase=self.identificador[-1]+";"+self.nombre[-1]+";"+self.telefono[-1]+";"+self.departamento[-1]
        profes.write(frase+"\n")
        print("Ha añadido usted el profesor "+self.nombre[-1]+" con un código "+self.identificador[-1]+" con un telefono de "+self.telefono[-1]+" y su departamento es "+self.departamento[-1])
        
        profes.close()
    
    def borrar_profesor(self):
        archivo= open("Profes.txt", "a+")
        contador=0
        bor = input("Que nombre quieres borrar?:")
        bor=bor.capitalize()
        for i in self.nombre:
            if i == bor:
                contador+=1
                pass
            else:
                frase=self.identificador[contador]+";"+self.nombre[contador]+";"+self.telefono[contador]+";"+self.departamento[contador]
                contador+=1
        archivo.close()
    
    def importar_datos(self):
        archivo = open("Profes.txt","r")
        for lineas in archivo:
            lineas=lineas.strip("\n")
            lineas=lineas.split(";")
            profesor.identificador.append(lineas[0])
            profesor.nombre.append(lineas[1])
            profesor.telefono.append(lineas[2])
            profesor.departamento.append(lineas[3])
        archivo.close()

    def inicializar_identificador(self, identificador):
        self.identificador=identificador
    
    def modificar_profesor(self):
        contador=0
        semaforo_modificar=True
        for i in lista_modificar_profesor:
            print(i)
        modificar=int(input("Que opcion quieres cambiar: "))
        while semaforo_modificar == True:
            if modificar == 1:
                nom= input("Dime el nombre del profesor: ")
                nom=nom.capitalize()
                cod2= input("Dime el nuevo codigo:")
                for i in self.nombre:
                    if i == nom:
                        self.codigo[contador]=cod2
                        semaforo_modificar=False
                    contador+=1
            elif modificar == 2:
                nom= input("Dime el nombre del profesor: ")
                nom=nom.capitalize()
                nom2= input("Dime el nuevo nombre:")
                nom2=nom2.capitalize()
                for i in self.nombre:
                    if i == nom:
                        self.nombre[contador]=nom2
                        semaforo_modificar=False
                    contador+=1
            elif modificar == 3:
                nom= input("Dime el nombre del profesor: ")
                nom=nom.capitalize()
                tel= input("Dime el telefono nuevo:")
                for i in self.nombre:
                    if i == nom:
                        self.telefono[contador]=tel
                        semaforo_modificar=False
                    contador+=1  
            elif modificar == 4:
                nom= input("Dime el nombre del profesor: ")
                nom=nom.capitalize()
                dep= input("Dime el nuevo departamento:")
                for i in self.nombre:
                    if i == nom:
                        self.departamento[contador]=dep
                        semaforo_modificar=False
                    contador+=1
            elif modificar == 5:
                semaforo_modificar=False
            else:
                modificar=input("Esa opcion no es valida, ponga una opcion correcta :")

    def actualizar_profesores(self):
        archivo = open("Profes.txt","w+")
        for i in range(len(self.nombre)):
            frase=self.identificador[i]+";"+self.nombre[i]+";"+self.telefono[i]+";"+self.departamento[i]
            archivo.write(frase+"\n")
        archivo.close()
    
    def listado_profesor(self):
        print("Identificador;Nombre;Telefono;Departamento")
        for i in range(len(self.nombre)):
            print(self.identificador[i]+";"+self.nombre[i]+";"+self.telefono[i]+";"+self.departamento[i])

    def buscar_profesor(self):
        contador=0
        semaforo_buscar=True
        for i in lista_modificar_profesor:
            print(i)
        buscar = int(input("Que quieres buscar?:"))
        while semaforo_buscar == True:
            if buscar == 1:
                cod= input("Dime el codigo del profesor: ")
                for i in self.codigo:
                    if i == cod:
                        print(self.identificador[contador]+";"+self.nombre[contador]+";"+self.telefono[contador]+";"+self.departamento[contador])
                        semaforo_buscar=False
                    contador+=1
            elif buscar == 2:
                nom= input("Dime el nombre del profesor: ")
                nom=nom.capitalize()
                for i in self.nombre:
                    if i == nom:
                        print(self.identificador[contador]+";"+self.nombre[contador]+";"+self.telefono[contador]+";"+self.departamento[contador])
                        semaforo_buscar=False
                    contador+=1
            elif buscar == 3:
                tel= input("Dime el telefono del profesor: ")
                for i in self.telefono:
                    if i == tel:
                        print(self.identificador[contador]+";"+self.nombre[contador]+";"+self.telefono[contador]+";"+self.departamento[contador])
                        semaforo_buscar=False
                    contador+=1
            elif buscar == 4:
                dto= input("Dime el departamento del profesor: ")
                for i in self.departamento:
                    if i == dto:
                        print(self.identificador[contador]+";"+self.nombre[contador]+";"+self.telefono[contador]+";"+self.departamento[contador])
                        semaforo_buscar=False
                    contador+=1
            elif buscar == 5:
                semaforo_buscar=False
            else:
                buscar=input("Esa opcion no es valida, ponga una opcion correcta :")

class Alumno(Persona):
    def __init__(self, identificador, nombre, telefono, curso):
        Persona.__init__(self,identificador, nombre, telefono)
        self.curso=curso

    def alta_alumno(self):
        print("Has seleccionado dar de alta un alumno.")
        cod=input("Dime el identificador de la persona: ")
        archivo = open("Alumnado.txt", "a+")
        for i in range(len(self.nombre)):
            if self.identificador[i] == cod:
                print("Este profesor ya esta en la lista, cambie el codigo.")
                cod=input("Dime el codigo del profesor: ")
        self.identificador.append(cod)
        Persona.alta(self)
        self.curso.append(input("Dime el curso al que pertenece: "))
        frase=self.identificador[-1]+";"+self.nombre[-1]+";"+self.telefono[-1]+";"+self.curso[-1]
        archivo.write(frase+"\n")
        print("Ha añadido usted el profesor "+self.nombre[-1]+" con un código "+self.identificador[-1]+" con un telefono de "+self.telefono[-1]+" y su curso es  "+self.curso[-1])
        
        archivo.close()
    
    def borrar_alumno(self):
        archivo = open("Alumnado.txt", "a+")
        contador=0
        bor = input("Que nombre quieres borrar?:")
        bor=bor.capitalize()
        for i in self.nombre:
            if i == bor:
                contador+=1
                pass
            else:
                frase=self.identificador[contador]+";"+self.nombre[contador]+";"+self.telefono[contador]+";"+self.curso[contador]
                archivo.write(frase+"\n")
                contador+=1
        archivo.close()
                
    
    def importar_datos(self):
        archivo = open("Alumnado.txt","r")
        for lineas in archivo:
            lineas=lineas.strip("\n")
            lineas=lineas.split(";")
            alumno.identificador.append(lineas[0])
            alumno.nombre.append(lineas[1])
            alumno.telefono.append(lineas[2])
            alumno.curso.append(lineas[3])
        archivo.close()

    def modificar_alumno(self):
        contador=0
        semaforo_modificar=True
        for i in lista_modificar_alumno:
            print(i)
        modificar=int(input("Que opcion quieres cambiar: "))
        while semaforo_modificar == True:
            if modificar == 1:
                nom= input("Dime el nombre del alumno: ")
                nom=nom.capitalize()
                cod2= input("Dime el nuevo codigo:")
                for i in self.nombre:
                    if i == nom:
                        self.identificador[contador]=cod2
                        semaforo_modificar=False
                    contador+=1
            elif modificar == 2:
                nom= input("Dime el nombre del alumno: ")
                nom=nom.capitalize()
                nom2= input("Dime el nuevo nombre:")
                nom2=nom2.capitalize()
                for i in self.nombre:
                    if i == nom:
                        self.nombre[contador]=nom2
                        semaforo_modificar=False
                    contador+=1
            elif modificar == 3:
                nom= input("Dime el nombre del alumno: ")
                nom=nom.capitalize()
                tel= input("Dime el telefono nuevo:")
                for i in self.nombre:
                    if i == nom:
                        self.telefono[contador]=tel
                        semaforo_modificar=False
                    contador+=1  
            elif modificar == 4:
                nom= input("Dime el nombre del alumno: ")
                nom=nom.capitalize()
                cur= input("Dime el nuevo curso:")
                for i in self.nombre:
                    if i == nom:
                        self.curso[contador]=cur
                        semaforo_modificar=False
                    contador+=1
            elif modificar == 5:
                semaforo_modificar=False
            else:
                modificar=input("Esa opcion no es valida, ponga una opcion correcta :")
    
    def actualizar_alumnos(self):
        archivo = open("Alumnado.txt","w+")
        for i in range(len(self.nombre)):
            frase=self.identificador[i]+";"+self.nombre[i]+";"+self.telefono[i]+";"+self.curso[i]
            archivo.write(frase+"\n")
        archivo.close()

    def listado_alumno(self):
        print("Identificador;Nombre;Telefono;Curso")
        for i in range(len(self.nombre)):
            print(self.identificador[i]+";"+self.nombre[i]+";"+self.telefono[i]+";"+self.curso[i])

    def buscar_alumno(self):
        contador=0
        semaforo_buscar=True
        for i in lista_modificar_alumno:
            print(i)
        buscar = int(input("Que quieres buscar?:"))
        while semaforo_buscar == True:
            if buscar == 1:
                cod= input("Dime el codigo del alumno: ")
                for i in self.codigo:
                    if i == cod:
                        print(self.identificador[contador]+";"+self.nombre[contador]+";"+self.telefono[contador]+";"+self.curso[contador])
                        semaforo_buscar=False
                    contador+=1
            elif buscar == 2:
                nom= input("Dime el nombre del alumno: ")
                nom=nom.capitalize()
                for i in self.nombre:
                    if i == nom:
                        print(self.identificador[contador]+";"+self.nombre[contador]+";"+self.telefono[contador]+";"+self.curso[contador])
                        semaforo_buscar=False
                    contador+=1
            elif buscar == 3:
                tel= input("Dime el telefono del alumno: ")
                for i in self.telefono:
                    if i == tel:
                        print(self.identificador[contador]+";"+self.nombre[contador]+";"+self.telefono[contador]+";"+self.curso[contador])
                        semaforo_buscar=False
                    contador+=1
            elif buscar == 4:
                dto= input("Dime el curso del alumno: ")
                for i in self.curso:
                    if i == dto:
                        print(self.identificador[contador]+";"+self.nombre[contador]+";"+self.telefono[contador]+";"+self.curso[contador])
                        semaforo_buscar=False
                    contador+=1
            elif buscar == 5:
                semaforo_buscar=False
            else:
                buscar=input("Esa opcion no es valida, ponga una opcion correcta :")

class Asignatura(Profesor):
    def __init__(self, identificador, nombre, idasignatura, curso, horas_semanales):
        Profesor.inicializar_identificador(self,identificador)
        self.nombre=nombre
        self.idasignatura=idasignatura
        self.curso=curso
        self.horas_semanales=horas_semanales
    
    def alta_asignatura(self):
        print("Has seleccionado dar de alta una asignatura.")
        cod=input("Dime el codigo de la asignatura: ")
        archivo= open("Asignatura.txt", "a+")
        for lineas in archivo:
            lineas=lineas.strip("\n")
            lineas=lineas.split(";")
            if lineas[0] == cod:
                print("Esta asignatura ya esta en la lista, cambie el codigo.")
                cod=input("Dime el codigo de la asignatura: ")
        self.idasignatura.append(cod)
        nom=input("Dime el nombre de la asignatura: ")
        nom=nom.capitalize()
        self.nombre.append(nom)
        self.identificador.append(input("Dime el identificador del profesor que la imparte: "))
        self.curso.append(input("Dime el curso al que pertenece: "))
        self.horas_semanales.append(input (int("Dime el numero de horas semanales: ")))
        frase=self.idasignatura[-1]+";"+self.nombre[-1]+";"+self.identificador[-1]+";"+self.curso[-1]+self.horas_semanales[-1]
        archivo.write(frase+"\n")
        print("Ha añadido usted la asignatura "+self.nombre[-1]+" con un código "+self.idasignatura[-1]+" que la imparte el profesor con el codigo  "+self.identificador[-1]+" , su curso es  "+self.departamento[-1]+" y tiene "+self.horas_semanales[-1]+" horas semanales.")
        
        archivo.close()
    
    def borrar_asignatura(self):
        archivo= open("Asignatura.txt", "a+")
        contador=0
        bor = input("Que nombre quieres borrar?:")
        bor=bor.capitalize()
        for i in self.nombre:
            if i == bor:
                contador+=1
                pass
            else:
                frase=self.idasignatura[contador]+";"+self.nombre[contador]+";"+self.identificador[contador]+";"+self.curso[contador]+self.horas_semanales[contador]
                archivo.write(frase+"\n")
                contador+=1
        archivo.close()

    def importar_datos(self):
        archivo = open("Asignatura.txt","r")
        for lineas in archivo:
            lineas=lineas.strip("\n")
            lineas=lineas.split(";")
            asignatura.idasignatura.append(lineas[0])
            asignatura.nombre.append(lineas[1])
            asignatura.identificador.append(lineas[2])
            asignatura.curso.append(lineas[3])
            asignatura.horas_semanales.append(lineas[4])
        archivo.close()
    
    def modificar_asignatura(self):
        contador=0
        semaforo_modificar=True
        for i in lista_modificar_asignatura:
            print(i)
        modificar=int(input("Que opcion quieres cambiar: "))
        while semaforo_modificar == True:
            if modificar == 1:
                nom= input("Dime el nombre de la asignatura: ")
                nom=nom.capitalize()
                cod2= input("Dime el nuevo codigo:")
                for i in self.nombre:
                    if i == nom:
                        self.identificador[contador]=cod2
                        semaforo_modificar=False
                    contador+=1
            elif modificar == 2:
                nom= input("Dime el nombre de la asignatura: ")
                nom=nom.capitalize()
                nom2= input("Dime el nuevo nombre:")
                nom2=nom2.capitalize()
                for i in self.nombre:
                    if i == nom:
                        self.nombre[contador]=nom2
                        semaforo_modificar=False
                    contador+=1
            elif modificar == 3:
                nom= input("Dime el nombre de la asignatura: ")
                nom=nom.capitalize()
                ida= input("Dime el IdAsignatura nuevo:")
                for i in self.nombre:
                    if i == nom:
                        self.idasignatura[contador]=ida
                        semaforo_modificar=False
                    contador+=1  
            elif modificar == 4:
                nom= input("Dime el nombre de la asignatura ")
                nom=nom.capitalize()
                cur= input("Dime el nuevo curso:")
                for i in self.nombre:
                    if i == nom:
                        self.curso[contador]=cur
                        semaforo_modificar=False
                    contador+=1
            elif modificar == 5:
                nom= input("Dime el nombre de la asignatura ")
                nom=nom.capitalize()
                horas= input("Dime el nuevo numero de horas:")
                for i in self.nombre:
                    if i == nom:
                        self.horas_semanales[contador]=horas
                        semaforo_modificar=False
                    contador+=1
            elif modificar == 6:
                semaforo_modificar=False
            else:
                modificar=input("Esa opcion no es valida, ponga una opcion correcta :")
    
    def actualizar_asignatura(self):
        archivo = open("Asignatura.txt","a+")
        for i in range(len(self.nombre)):
            frase=self.idasignatura[i]+";"+self.nombre[i]+";"+self.identificador[i]+";"+self.curso[i]+self.horas_semanales[i]
            archivo.write(frase+"\n")
        archivo.close()
    
    def listado_asignatura(self):
        print("Identificador;Nombre;IdAsignatura;Curso;Horas_Semanales")
        for i in range(len(self.nombre)):
            print(self.identificador[i]+";"+self.nombre[i]+";"+self.idasignatura[i]+";"+self.curso[i]+";"+self.horas_semanales[i])
    
    def buscar_asignatura(self):
        contador=0
        semaforo_buscar=True
        for i in lista_modificar_asignatura:
            print(i)
        buscar = int(input("Que quieres buscar?:"))
        while semaforo_buscar == True:
            if buscar == 1:
                cod= input("Dime el codigo del profesor: ")
                for i in self.codigo:
                    if i == cod:
                        print(self.identificador[contador]+";"+self.nombre[contador]+";"+self.idasignatura[contador]+";"+self.curso[contador]+";"+self.horas_semanales[contador])
                        semaforo_buscar=False
                    contador+=1
            elif buscar == 2:
                nom= input("Dime el nombre de la asignatura: ")
                nom=nom.capitalize()
                for i in self.nombre:
                    if i == nom:
                        print(self.identificador[contador]+";"+self.nombre[contador]+";"+self.idasignatura[contador]+";"+self.curso[contador]+";"+self.horas_semanales[contador])
                        semaforo_buscar=False
                    contador+=1
            elif buscar == 3:
                tel= input("Dime el codigo IdAsignatura: ")
                for i in self.idasignatura:
                    if i == tel:
                        print(self.identificador[contador]+";"+self.nombre[contador]+";"+self.idasignatura[contador]+";"+self.curso[contador]+";"+self.horas_semanales[contador])
                        semaforo_buscar=False
                    contador+=1
            elif buscar == 4:
                dto= input("Dime el curso de la asignatura: ")
                for i in self.curso:
                    if i == dto:
                        print(self.identificador[contador]+";"+self.nombre[contador]+";"+self.idasignatura[contador]+";"+self.curso[contador]+";"+self.horas_semanales[contador])
                        semaforo_buscar=False
                    contador+=1
            elif buscar == 5:
                dto= input("Dime las horas semanales: ")
                for i in self.horas_semanales:
                    if i == dto:
                        print(self.identificador[contador]+";"+self.nombre[contador]+";"+self.idasignatura[contador]+";"+self.curso[contador]+";"+self.horas_semanales[contador])
                        semaforo_buscar=False
                    contador+=1
            elif buscar == 6:
                semaforo_buscar=False
            else:
                buscar=input("Esa opcion no es valida, ponga una opcion correcta :")

def importar_datos():
    profesor.importar_datos()
    alumno.importar_datos()
    asignatura.importar_datos()

def actualizar_datos():
    profesor.actualizar_profesores()
    alumno.actualizar_alumnos()
    asignatura.actualizar_asignatura()


def menu():
    semaforo=True
    
    while semaforo == True:
        actualizar_datos()
        print("Este es el programa de notas: ")
        for i in lista_menu:
            print(i)
        opcion=int(input("Que quieres hacer?: "))
        
        if opcion == 1:
            for i in lista_alta:
                print(i)
            semaforo_alta=True
            opcion_alta=int(input("Que opcion eliges: "))
            while semaforo_alta == True:
                if opcion_alta == 1:
                    alumno.alta_alumno()
                    semaforo_alta = False
                elif opcion_alta == 2:
                    profesor.alta_profesor()
                    semaforo_alta = False
                elif opcion_alta == 3:
                    asignatura.alta_asignatura()
                    semaforo_alta = False
                elif opcion_alta == 4:
                    semaforo_alta=False
                else:
                    opcion_alta = input("Esa opcion no es valida, ponga una opcion correcta :")
        elif opcion == 2:
            for i in lista_baja:
                print(i)
            semaforo_baja=True
            opcion_baja=int(input("Que opcion eliges: "))
            while semaforo_baja == True:
                if opcion_baja == 1:
                    alumno.borrar_alumno()
                    semaforo_baja = False
                elif opcion_baja == 2:
                    profesor.borrar_profesor()
                    semaforo_baja = False
                elif opcion_baja == 3:
                    asignatura.borrar_asignatura()
                    semaforo_baja = False
                elif opcion_baja == 4:
                    semaforo_baja=False
                else:
                    opcion_baja = input("Esa opcion no es valida, ponga una opcion correcta :")
        elif opcion == 3:
            for i in lista_modificar:
                print(i)
            semaforo_modificar=True
            opcion_modificar=int(input("De que quieres modificar: "))
            while semaforo_modificar == True:
                if opcion_modificar == 1:
                    alumno.modificar_alumno()
                    semaforo_modificar = False
                elif opcion_modificar == 2:
                    profesor.modificar_profesor()
                    semaforo_modificar = False
                elif opcion_modificar == 3:
                    asignatura.modificar_asignatura()
                    semaforo_modificar = False
                elif opcion_modificar == 4:
                    semaforo_modificar=False
                else:
                    opcion_modificar = input("Esa opcion no es valida, ponga una opcion correcta :")
        elif opcion == 4:
            for i in lista_listado:
                print (i)
            semaforo_listado=True
            opcion_listado=int(input("Dime de que quieres ver la lista: "))
            while semaforo_listado == True:
                if opcion_listado == 1:
                    alumno.listado_alumno()
                    semaforo_listado=False
                elif opcion_listado == 2:
                    profesor.listado_profesor()
                    semaforo_listado=False
                elif opcion_listado == 3:
                    asignatura.listado_asignatura()
                    semaforo_listado=False
                elif opcion_listado == 4:
                    semaforo_listado=False
                else:
                    opcion_listado = input("Esa opcion no es valida, ponga una opcion correcta :")
        elif opcion == 5:
            for i in lista_listado:
                print (i)
            semaforo_buscar=True
            opcion_buscar=int(input("Dime de donde quieres buscar: "))
            while semaforo_buscar == True:
                if opcion_buscar == 1:
                    alumno.buscar_alumno()
                    semaforo_buscar=False
                elif opcion_buscar == 2:
                    profesor.buscar_profesor()
                    opcion_buscar=False
                elif opcion_buscar == 3:
                    asignatura.buscar_asignatura()
                    opcion_buscar=False
                elif opcion_listado == 4:
                    opcion_buscar=False
                else:
                    opcion_buscar = input("Esa opcion no es valida, ponga una opcion correcta :")
        elif opcion == 6:
            semaforo = False
        else:
            opcion = input("Esa opcion no es valida, ponga una opcion correcta :")
        

    


lista_menu=["1- Dar de alta", "2- Dar de baja", "3- Modificar parametro" , "4- Listado ", "5- Buscar", "6- Salir"]
lista_alta=["1- Dar de alta alumno", "2- Dar de alta profesor", "3- Dar de alta asignatura", "4- Salir"]
lista_baja=["1- Dar de baja alumno", "2- Dar de baja profesor", "3- Dar de baja asignatura", "4- Salir"]
lista_listado=["1- Alumnos", "2- Profesores", "3- Asignaturas", "4- Salir"]
lista_modificar=["1- Alumnos", "2- Profesores", "3- Asignaturas", "4- Salir"]
lista_modificar_alumno=["1- Identificador", "2- Nombre", "3- Telefono", "4- Curso", "5- Salir"]
lista_modificar_profesor=["1- Identificador", "2- Nombre", "3- Telefono", "4- Departamento", "5- Salir"]
lista_modificar_asignatura=["1-Identificador", "2- Nombre", "3- IdAsignatura", "4- Curso", "5- Horas semanales", "6- Salir"]
profesor=Profesor([],[],[],[])
alumno=Alumno([],[],[],[])
asignatura=Asignatura([],[],[],[],[])
importar_datos()
menu()
