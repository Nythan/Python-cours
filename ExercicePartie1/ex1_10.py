test = 0
liste = []

while test != 4:
    x="Saisir un chiffre (",test+1,") : "

    saisie = input(x)

    if len(saisie) == 1:
        if 48 <= ord(saisie) <= 57:
            test = test+1
            liste.append(int(saisie))
        else:
            print("Ce n'est pas un chiffre !!!!")
    else:
        print("Ce n'est pas un chiffre !!!!")
print(liste)