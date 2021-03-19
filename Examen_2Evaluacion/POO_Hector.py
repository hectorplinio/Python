class Vehiculo():
    def __init__(self,matricula, modelo, potencia):
        self.matricula=matricula
        self.modelo=modelo
        self.potencia=potencia

    def alta_vehiculo(self):
        print("Vamos a dar de alta un vehiculo.")
        self.matricula.append(input("Digame el numero de matricula: "))
        mod=input("Digame el modelo: ")
        mod=mod.capitalize()
        self.modelo.append(mod)
        self.potencia.append(input("Digame la potencia en CV: "))
        

class Taxi(Vehiculo):
    def __init__(self,matricula, modelo, potencia, numero_licencia):
        Vehiculo.__init__(self,matricula, modelo, potencia)
        self.numero_licencia=numero_licencia

    def alta_taxi(self):
        vehiculo.alta_vehiculo()
        self.matricula.append(vehiculo.matricula[-1])
        self.modelo.append(vehiculo.modelo[-1])
        self.potencia.append(vehiculo.potencia[-1])
        self.numero_licencia.append(input("Digame el numero de licencia: "))
    
    def listado_taxi(self):
        x=0
        print("Matricula;Modelo;Potencia;Numero_licencia")
        for i in self.matricula:
            print(self.matricula[x]+";"+self.modelo[x]+";"+self.potencia[x]+";"+self.numero_licencia[x])
            x=x+1
        
    def modificar_taxi(self):
        print("Has entrado en el modificador, estas son las opciones: ")
        for i in lista_modificar_taxi:
            print(i)
        opcion=int(input("Que quieres modificar?: "))
        semaforo_modificar=True
        while semaforo_modificar ==True:
            if opcion == 1:
                contador=0
                mat=input("Escriba la matricula antigua: ")
                mat2=input("Escriba la nueva matricula: ")
                for i in self.matricula:
                    if i == mat:
                        self.matricula[contador]=mat2
                    else:
                        contador+=1
                semaforo_modificar=False
            elif opcion == 2:
                contador=0
                mat=input("Escriba la matricula: ")
                mat=mat.capitalize()
                mat2=input("Escriba el nuevo modelo: ")
                mat2=mat2.capitalize()
                for i in self.matricula:
                    if i == mat:
                        self.modelo[contador]=mat2
                    else:
                        contador+=1
                semaforo_modificar=False
            elif opcion == 3:
                contador=0
                mat=input("Escriba la matricula: ")
                mat2=input("Escriba la nueva potencia: ")
                for i in self.matricula:
                    if i == mat:
                        self.potencia[contador]=mat2
                    else:
                        contador+=1
                semaforo_modificar=False
            elif opcion == 4:
                contador=0
                mat=input("Escriba el numero de licencia: ")
                mat2=input("Escriba el nuevo numero de licencia: ")
                for i in self.numero_licencia:
                    if i == mat:
                        self.numero_licencia[contador]=mat2
                    else:
                        contador+=1
                semaforo_modificar=False
            elif opcion == 5:
                semaforo_modificar=False
            else:
                opcion=int(input("Escriba una opcion correcta para modificar?: "))
    
    def borrar_taxi(self):
        print("Has entrado en el borrador, estas son las opciones: ")
        for i in lista_modificar_taxi:
            print(i)
        opcion=int(input("Dame el valor del vehiculo quieres borrar?: "))
        semaforo_borrar=True
        while semaforo_borrar ==True:
            if opcion == 1:
                contador=0
                mat=input("Escriba la matricula: ")
                for i in self.matricula:
                    if i == mat:
                        self.matricula[contador]=""
                        print("Has borrado correctamente la matricula")
                    else:
                        contador+=1
                semaforo_borrar=False
            elif opcion == 2:
                contador=0
                mat2=input("Escriba la matricula: ")
                mat2=mat2.capitalize()
                for i in self.modelo:
                    if i == mat:
                        self.modelo[contador]=""
                        print("Has borrado correctamente el modelo")
                    else:
                        contador+=1
                semaforo_borrar=False
            elif opcion == 3:
                contador=0
                mat=input("Escriba la matricula: ")
                for i in self.matricula:
                    if i == mat:
                        self.potencia[contador]=""
                        print("Has borrado correctamente la potencia")
                    else:
                        contador+=1
                semaforo_borrar=False
            elif opcion == 4:
                contador=0
                mat=input("Escriba el numero de licencia: ")
                for i in self.numero_licencia:
                    if i == mat:
                        self.numero_licencia[contador]=""
                        print("Has borrado correctamente el numer de licencia")
                    else:
                        contador+=1
                semaforo_borrar=False
            elif opcion == 5:
                semaforo_borrar=False
            else:
                opcion=int(input("Escriba una opcion correcta para borrar?: "))

    def buscar_taxi(self):
        print("Has entrado en el buscador, estas son las opciones: ")
        for i in lista_modificar_taxi:
            print(i)
        opcion=int(input("Dame el valor del vehiculo quieres borrar?: "))
        semaforo_buscar=True
        while semaforo_buscar ==True:
            if opcion == 1:
                contador=0
                mat=input("Escriba la matricula: ")
                for i in self.matricula:
                    if i == mat:
                        print("Matricula;Modelo;Potencia;Numero_licencia")
                        print(self.matricula[contador]+";"+self.modelo[contador]+";"+self.potencia[contador]+";"+self.numero_licencia[contador])
                    else:
                        contador+=1
                semaforo_buscar=False
            elif opcion == 2:
                contador=0
                mat2=input("Escriba el modelo: ")
                mat2=mat2.capitalize()
                for i in self.modelo:
                    if i == mat2:
                        print("Matricula;Modelo;Potencia;Numero_licencia")
                        print(self.matricula[contador]+";"+self.modelo[contador]+";"+self.potencia[contador]+";"+self.numero_licencia[contador])
                    else:
                        contador+=1
                semaforo_buscar=False
            elif opcion == 3:
                contador=0
                mat=input("Escriba la potencia: ")
                for i in self.potencia:
                    if i == mat:
                        print("Matricula;Modelo;Potencia;Numero_licencia")
                        print(self.matricula[contador]+";"+self.modelo[contador]+";"+self.potencia[contador]+";"+self.numero_licencia[contador])
                    else:
                        contador+=1
                semaforo_buscar=False
            elif opcion == 4:
                contador=0
                mat=input("Escriba el numero de licencia: ")
                for i in self.numero_plazas:
                    if i == mat:
                        print("Matricula;Modelo;Potencia;Numero_licencia")
                        print(self.matricula[contador]+";"+self.modelo[contador]+";"+self.potencia[contador]+";"+self.numero_licencia[contador])
                    else:
                        contador+=1
                semaforo_buscar=False
            elif opcion == 5:
                semaforo_buscar=False
            else:
                opcion=int(input("Escriba una opcion correcta para buscar?: "))



