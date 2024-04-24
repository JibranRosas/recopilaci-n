print('el cilo while continua minetras la condición sea cierta\n')
print("un ciclo while que muestra los numeros del 0 al 5")

c=0
while c<=5:
    print(c)
    c+=1
    
print("\n lo mismo pero con while not y entregando una lista \n")
j=0
l1=[]
while not j>5:
    l1.append(j)
    j+=1
print(l1)

print('\n ahora la vamos a iterarla en un ciclo for: \n')

for h in enumerate(l1):
    print(h)

print('\n tambien podermos acceder a tuplas desde un for: \n')

t1=tuple(l1)
print('\n tenemos la tupla: \n')
print(t1)
print('\n ahora la iteramos en un for: \n')

for g in t1:
    print(g)


print("\n econtrar una coincidencia de caracteres en 2 palabras\n")

p1="terminación"
p2="programación"


for i in range(len(p2)):
    x=p1.endswith(p2[i:])
    if x==True:
        print(f'la cadena \" {p2[i:]} \" coincide al final de ambas palabras')
        break
    else:
        continue

print("\n lo mismo pero con un while \n")

#con while

k=0
while not p1.endswith(p2[k:]):
    k+=1
print(f'la cadena \" {p2[k:]} \" coincide al final de ambas palabras \n')
print('\n deletrea una palabra \n')

palabra="superfrajilistico"

for letras in palabra:
    print(letras)

print('\n ahora veamos un diccionario \n')

d1={"anahi":25,"jibran":26,"zeus":16,"jess":17}
print(d1)
print(d1.keys())
print(d1["anahi"])
le=[]
ln=[]
for persona in d1.keys():
    print(f'{persona} tiene {d1[persona]} años\n')
    le.append(d1[persona])
    ln.append(persona)

te=tuple(le)
tn=tuple(ln)

print(le)   
print(ln)

print('\n se convierte en tupla para no poder conmutarlas\n')
print(te)   
print(tn)

print('\n ¿quien es menor de edad?\n')
for edad in te:
    if edad < 18:
        per=tn[te.index(edad)]
        print(f'\n {per} es menor de edad\n')
        

        

 
    