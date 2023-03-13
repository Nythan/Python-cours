def permEtDern(list1 : int,x : int) -> list:
    indice = [-1, -13]
    for i in range(len(list1)):
        if indice[0] == -1:
            if list1[i] == x:
                indice = [i, i]
        else:
            if list1[i] == x:
                indice[1] = i


    return indice

l = [1,2,3,4,5,6,7,8,2,9,10]

print(permEtDern(l,2))