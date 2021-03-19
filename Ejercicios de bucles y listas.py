"""
num = int(input("Ingrese un número para ver la sucesión: "))
n1 = 0
n2 = 1


for i in range (num):
  if i %2 ==0:
    n1= n1+n2
    print (n1)
  if i %2!=0:
    n2=n1+n2
    print (n2)
"""
lista_p = []
lista_m = []
num_lineas =int(input("Escribe un número:"))

n=0
operaciones = 1
for i in range (num_lineas):
  if i == 0:
    lista_p = [1]
    print (lista_p)
  elif i ==1:
    lista_p = [1,1]
    print (lista_p)
  else:
    lista_m.append(1)
    for i in range (operaciones):
      x= lista_p [n] + lista_p [n+1]
      lista_m.append (x)
      n= n+1
    
    n=0
    operaciones = operaciones+1
    lista_m.append (1)
    lista_p = lista_m
    lista_m =[]
    print (lista_p)