class Autobus(Vehiculo):
    def __init__(self,matricula, modelo, potencia, numero_plazas):
        Vehiculo.__init__(self,matricula, modelo, potencia)
        self.numero_plazas=numero_plazas
    
    def alta_autobus(self):
        vehiculo.alta_vehiculo()
        self.matricula.append(vehiculo.matricula[-1])
        self.modelo.append(vehiculo.modelo[-1])
        self.potencia.append(vehiculo.potencia[-1])
        self.numero_plazas.append(input("Digame el numero de plazas: "))
    
    def listado_autobus(self):
        x=0
        print("Matricula;Modelo;Potencia;Numero_plazas")
        for i in self.matricula:
            print(self.matricula[x]+";"+self.modelo[x]+";"+self.potencia[x]+";"+self.numero_plazas[x])
            x=x+1

    def modificar_autobus(self):
        print("Has entrado en el modificador, estas son las opciones: ")
        for i in lista_modificar_autobus:
            print(i)
        opcion=int(input("Que quieres modificar?: "))
        semaforo_modificar=True
        while semaforo_modificar ==True:
            if opcion == 1:
                contador=0
                mat=input("Escriba la matricula antigua: ")
                mat2=input("Escriba la nueva matricula: ")
                for i in self.matricula:
                    if i == mat:
                        self.matricula[contador]=mat2
                    else:
                        contador+=1
                semaforo_modificar=False
            elif opcion == 2:
                contador=0
                mat=input("Escriba la matricula: ")
                mat=mat.capitalize()
                mat2=input("Escriba el nuevo modelo: ")
                mat2=mat2.capitalize()
                for i in self.matricula:
                    if i == mat:
                        self.modelo[contador]=mat2
                    else:
                        contador+=1
                semaforo_modificar=False
            elif opcion == 3:
                contador=0
                mat=input("Escriba la matricula: ")
                mat2=input("Escriba la nueva potencia: ")
                for i in self.matricula:
                    if i == mat:
                        self.potencia[contador]=mat2
                    else:
                        contador+=1
                semaforo_modificar=False
            elif opcion == 4:
                contador=0
                mat=input("Escriba el numero de plazas: ")
                mat2=input("Escriba el nuevo numero de plazas: ")
                for i in self.numero_plazas:
                    if i == mat:
                        self.numero_plazas[contador]=mat2
                    else:
                        contador+=1
                semaforo_modificar=False
            elif opcion == 5:
                semaforo_modificar=False
            else:
                opcion=int(input("Escriba una opcion correcta para modificar?: "))


    def borrar_autobus(self):
        print("Has entrado en el borrador, estas son las opciones: ")
        for i in lista_modificar_autobus:
            print(i)
        opcion=int(input("Dame el valor del vehiculo quieres borrar?: "))
        semaforo_borrar=True
        while semaforo_borrar ==True:
            if opcion == 1:
                contador=0
                mat=input("Escriba la matricula: ")
                for i in self.matricula:
                    if i == mat:
                        self.matricula[contador]=""
                        print("Has borrado correctamente la matricula")
                    else:
                        contador+=1
                semaforo_borrar=False
            elif opcion == 2:
                contador=0
                mat2=input("Escriba la matricula: ")
                mat2=mat2.capitalize()
                for i in self.matricula:
                    if i == mat:
                        self.modelo[contador]=""
                        print("Has borrado correctamente el modelo")
                    else:
                        contador+=1
                semaforo_borrar=False
            elif opcion == 3:
                contador=0
                mat=input("Escriba la matricula: ")
                for i in self.matricula:
                    if i == mat:
                        self.potencia[contador]=""
                        print("Has borrado correctamente la potencia")
                    else:
                        contador+=1
                semaforo_borrar=False
            elif opcion == 4:
                contador=0
                mat=input("Escriba la matricula: ")
                for i in self.matricula:
                    if i == mat:
                        self.numero_plazas[contador]=""
                        print("Has borrado correctamente el numero de plazas")
                    else:
                        contador+=1
                semaforo_borrar=False
            elif opcion == 5:
                semaforo_borrar=False
            else:
                opcion=int(input("Escriba una opcion correcta para borrar?: "))

    def buscar_autobus(self):
        print("Has entrado en el buscador, estas son las opciones: ")
        for i in lista_modificar_autobus:
            print(i)
        opcion=int(input("Dame el valor del vehiculo quieres borrar?: "))
        semaforo_buscar=True
        while semaforo_buscar ==True:
            if opcion == 1:
                contador=0
                mat=input("Escriba la matricula: ")
                for i in self.matricula:
                    if i == mat:
                        print("Matricula;Modelo;Potencia;Numero_plazas")
                        print(self.matricula[contador]+";"+self.modelo[contador]+";"+self.potencia[contador]+";"+self.numero_plazas[contador])
                    else:
                        contador+=1
                semaforo_buscar=False
            elif opcion == 2:
                contador=0
                mat2=input("Escriba el modelo: ")
                mat2=mat2.capitalize()
                for i in self.modelo:
                    if i == mat:
                        print("Matricula;Modelo;Potencia;Numero_plazas")
                        print(self.matricula[contador]+";"+self.modelo[contador]+";"+self.potencia[contador]+";"+self.numero_plazas[contador])
                    else:
                        contador+=1
                semaforo_buscar=False
            elif opcion == 3:
                contador=0
                mat=input("Escriba la potencia: ")
                for i in self.potencia:
                    if i == mat:
                        print("Matricula;Modelo;Potencia;Numero_plazas")
                        print(self.matricula[contador]+";"+self.modelo[contador]+";"+self.potencia[contador]+";"+self.numero_plazas[contador])
                    else:
                        contador+=1
                semaforo_buscar=False
            elif opcion == 4:
                contador=0
                mat=input("Escriba el numero de plazas: ")
                for i in self.numero_plazas:
                    if i == mat:
                        print("Matricula;Modelo;Potencia;Numero_plazas")
                        print(self.matricula[contador]+";"+self.modelo[contador]+";"+self.potencia[contador]+";"+self.numero_plazas[contador])
                    else:
                        contador+=1
                semaforo_buscar=False
            elif opcion == 5:
                semaforo_buscar=False
            else:
                opcion=int(input("Escriba una opcion correcta para buscar?: "))


