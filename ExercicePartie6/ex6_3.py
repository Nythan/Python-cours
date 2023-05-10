Dico = {"Bonjour" : "Hello", "Salut" : "hy" }

def ajouter(fra : str,en:str,dico:dict[str,str]):
    if not fra in dico.keys():
        dico[fra] = en
        res = True
    else:
        res = False
    return res

print("Saisir un mot en français", end=" ")
motfr = input()

while not motfr == "fin":
    moten = input("Saisir un mot en anglais :")
    res = ajouter(motfr,moten,Dico)
    if not res:
        print("Le mot français figure déjà dans le dictionnaire !")
    motfr = input("Saisir un mot en français : ")
print(Dico)

listOrdonnee=sorted(Dico.items())

dicoOrdonnee = dict(listOrdonnee)
print(dicoOrdonnee)

dicoEnFr = {}
for clef,valeur in Dico.items():
    dicoEnFr[valeur] = clef
print(dicoEnFr)
motEn = input("Saisir un mot en anglais à supprimer du dictionnaire inversé : ")
if motEn in dicoEnFr.keys():
    del dicoEnFr[motEn]
else:
    print("Ce mot n'est pas dans le dictionnaire inversé !!")


