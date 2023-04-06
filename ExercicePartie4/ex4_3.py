def genererTuple(l : list[int])->tuple:
    tp = tuple(l)
    return tp



assert genererTuple([]) == ()
assert genererTuple([5]) == (5,)
assert genererTuple([5, 9, 2, 4]) == (5, 9, 2, 4)