import os
#x1 = int(input("Introduce un número para empezar a jugar:"))
import random
x1=random.randint(0, 1000)

while x1<0:
  x1= int(input("Error introduce un número positivo para empezar a jugar:"))
  os.system ("clear")
 
os.system ("clear")
contador = 1
 
    
x2 = int(input("Comienza el juego, intenta adivinar mi número:"))

while x1!=x2:
  if x2<x1:
    print ("Fallaste, es mayor")
    contador = contador +1
    x2= int(input ("Prueba otra vez:"))

  if x2>x1:
    print ("Fallaste, es menor")
    contador = contador +1
    x2= int(input ("Prueba otra vez:"))

  
print ("Has acertado, te ha costado "  + str(contador) + " veces.")
  
