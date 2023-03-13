def redondance(List : int) -> list:
    List.sort()
    test = []
    #for v in range(len(List)):
    for i in range(len(List)):

        if List[i-1] != List[i]:
            test.append(List[i-1])
    test.sort()
    return test

l = [1,2,3,4,5,6,7,8,2,2,2,9,10]
print(redondance(l))