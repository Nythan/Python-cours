x = int(input("Quel taille de damier voulait vous ?"))

for i in range(0,x):
    for j in range(0,x):
        if (i+j)%2==0:
            print('u',end='')
        else:
            print(' ',end='')
    print()