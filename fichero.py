"""diccionario={"one":"uno","two":"dos", "three":"tres"}

print(diccionario["one"])
print(len(diccionario))
"one" in diccionario"""

palabra= "brontosaurio"
d=dict()
for c in palabra:
    if c not in d:
        d[c]=1
    else:
        d[c] = d[c] + 1
print(d)
for j in d:
    print(j, "---->", d[j])