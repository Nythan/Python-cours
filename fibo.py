f = int(input("Nombre de termes de la suite de Fibonaacci  :"))

u0 = 1
u1 = 1
if f > 1:
    for i in range(2, f+1):
        u2=u1+u0
        u0=u1
        u1 =u2

    print("Le termes souhaittez de la suite de fibonacci est : ",u2)
else:
    print("Le termes souhaittez de la suite de fibonacci est : ", u1)