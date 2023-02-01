
def saisirEntier() -> int:
    premier = int(input("entrez un entier : "))
    return premier

def saisieEntierSuivant(premier : int) -> int:
    second = int(input("entrez un second entier strictement supérieur au premier : "))
    if second <= premier:
        second = int(input("vous avez entrez un entier plus petit ou égale au premier"
                           "entrez un second entier strictement supérieur au premier : "))
    return second


def somme(premier,second)-> int:
    test=[]
    total = 0
    for i in range(premier,second+1):
        test.append(int(i))
    #print(test)
    for i in range(len(test)):
        total = total + int(test[i])
    print(total)

x = saisirEntier()
somme(x,saisieEntierSuivant(x))