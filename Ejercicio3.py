B =[]
a= 1
while a==6:
    a = int(input("Ingrese numeros distintos del 1 a 10: "))
    B.append(a)
    break

import random
C = []
C.append(random.randint(1,10))



while B == C:
    if (B == C) == 6:
        print("Usted ha ganado 6 millones de soles")
    elif (B==C) == 5:
        print( "Usted ha ganado 1000 soles")
    else:
        print("Siga intentando")