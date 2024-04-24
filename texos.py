#tratamiento de strings

tx="es_una_cadena_de_texto"
tx1="abcdefghijklmnopqrstwxyz"
tx2="guitarra"
tx3="teclado"
nm="jIbrAn rOsAs"

print(tx.split("_")) #separa el texto por un caracter específico
print(tx1.upper()) #convierte todo a mayusculas
print(tx1.isupper()) #¿todo es mayuscula?
print(tx1.lower()) #convierte todo a mayusculas
print(tx1.islower()) #¿todo es miniscula?
print(tx2[2:])  #muestra el caracter del indice
print(tx2.endswith(tx3)) #muestra true o false si la cadena termina con la cadena parámetro
print(type(len(tx2))) #muestra el tipo de dato del resultado de len que es el tamaño de la cadena
txt=tx2+" y el "+tx3 #concatenación
print(nm.title(), "toca la", txt) #capitalize() 1ra mayus, swapcase() mayus a minus y viceversa.


txt1="     "+tx2+"     "

print(txt1.strip()) #elimina blancos
print(txt1.rstrip()) #"" de la derecha
print(txt1.lstrip()) #"" de la izquierda
print(tx1.find("jkl")) #"" indice de la coincidencia de la cadena
    
