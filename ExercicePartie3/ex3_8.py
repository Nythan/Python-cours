def divPar2(x : int) -> list:
    i = 0
    while x %2 == 0 :
        x=x//2
        i = i+1
    return [x,i]



print(divPar2(48))
assert divPar2(46) == [23, 1]
assert divPar2(24) == [3, 3]
assert divPar2(7) == [7, 0]
assert divPar2(125) == [125,0]
assert divPar2(360) == [45,3]