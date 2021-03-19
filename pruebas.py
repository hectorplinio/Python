lista_prueba=[]
x=int(input("Dime la longitud:"))
y=int(input("Dime la altura:"))
f=0

for i in range(x):
    lista_prueba.append([])
    for j in range (y):
        f+=1
        lista_prueba[i].append(f)
for i in range (len(lista_prueba)): 
    for j in lista_prueba[i]:  
        print("{:3}".format(j),end="")
    print()

