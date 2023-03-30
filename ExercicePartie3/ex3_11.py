def rechercheDicchotomie(elem, tab : list, deb=0, *reste) -> bool:
    sorted(tab)
    result = False
    if len(reste) != 0:
        fin = reste[0]
    else:
        fin = len(tab)
    print(fin)
    milieu = (deb + fin) // 2
    if elem == tab[milieu]:
        result =  True
    if deb == fin :
        if elem == tab[deb]:
            result = True
    if deb > fin :
        result = False
    if deb < fin:
        for i in range(len(tab)):
            if elem == tab[i]:
                 if rechercheDicchotomie(elem, tab, deb, milieu):
                    result = True
                 if rechercheDicchotomie(elem, tab, milieu, fin):
                    result = True

    return result

e = 1
t = [1,2,3,5,8,6,47,5416,654,35,935,659,2]
print(rechercheDicchotomie(e,t))


