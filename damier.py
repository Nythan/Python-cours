x = int(input("Quel taille de damier voulait vous ?"))

for i in range(0,x):
    for j in range(0,x):
        if i%2==0:
            if j%2==0:
                print('□',end=' ')
            else:
                print('■',end=' ')
        else:
            if j%2==0:
                print('■',end=' ')
            else:
                print('□',end=' ')
    print()