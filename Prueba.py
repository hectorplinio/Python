lista_o=["+","-", "*", "/", "%","--", "!", "Pot","=", "Salir", "Guarda", "MonstrarMemoria", "memoria", "AYUDA"]
print(lista_o)
lista_h=[]
lista_m=[0,0,0,0,0,0,0,0,0,0]
lista_f=[]
z=input("Operacion:")
x=int(input("Numero:"))
y=int(input("Numero:"))

while z!="Salir":
    

    

    if z=="+":
        #num3=int(input("Numero:"))
        RESULTADO=x+y
        print ("RESULTADO:" + str(RESULTADO))
        lista_h.append("+")
        z=input("Operacion:")
        
        
        
    if z=="-":
        num3=int(input("Numero:"))
        RESULTADO = RESULTADO - (num3)
        print ("RESULTADO:" + str(RESULTADO))
        lista_h.append("-")
        z=input("Operacion:")
        
    if z=="*":
        num3=int(input("Numero:"))
        RESULTADO= RESULTADO * (num3)
        print ("RESULTADO:" + str(RESULTADO))
        lista_h.append("*")
        z=input("Operacion:")
        
    if z=="/":
        RESULTADO = RESULTADO//(num3)
        print ("RESULTADO:" + str(RESULTADO))
        lista_h.append("/")
        z=input("Operacion:")
        num3=int(input("Numero:"))
    if z=="%":
        RESULTADO = RESULTADO % (num3)
        print ("RESULTADO:" + str(RESULTADO))
        lista_h.append("%")
        z=input("Operacion:")
        num3=int(input("Numero:"))
    if z=="--":
        RESULTADO = RESULTADO - 2*(RESULTADO)
        print ("RESULTADO:" + str(RESULTADO))
        lista_h.append("--")
        z=input("Operacion:")
        num3=int(input("Numero:"))
    if z=="!":
        
        RESULTADO=RESULTADO*(RESULTADO-1)
        
        lista_h.append("!")
        print ("RESULTADO:" + str(RESULTADO))
        z=input("Operacion:")
        num3=int(input("Numero:"))
    if z=="Pot":
    
        while num3>0:
            RESULTADO = RESULTADO*(RESULTADO)
            num3=num3-1
    
        lista_h.append("Pot")
        print ("RESULTADO:" + str(RESULTADO))
        z=input("Operacion:")
        num3=int(input("Numero:"))
    if z=="=":
        z=lista_h[-1]

    if z=="Guarda":
        p=int(input("Posicion:"))
        lista_m[p]= (RESULTADO)
        print ("RESULTADO:" + str(RESULTADO))
        z=input("Operacion:")

    if z=="MonstrarMemoria":
        print (lista_m)
        print ("RESULTADO:" + str(RESULTADO))
        z=input("Operacion:")

    if z=="memoria":
        t=input("Memoria:")
        lista_m[t]=lista_m(t)
        print ("RESULTADO:" + str(RESULTADO))
        z=input("Operacion:")
    if z=="AYUDA":
        print (lista_o)
        z=input("Operacion:")
    
    if z=="SALIR":
        break  
    
    