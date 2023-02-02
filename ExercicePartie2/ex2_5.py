x = "INFO.MA.IQUE"  # x=sorted("INFO.MA.IQUE")
y = "INFORMATIQUE"  # y=sorted("INFORMATIQUE")
# print(y)
# print(x)
def correspondance(x : str,y:str) -> bool:
    e = []
    if len(x) == len(y):
        for i in range(len(x)):
            if x[i] != y[i]:
                e.append(y[i])
        for i in range(len(e)):
            if e[i] == ".":
                h=True

    else:
        print("impossible")
        h = False
    if h:
        print(x,",",y,",", "les mots sont correspondant")
    return h

#correspondance(input("mot"),input("mot"))

assert correspondance("INFORMATIQUE", "INFO.MA.IQUE") == True
assert correspondance("AUTOMATIQUE", "INFO.MA.IQUE") == False
assert correspondance("INFO", "INFO.MA.IQUE") == False
assert correspondance("INFORMATIQUES", "INFO.MA.IQUE") == False