def divPar2(x : int) -> list:
    i = 0
    while x %2 == 0 :
        x=x//2
        i = i+1
    return [x,i]

def divParImpair(List:list)->list:
    x = List[0]
    i = 3
    while x != 1:
        if x%i == 0:
            x=x//i
            List.append(i)
        else:
            i = i+2
    return List

def affichage(x:int,List:list) -> str:
    affiche = ""
    y = List[1]
    z = []

    for i in range(2,len(List)):
        z.append(List[i])
    for i in range(y):
        affiche = affiche+ "2*"
    for i in range(len(z)):
        if i == len(z)-1:
            affiche = affiche + str(z[i])
        else:
            affiche = affiche + str(z[i]) + "*"

    if len(affiche) > 1 :
        print(affiche)
    else:
        print("C'est un nombre premier !")

print(divPar2(48))
print(divParImpair([45,3]))
affichage(360,[45,3,3,3,5])
assert divPar2(46) == [23, 1]
assert divPar2(24) == [3, 3]
assert divPar2(7) == [7, 0]
assert divPar2(125) == [125,0]
assert divPar2(360) == [45,3]

assert divParImpair([23,1]) == [23,1,23]
assert divParImpair([3,3]) == [3,3,3]
assert divParImpair([7,0]) == [7,0,7]
assert divParImpair([125,0]) == [125,0,5,5,5]
assert divParImpair([45,3]) == [45,3,3,3,5]

# 2*23
affichage(46,[23,1,23])
# 2*2*2*3
affichage(24,[3,3,3])
# C'est un nombre premier !
affichage(7,[7,0,7])
# 5*5*5
affichage(125,[125,0,5,5,5])
# 2*2*2*3*3*5
affichage(360,[45,3,3,3,5])