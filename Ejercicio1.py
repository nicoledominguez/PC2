a = int(input("Ingrese numero"))
b = int(input("Ingrese numero"))
c = int(input("Ingrese numero"))
d = int(input("Ingrese numero"))
e = int(input("Ingrese numero"))
f = int(input("Ingrese numero"))
g = int(input("Ingrese numero"))
h = int(input("Ingrese numero"))
i = int(input("Ingrese numero"))

A = [[a,b,c],[d,e,f],[g,h,i]]

suma = 0
for i in A:
    suma = a+e+h

if suma%2==1:
    mensaje= "Resultado impar"
if suma%2==0:
    mensaje="Resultado par"
print(A)
print (mensaje)
