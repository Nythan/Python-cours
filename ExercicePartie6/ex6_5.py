def ajouter(dico: dict, clef) -> dict:
    if clef in dico.keys():
        dico[clef] = dico[clef] +1
    else:
        dico.update({clef:1})
    return dico


def decomposer(ch:str)-> dict:
    lres = {}
    for car in ch:
        ajouter(lres,car)
    return lres

print(decomposer("bonjour"))
print(decomposer("aaa"))

assert decomposer("bonjour")== {'b':1,'o':2,'n':1,'j':1,'u':1,'r':1}
assert decomposer("abcd")=={'a':1,'b':1,'c':1,'d':1}
assert decomposer("aa bb c")=={'a':2,' ':2,'b':2,'c':1}
assert decomposer("aaa") == {'a':3}
assert decomposer("") == {}

