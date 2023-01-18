# Python-cours
Partie 1: Remise en route sur les bases
Exercice 1.1 : calcul d’une valeur approchée de PI
Sachant que la somme : 1 – 1/3 + 1/5 – 1/7 + 1/9 – 1/11 + 1/13 – 1/15 + … tend vers π/4, écrire un
programme permettant de calculer une valeur approchée de π. On pourra écrire deux versions :
selon que l’on demande à l’utilisateur le nombre de termes souhaités, ou la valeur du dénominateur
du dernier terme pris en compte dans le calcul.
Exercice 1.2 : calcul des termes de la suite de Fibonacci
Écrire un algorithme, puis un programme, qui permet d’afficher le n ième terme (n étant saisi au
clavier) de la suite de fibonnaci : 1 1 2 3 5 8 13 21…
Rappel : la définition mathématique de la suite de Fibonnaci est la suivante :
✗ U0 = 1
✗ U1 = 1
✗ Un = Un-1 + Un-2 pour n>1
Exercice 1.3 : calcul des tables de multiplication
Écrire un programme, permettant d’afficher à l’écran la table de multiplication des entiers de 1 à 10.
On n’utilisera ici aucune structure de données. L’affichage doit être le suivant :
1 2 3 4 5 6 7 8 9 10
2 4 6 8 10 12 14 16 18 20
3 6 9 12 15 18 21 24 27 30
4 8 12 16 20 24 28 32 36 40
5 10 15 20 25 30 35 40 45 50
6 12 18 24 30 36 42 48 54 60
7 14 21 28 35 42 49 56 63 70
8 16 24 32 40 48 56 64 72 80
9 18 27 36 45 54 63 72 81 90
10 20 30 40 50 60 70 80 90 100
Exercice 1.4 : le damier
Écrire un programme qui affiche à l’écran un damier. La taille du coté du damier sera demandée à
l’utilisateur. Pour les cases noires, on affichera un espace. Pour les cases blanches, on affichera le
caractère correspondant à un carré blanc (taper au clavier dans un terminal : CTRL+SHIFT+u2410
pour obtenir le caractère) .
G. Simon – Université Le Havre Normandie 4
Exercice 1.5 : le distributeur automatique
Un distributeur automatique dispose, pour rendre la monnaie, de 20 billets de 5 euros et de 100
pièces de 1 euro. Ecrire un programme, qui :
• demande à l'utilisateur le prix de l'article à payer (en euros entiers) et la somme qu'il va
introduire dans le distributeur ;
• calcule la monnaie à rendre à l'utilisateur en billets de 5 euros et pièces de 1 euro ;
• déduit de ses propres ressources le nombre de billets et pièces rendues ;
• propose un nouvel achat jusqu'à ce qu'il n'y ait plus de monnaie à rendre.
Indication : la caisse contenant la monnaie à rendre et celle recevant l’argent des clients sont
distinctes. Il arrivera donc un moment où il ne sera plus possible d’effectuer un achat.
Exercice 1.6 : jeu du nombre à deviner
Ecrire un programme permettant de jouer au jeu du nombre mystérieux. La règle en est la suivante :
après que la machine ait choisi un nombre aléatoire compris entre 1 et 1000, vous devez, en
proposant des nombres, retrouver le nombre de la machine. Pour cela à chaque fois que vous
proposez un nombre, la machine vous répond si votre nombre est plus grand ou plus petit que le
nombre à trouver. Quand vous aurez trouvé le nombre mystérieux, la machine devra préciser en
combien de coups vous avez réussi.
G. Simon – Université Le Havre Normandie 5
Exercice 1.7 : jeu du nombre à deviner inversé
Inverser le principe de l’exercice précédent en faisant trouver par l’ordinateur un nombre choisi par
l’utilisateur. Pour cela, le programme va tirer aléatoirement un nombre dans un intervalle qui sera
réduit à chaque tentative en fonction des tirages précédents. Par exemple, supposons que le nombre
à trouver est 35. Le programme va commencer par tirer aléatoirement un nombre entre 1 et 1000.
Supposons qu’il choisisse 50. L’utilisateur va indiquer que le nombre proposé est trop grand. Le
prochain tirage du programme se fera donc entre 1 et 50...
A chaque tentative de la machine, on affichera le nombre qu’elle propose ainsi que le nombre de
tentatives déjà effectuées.
Exercice 1.8 : propriétés des nombres
On recherche les nombres à quatre chiffres ‘ abcd’ tels que, si l’on décompose ces nombres, ils
vérifient la propriété suivante : ab + cd = bc.
Par exemple, 3956 vérifie cette propriété. En effet, 39 + 56 = 95.
Ecrire un programme qui affiche tous les nombres vérifiant cette propriété combien il y en a.
Remarque : pour ce type de problème,on peut effectuer une recherche exhaustive sur l’intervalle des
nombres à quatre chiffres.
Exercice 1.9 : nombres à construire
Soit l'équation aa * bb = ccdd avec chaque lettre représentant un chiffre
Ecrire un programme qui doit trouver les nombres correspondant à ccdd.
Pour chacun, le programme doit fournir la multiplication de la forme aa * bb dont il est issu.
• dans une première version, les 4 chiffres a,b,c et d sont quelconques
• dans une seconde version, les 4 chiffres a, b, c et d doivent être tous différents
Exercice 1.10 : contrôle de saisie
Il s’agit ici d’écrire un programme permettant de faire saisir à l’utilisateur consécutivement 4
chiffres. Tout ce qui n’est pas un chiffre doit être refusé. Dès qu’un chiffre est validé, il doit être
affiché et le programme doit passer à la saisie du chiffre suivant. Une fois les 4 chiffres saisis, le
programme doit afficher le nombre correspondant aux 4 chiffres saisis ainsi que son double.
Rappels:
- la fonction chr renvoie le caractère dont le code ASCII est passé en paramètre.
- la fonction ord renvoie le code ASCII du caractère passé en paramètre
NB : il faut aussi prévoir et refuser le cas ou l’utilisateur saisit plusieurs caractères au lieu d’un seul.
Exercice 1.11 : code Hamming
Il s’agit d’écrire un programme permettant de calculer la distance de Hamming entre deux mots.
Cette notion est utilisée dans de nombreux domaines comme les télécommunications, le traitement
du signal, . . . Elle est définie, pour deux mots de même longueur, comme le nombre de positions où
les deux mots ont un caractère différent. Le programme doit saisir 2 mots et calcule la distance de
Hamming entre les deux mots lorsqu’ils ont la même longueur. Si les mots n’ont pas la même
longueur, le programme doit afficher -1.
Par exemple, pour les mots « aaba » et « aaha », le programme doit afficher 1. Pour les mots
« poire » et « pomme », le programme doit afficher 2. Enfin pour les mots « stylo » et « bouteille »,
le programme doit afficher -1.
