def anagrammes(mot1, mot2):
    if len(mot1) != len(mot2):
        print("les mots ont des longeu différente ils ne peuvent donc pas être des anagrammes")
        exit()
    arranged1 = "".join(sorted(mot1))
    arranged2 = "".join(sorted(mot2))
    if arranged2 == arranged1:
        print("ce sont des anagrammes")
    else:
        print("ce ne sont pas des anagrammes")
test = input("entrez un mot : ")
b = input("donnez une anagramme du premier mot que vous avez écrit : ")

anagrammes(test,b)