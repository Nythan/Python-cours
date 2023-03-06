def insert(list : int)->list:
    x = int(input("Entrez un entier : "))
    list.append(x)
    list.sort()
    return list

l = [1,2,3,4,5,6,7,8,9,10]

print(insert(l))