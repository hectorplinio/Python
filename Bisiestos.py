#Escribir un programa que permita al usuario ingresar dos años y luego imprima todos los años en ese rango, que sean bisiestos. Nota: para que un año sea bisiesto debe ser divisible por 4 y no debe ser divisible por 100, excepto que también sea divisible por 400.
num1 = int( input("Escriba un año:"))
num2 = int( input("Escriba un segundo año:"))
lista_p = []


for i in range (num1,num2+1):
  if num1 %4==0 and (num1 %100!=0 or num1 %400==0):
    lista_p.append(num1)
    num1=num1+1
    
  else: 
    num1 = num1 + 1

print (lista_p)
print ("Esta es la lista de bisiestos entre tus 2 años.")