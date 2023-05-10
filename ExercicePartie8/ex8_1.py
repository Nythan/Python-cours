ok = False
while not ok :
    try :
        print("Saisir un entier : ")
        val = int(input())
        ok = True
    except ValueError :
        print("Ce n'est pas un entier bordel !!!!!!!!!!!!!!!!!!!!!!!!!!!")
print("C'est bien tu as compris la consigne abruti ")
print("nombre saisi : ", val)