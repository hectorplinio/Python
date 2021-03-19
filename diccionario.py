numero=int(input("Escriba el número final:"))
d=dict()
for i in range(numero+1):
    if i <= numero and not i==0:
        d[i]=i*i
    else:
        pass
print(d)