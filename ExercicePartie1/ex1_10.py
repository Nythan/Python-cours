test = 0
liste = []
codeZero = 48
codeNeuf = 57

while test != 4:
    x="Saisir un chiffre (",test+1,") : "

    saisie = input(x)

    if len(saisie) == 1:
        if codeZero <= ord(saisie) <= codeNeuf:
            test = test+1
            liste.append(int(saisie))
        else:
            print("Ce n'est pas un chiffre !!!!")
    else:
        print("Ce n'est pas un chiffre !!!!")
print(liste)