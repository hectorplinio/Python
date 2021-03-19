print("HOLA, DIME 3 NUMEROS AL AZAR")
numero1  = input()
numero2 = input()
numero3  = input()
if numero1 > numero2 and numero1 > numero3:
  num_mayor = numero1
  
elif numero2 > numero1 and numero2 > numero3:
  num_mayor = numero2

elif numero3 > numero1 and numero3 > numero2:
  num_mayor = numero3
 





if numero1 < numero2 and numero1 < numero3:
  num_menor = numero1
  
elif numero2 < numero1 and numero2 < numero3:
  num_menor = numero2

elif numero3 < numero1 and numero3 < numero2:
  num_menor = numero3



if numero1 > numero2 and numero1 > numero3 and numero2 > numero3:
  num_medio = numero2

elif numero1 > numero2 and numero1 > numero3 and numero3 > numero2:
  num_medio = numero3

  
elif numero2 > numero1 and numero2 > numero3 and numero3 > numero1:
  num_medio = numero3

elif numero2 > numero1 and numero2 > numero3 and numero1 > numero3:
  num_medio = numero1
  
elif numero3 > numero1 and numero3 > numero2 and numero1 > numero2:
  num_medio = numero1

elif numero3 > numero1 and numero3 > numero2 and numero2 > numero1:
  num_medio = numero2
  
  
 
 

print ("Mayor:"+ str (num_mayor))
print ("Menor:"+ str (num_menor))
print ("Medio:"+ str (num_medio))

