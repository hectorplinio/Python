lista_mapa=[]
lista_mapa_2=[]
x=0
y=0
x=int(input("Escribe una altura: "))
y=int(input("Escribe una altura: "))
f=0

for i in range (x):
    lista_mapa.append([])
    for j in range (y):
        f+=1
        lista_mapa[i].append(f)
for i in range (len(lista_mapa)):
    for j in lista_mapa[i]:
        print("{:3}".format(j),end="")
    print()