def max(List : int) -> int:
    max = 0
    for i in range(len(List)):
        if max < List[i]:
            max = List[i]
    return max

#def maxOccurence(List : int) ->int:


l = [1,2,3,4,5,6,7,8,9,10]

print(max(l))