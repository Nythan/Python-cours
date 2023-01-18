from random import randint
x = int(input("Borne inférieur : "))
y = int(input("Borne supperieur: "))
n = randint(x,y)
h = False
grand = "Trop Grand"
petit = "Trop Petit"
bien = "Gagné"
z=0
while h!= True:
    print("j'ai choisi", n)
    test = input("alors c'est bien ?")
    if test == grand:
        y=n
        n = randint(x,y)
    elif test == petit:
        x=n
        n = randint(x,y)
    else:
        h = True
    z = z+1
print("J'ai fini par trouvé")
print("J'ai essayer :", z, "fois avant de trouvé")