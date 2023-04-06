def indiceOccurenceElem(x:int,t : tuple) ->int:
    z = -1
    for i in range(len(t)):
        if t[i] == x:
            z = i
    return z




tup1 = (1,5,4,10)
assert indiceOccurenceElem(5,tup1) == 1
assert indiceOccurenceElem(12,tup1) == -1
assert indiceOccurenceElem(10,tup1) == 3