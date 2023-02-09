def calcule_ch(k = "etc",*reste) -> str:
    z = ""+k
    if len(reste) == 0:
        z = z+k
    else:
        for i in range(len(reste)):
            z = z+reste[i]
    return z
print(calcule_ch("toto"))
assert calcule_ch() == "etcetc"
assert calcule_ch("toto") == "totototo"
assert calcule_ch("toto","tutu") == "tototutu"
assert calcule_ch("toto","tutu","titi") == "tototututiti"