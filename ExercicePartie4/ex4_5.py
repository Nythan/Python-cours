def decomposer(ch: str) -> list:
    t = []
    i = 0
    chl = list(ch)
    while i < len(chl):
        car = chl[i]
        y = 1
        j = i+1
        while j < len(chl):
            if car == chl[j]:
                y = y + 1
                del chl[j]
            else:
                j=j+1
        t.append((chl[i], y))
        i = i+1
    return t

print(decomposer("bonjour"))
print(decomposer("aaa"))

assert decomposer("bonjour") == [('b',1),('o',2),('n',1),('j',1),('u',1),('r',1)]
assert decomposer("abcd") == [('a',1),('b',1),('c',1),('d',1)]
assert decomposer("aa bb c") == [('a',2),(' ',2),('b',2),('c',1)]
assert decomposer("aaa") == [('a',3)]
assert decomposer("") == []