def decomposer(ch : str) -> list[tuple[str,int]]:
    ll = list(ch)
    lres = []
    i = 0

    while i < len(ll):
        car = ll[i]
        j = i+1
        cpt = 1
        while j < len(ll):
            if ll[j] == car:
                cpt = cpt+1
                del ll[j]
            else:
                j = j+1
        i = i +1
        lres.append((car,cpt))
    return lres

print(decomposer("bonjour"))
print(decomposer("aaa"))

assert decomposer("bonjour") == [('b',1),('o',2),('n',1),('j',1),('u',1),('r',1)]
assert decomposer("abcd") == [('a',1),('b',1),('c',1),('d',1)]
assert decomposer("aa bb c") == [('a',2),(' ',2),('b',2),('c',1)]
assert decomposer("aaa") == [('a',3)]
assert decomposer("") == []