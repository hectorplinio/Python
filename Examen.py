memoria=[0,0,0,0,0,0,0,0,0,0]
instruccion=""
pantalla =0
semaforo ="rojo"

def MostrarMemoria():
    print(memoria)

def Guarda():
    posicion= float(input("memoria:"))
    memoria[posicion]=pantalla

def Memoria():
    posicion= float(input("memoria:"))
    return(memoria[posicion])
def MemoriaNumero ():
    numero= float(input("numero:"))
    if numero == "memoria":                                 
        return(Memoria())
    else:
        return (numero)

while semaforo=="rojo":
    try:
        pantalla = float(input("numero:"))
        semaforo = "verde"
    except:
        print ("TIENES QUE ESCRIBIR UN NUMERO")

def ayuda():
    lista=["+","-","*", "/","%", "--", "!", "Pot", "=", "salir"]
    for j in lista:
        print(j)

def suma():
    n1= float(input("numero:"))
    return (pantalla+n1)

def resta():
    n1= float(input("numero:"))
    return (pantalla-n1)

def multiplica():
    n1= float(input("numero:"))
    return (pantalla*n1)

def division():
    n1= float(input("numero:"))
    return (pantalla/n1)

def resto():
    n1= float(input("numero:"))
    return (pantalla//n1)

def negativo():
    return (pantalla*-1)

def potencia():
    n1= float(input("numero:"))
    return (pantalla**n1)

def factorial():
    resultado=pantalla
    for i in range(1,pantalla):
        resultado=resultado*i
    return(resultado)


while instruccion !="salir":
    print ("Resultado: ", pantalla)
    instruccion= input("Operacion:")
    if instruccion =="ayuda":
        ayuda()
    elif instruccion =="+":
        pantalla =suma()
    elif instruccion =="-":
        pantalla =resta()
    elif instruccion =="*":
        pantalla =multiplica()
    elif instruccion =="/":
        pantalla =division()
    elif instruccion =="%":
        pantalla =resto()
    elif instruccion =="--":
        pantalla =negativo()
    elif instruccion =="!":
        pantalla =factorial()
    elif instruccion =="Pot":
        pantalla =potencia()
    elif instruccion== "MostrarMemoria":
        pantalla = MostrarMemoria()
    