def jouable(t: list[tuple], x: int) -> list:
    res = []
    for i in range(len(t)):
        if t[i][-2] <= x <=t[i][-1]:
            res.append(t[i][0])
    return res






tab = []
tab.append(('dark castle',3,6))
tab.append(('lucky numbers',2,4))
tab.append(('lueurs',2,4))
assert jouable(tab,2)==['lucky numbers','lueurs']
assert jouable(tab,5)==['dark castle']
assert jouable(tab,1)==[]
assert jouable(tab,4)==['dark castle','lucky numbers','lueurs']