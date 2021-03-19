#Ejercicio 1
print ("Indique un número:")
numero = int(input())

if (numero % 2) == 0:
  print(numero, " es par")
else:
  print(numero, " es impar")





#Ejercicio 2
print ("Pon tu nota:")
nota = int(input())

if nota < 5:
  print ("INSUFICIENTE")
elif nota < 6:
  print ("SUFICIENTE")
elif nota < 7:
  print ("BIEN")
elif nota < 9:
  print ("NOTABLE")
elif nota >= 9 or nota <= 10:
  print ("SOBRESALIENTE")
else:
  print ("NOTA NO VALIDA")


#Ejercicio 4
print ("Escriba 2 número:")
n1 = int(input())
print ("¿Cuantos numeros van a seguir?")
n2 = int(input())

resultado =""
while n2>0:
  n1 = n1 + 1
  n2 = n2 - 1
  if resultado == "":
    resultado = str(n1)
  else:
    resultado = resultado + "," + str(n1)

resultado = resultado + "."
  
print (resultado)


#Ejercico 6
exponente = 0

base = int(input("Dame una base:"))

while exponente <= 0:
  exponente = int (input("Dame un exponente:"))

resultado = 1
while (exponente >0):
  exponente = exponente - 1
  resultado = resultado * base
  print ("Resultado -->"+ str(resultado))

print (resultado)

#Otra forma

import math

n1 = int (input("Escriba un numero:"))

n2 = int (input("Escriba un segundo para elevar:"))

while n2 < 0:
  print ("Error, ponga un número positivo")
  n2 = int( input("Escriba un número para elevar:"))

print ("El resultado es:"+ str(n1**n2)) 

#Ejercicio 7 cuenta los pares hasta el 100
i = 2
while i<=100:
  print(i)
  print (",") 
  i = i+2
#Cuenta los pares hasta el 49
j = 2
for i= 0 to 49:
  print (j)
  print (",")
  j = j+2
  
#Ejercicio 8 Te dice que eres el 1, el 2 asi hasta que llega al numero 5, que se rompe la condicion.
numbers = (1,2,3,4,5,6,7,8,9,10)
value = 1
while value in numbers:
  if value< 5:
    print ("I'm # " + str (value))
    value = value+1
    continue
    print ("I'm in the if-condition, why are you ignoring me?")
  elif value ==5:
    break

print ("I'have reached the last statement in the program and need to exit!")

#Ejercicio 9
print 
nombre = input("Hola, escribe tu nombre:")
n1 = int(input ("Ahora escribe un número:"))
n2 = int(input ("Escribe un segundo número:"))
texto =""
while n1 > 0:
  n1 = n1-1
  if texto == "":
    texto = str(nombre)
  else:
      texto = texto + " " + nombre
while n2 > 0:
  print (texto)
  n2 = n2-1

#Ejercicio 10

resultado =""
contador = 200
while contador > 0:
    if contador %3==0:
        resultado =resultado + "X"
    else:
        resultado = resultado + "O"

    contador = contador - 1
    if contador % 20 == 0:
        print ( resultado)
        resultado =""

#Ejercicio 11

h = int(input("Escriba la altura de la piramide:"))

for i in range(h+1):
  if i%2==0:
    print ("B"*i)
  else:
    print ("A"*i)

#Ejercicio 11
h = int(input("Escriba la altura de la piramide:"))

for i in range(1,h+1):
  resultado = ""
  if i%2==0:
    caracter ="B"
  else:
    caracter = "A"
  for j in range (i):
    resultado+=caracter
  print (resultado)
   

#Ejercicio 12
h = int(input("Escriba la altura de la piramide:"))

for asteriscos in range (h):
  for e in range (h-asteriscos-1):
    print("-", end="")
  
  for e in range(2*asteriscos +1):
    print ("X", end="")

  for e in range (h-asteriscos-1):
    print ("-", end="")
  
  print()

#Ejercicio 12
equis = "X"
filas = int(input("Filas:"))
while filas>0:
  guiones = ""

  for i in range (filas-1):
    guiones = guiones + "-"
  filas = filas-1

  print (guiones + equis + guiones)
  equis = equis + "XX"
