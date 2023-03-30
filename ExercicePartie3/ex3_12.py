def construireTabCoef(tab:list, n):
    for i in range(1,n-1):
        tab.append([1] + [tab[i][j] + tab[i][j+1] for j in range(len(tab[i])-1)] + [1])
    return tab

def affichage(tab:list):
    for i in range(len(tab)):
        for j in range(len(tab[i])):
            print(tab[i][j], end=' ')
        print()

t = [[1],[1,1]]
affichage(construireTabCoef(t,11))