from random import randint
x = int(input("Borne inférieur : "))
y = int(input("Borne supperieur: "))
n = randint(x,y)
test = int(input("essaye de deviner : "))
z=1
while test != n:
    if test > n:
        print("Plus petit")
        test = int(input("essaye encore : "))
        z=z+1
    else:
        print("Plus Grand")
        test = int(input("essaye encore : "))
        z=z+1
print("Vous avez gagnez")
print("Vous avez mis :", z, "tentative")