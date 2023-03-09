
from math import sqrt

print("------------------------------------------------")
print("---------RESOLVER EC. DE PRIMER GRADO-----------")
print("------------------------------------------------")

#INPUT

m = int(input("Ingrese el valor m: " ))
b = int(input("Ingrese el valor b: " ))

#PROCESSING

if m==0 :

    print ("el valor de la recta no toca el eje x, por lo tanto su valor es: " + str(b))

else :
     
     c = -b/m
     print ("el punto donde x=0, Y es: "+ str(c))