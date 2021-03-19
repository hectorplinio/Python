"""
lista1 = [1,3,3,1]
lista2 = [1,4,6,4,1]
lista3 = []
n=0
lista3.append (1)
for i in range (4):
  x= lista2 [n] + lista2 [n+1]
  lista3.append (x)
  n= n+1
lista3.append (1)
print (lista3)
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

    operaciones = operaciones+1
    n=0
    lista_m.append (1)
    lista_p=lista_m
    lista_m = []
    print (lista_p)