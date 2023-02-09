def verif(x : str) -> bool:
    if 48 <= ord(x) <= 57:
        return True
    else:
        return False
def saisirEntier() -> int:
    premier = (input("entrez un entier : "))
    for i in range(len(premier)):
         while not verif(premier[i]):
            premier = (input("entrez un entier : "))

    return int(premier)

def saisieEntierSuivant(premier : int) -> int:
    second = saisirEntier()
    while premier+1 > second:
        print("Saisir un entier plus grand")
        second = saisirEntier()
    return second


def somme(premier : int,second : int)-> int:
    test=[]
    total = 0
    for i in range(premier,second+1):
        test.append(int(i))
    #print(test)
    for i in range(len(test)):
        total = total + int(test[i])
    return total

x = saisirEntier()
#print(x)
print(somme(x,saisieEntierSuivant(x)))