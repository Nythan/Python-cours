def fusion(list:int, list2:int)->list:
    for i in range(len(list2)):
        list.append(list2[i])
    list.sort()
    return list

l = [1,2,8]
l2 = [6,7,3]
l3 = []

print(fusion(l,l2))

print(fusion(l2,l3))