lista_menu=["1- Añadir vehiculo", "2- Listado vehiculos ", "3- Modificar valores", "4- Borrar vehiculo", "5- Buscar","6- Salir"]
lista_alta=["1- Añadir taxi", "2- Añadir autobus", "3- Salir"]
lista_listado=["1- Taxi", "2- Autobus", "3- Salir"]
lista_modificar_taxi=["1- Matricula", "2- Modelo", "3- Potencia", "4- Numero licencia", "5- Salir"]
lista_modificar_autobus=["1- Matricula", "2- Modelo", "3- Potencia", "4- Numero plazas", "5- Salir"]
vehiculo=Vehiculo([],[],[])
taxi=Taxi([],[],[],[])
autobus=Autobus([],[],[],[])
def menu():
    semaforo=True
    while semaforo == True:
        print("Bienvenido al menu de consultas de creacion de vehiculos.")
        for i in lista_menu:
            print(i)
        opcion=int(input("Seleccione una opcion para empezar: "))
        if opcion == 1:
            semaforo_alta=True
            while semaforo_alta==True:
                for i in lista_alta:
                    print(i)
                opcion_alta=int(input("Seleccione una opcion para empezar: "))
                if opcion_alta == 1:
                    taxi.alta_taxi()
                    semaforo_alta=False
                elif opcion_alta == 2:
                    autobus.alta_autobus()
                    semaforo_alta=False
                elif opcion_alta == 3:
                    semaforo_alta=False
                else:
                    opcion_alta=int(input("Seleccione una opcion valida."))
        elif opcion == 2:
            semaforo_listado=True
            while semaforo_listado==True:
                for i in lista_listado:
                    print(i)
                opcion_listado=int(input("Seleccione una opcion para empezar."))
                if opcion_listado == 1:
                    taxi.listado_taxi()
                    semaforo_listado=False
                elif opcion_listado == 2:
                    autobus.listado_autobus()
                    semaforo_listado=False
                elif opcion_listado == 3:
                    semaforo_listado=False
                else:
                    opcion_alta=int(input("Seleccione una opcion valida."))
        elif opcion == 3:
            semaforo_modificar=True
            while semaforo_modificar==True:
                for i in lista_listado:
                    print(i)
                opcion_modificar=int(input("Seleccione una opcion para empezar ha modificar."))
                if opcion_modificar== 1:
                    taxi.modificar_taxi()
                    semaforo_modificar=False
                elif opcion_modificar == 2:
                    autobus.modificar_autobus()
                    semaforo_modificar=False
                elif opcion_modificar == 3:
                    semaforo_modificar=False
                else:
                    opcion_alta=int(input("Seleccione una opcion valida."))
        elif opcion == 4:
            semaforo_borrar=True
            while semaforo_borrar==True:
                for i in lista_listado:
                    print(i)
                opcion_borrar=int(input("Seleccione una opcion para empezar ha borrar."))
                if opcion_borrar== 1:
                    taxi.borrar_taxi()
                    semaforo_borrar=False
                elif opcion_borrar == 2:
                    autobus.borrar_autobus()
                    semaforo_borrar=False
                elif opcion_borrar == 3:
                    semaforo_borrar=False
                else:
                    opcion_alta=int(input("Seleccione una opcion valida."))
        elif opcion == 5:
            semaforo_buscar=True
            while semaforo_buscar==True:
                for i in lista_listado:
                    print(i)
                opcion_buscar=int(input("Seleccione una opcion para empezar ha borrar."))
                if opcion_buscar== 1:
                    taxi.buscar_taxi()
                    semaforo_buscar=False
                elif opcion_buscar == 2:
                    autobus.buscar_autobus()
                    semaforo_buscar=False
                elif opcion_buscar == 3:
                    semaforo_buscar=False
                else:
                    opcion_alta=int(input("Seleccione una opcion valida."))
        elif opcion == 6:
            semaforo=False
        else:
            opcion=int(input("Seleccione una opcion correcta empezar."))
menu()