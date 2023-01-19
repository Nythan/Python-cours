distribMax = 200
billet = 20
piece = 100

while distribMax != 0:
    print("Montant restant : ", distribMax)
    prix = int(input("Prix de l'article : "))
    somme = int(input("Montant fourni : "))
    rendre = somme-prix
    if rendre <= distribMax:
        print("Je vous rend la monaie :", rendre)
        distribMax = distribMax - rendre
        if billet != 0:
            if rendre%5 == 0:
                x=rendre/5
                if x <=billet:
                    print("Je vous rend :", x ,"billets de 5 € et 0 pièce de 1 €")
                    billet=billet-x
                else:
                    z=x-billet
                    print("Je vous rend : ",billet," billets de 5 € et :",z*5,  "pièces de 1 €")
                    billet = billet - z
            else:
                l=rendre//5
                rest = rendre - rendre//5*5
                if  l>billet:
                    h=l-billet
                    print("Je vous rend : ",billet," billets de 5 € et :",h*5+rest,"pièce de 1 €")
                    billet=billet-h
                else:
                    print("Je vous rend : ",l," billets de 5 € et :",rest,"pièce de 1 €")
                    billet = billet-l
        else:
            print("Je vous rend : ", billet, " billets de 5 € et :", rendre, "pièce de 1 €")
    else:
        print("Je n'ai pas assez de monaie !")


