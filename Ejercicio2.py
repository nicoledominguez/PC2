# Una historia de usuario, es un medio en el que el cliente puede pedir algo que requiera para 
# una determinada pagina, estás siempre estan calificadas po numeros que representan la dificultad
# del requisito propuesto, siendo 1 la más baja.

#-----------Historia de usuario-------------------
#¿Como? Como cliente frecuente de la empresa

#¿Quiere? Deseo que el sistema me pida una contraseña de 6 digitos para ingresar al documento

#¿Para? Para asi estar mas seguro de mi privacidad

# Nivel de dificultad : 1

Contraseña = int(input("Ingrese contraseña"))

while True:
    if Contraseña >=1 and Contraseña <=6:
        print("Acceso Concedido")
    else: 
        print("Acceso Denegado. Intente nuevamente")
        break
        