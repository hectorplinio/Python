x = str(input("Dime una palabra:"))
lista_pares = []
lista_impares = []
z=("SALIR")
contador=0
while x!=z:
  if contador %2==0:
      lista_pares.append(x)
      x = str(input("Dime una palabra:"))
      contador += 1
  if x==z:
    print (lista_pares)
    print (lista_impares)
    break
    
  if contador %2!=0:
      lista_impares.append(x)
      x = str(input("Dime una palabra:"))
      contador += 1
  if x==z:
    print (lista_pares)
    print (lista_impares)
    break
    
