def anagrammes(mot1 : str, mot2 : str):
    if len(mot1) != len(mot2):
        print("les mots ont des longeu différente ils ne peuvent donc pas être des anagrammes")
        exit()
    arranged1 = "".join(sorted(mot1))
    arranged2 = "".join(sorted(mot2))
    if arranged2 == arranged1:
        print("ce sont des anagrammes")
        return True
    else:
        print("ce ne sont pas des anagrammes")
        return False


test = input("entrez un mot : ")
b = input("donnez une anagramme du premier mot que vous avez écrit : ")

anagrammes(test,b)

assert anagrammes('chien', 'niche'), "ne fonctionne pas"
assert anagrammes('énergie noire', 'reine ignorée'), "ne fonctionne pas"
assert not anagrammes('louve', 'poule'), "raté"
