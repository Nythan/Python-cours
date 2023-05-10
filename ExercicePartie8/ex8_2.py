def saisirEntier() -> int:
    ok = False
    while not ok:
        try:
            print("Saisir un entier : ")
            val = int(input())
            ok = True
        except ValueError:
            print("Ce n'est pas un entier bordel !!!!!!!!!!!!!!!!!!!!!!!!!!!")
    return ("nombre saisi : ", val)


distance = saisirEntier()
vitesse = saisirEntier()

try:
    test = distance / vitesse
except ZeroDivisionError:
    print("Il y a une division par zero ")