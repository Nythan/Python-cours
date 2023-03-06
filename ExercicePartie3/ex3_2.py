def pair(list:int)->list:
    l2 = []
    l3 = []
    for i in range(len(list)):
        if list[i] %2:
            l2.append(list[i])
        else:
            l3.append(list[i])

    return l2 , l3

l = [1,2,3,4,5,6,7,8,9,10]

print(pair(l))