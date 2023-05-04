from random import randint

jeu = []

for couleur in ('carreau', 'coeur', 'pique', 'trèfle'):
    for valeur in range(1,11):
        carte = (valeur, couleur)
        jeu.append(carte)

print(len(jeu))
print(jeu)

print("Nom du joueur 1", end="")
nom1 = input()
print("Nom du joueur 2", end="")
nom2 = input()

jeu1 = []
jeu2 = []

i = 0
while (i<10):
    indChoisi = randint(0,len(jeu)-1)
    carteChoisie = jeu.pop(indChoisi)
    if i%2 == 0 :
        jeu1.append(carteChoisie)
    else:
        jeu2.append(carteChoisie)
    i=i+1

print('jeu joueur 1', format(jeu1))
print('jeu joueur 2', format(jeu2))
print(len(jeu2))
print("choisir un symblole :")

symbole = input()

maxj1 = 0

for i in range(len(jeu1)):
    if jeu1[i][1] == symbole:
        if jeu1[i][0] > maxj1:
            maxj1 = jeu1[i][0]

maxj2 = 0

for i in range(len(jeu2)):
    if jeu2[i][1] == symbole:
        if jeu2[i][0] > maxj2:
            maxj2 = jeu2[i][0]

if maxj1 == 0 and maxj2 ==0 :
    print("aucun des joueurs n'a cette couleur")
else:
    if maxj1 > maxj2:
        print("{} à la carte la plus grande {}", format())