def ligne_pleine(car : str,nb : int) -> str:
    e = []
    if nb >= 1:
        for i in range(nb):
            e.append(car)
            test = "".join(e)
        print(test)
        return test

def ligne_creuse(car : str, nb : int) -> str:
    e = []
    if nb >= 1:
        for i in range(nb):
            e.append(" ")
        e[0] = car
        e[-1] = car
        test = "".join(e)
        print(test)
        return test

def rectangle_plein(car:str, longeur:int, largeur:int) -> str:
    for i in range(longeur):
        ligne_pleine(car,largeur)

def rectangle_creux(car:str, longeur:int, largeur:int) -> str:
    ligne_pleine(car,largeur)
    for i in range(longeur-2):
        ligne_creuse(car, largeur)
    ligne_pleine(car,largeur)

def triangle_plein(car:str, hauteur:int) -> str:
    for i in range(hauteur):
        ligne_pleine(car,i)

def triangle_creux(car:str,hauteur:int) -> str:
    ligne_pleine(car,1)
    for i in range(2,hauteur):
        ligne_creuse(car,i)
    ligne_pleine(car,hauteur)

ligne_pleine("A",5)
print()
ligne_creuse("A", 10)
print()
rectangle_plein("C",5,5)
print()
rectangle_creux("B",5,5)
print()
triangle_plein("H",10)
print()
triangle_creux("Z",5)


print("------------")
# BBBBB
rectangle_plein('B', 1, 5)

print("------------")

# AAAAA
# AAAAA
# AAAAA
rectangle_plein('A', 3, 5)

print("------------")

# PPPPP
rectangle_creux('P', 1, 5)

print("------------")

# OOOOO,
# O   O
# O   O
# OOOOO
rectangle_creux('O', 4, 5)

print("------------")

# S
triangle_plein('S', 1)

print("------------")

# T
# TT
# TTT
# TTTT
# TTTTT
triangle_plein('T', 5)

print("------------")

# G
triangle_creux('G', 1)

print("------------")

# F
# FF
# F F
# F  F
# FFFFF
triangle_creux('F', 5)

assert ligne_pleine('M', 1) == "M"
assert ligne_pleine('#', 5) == "#####"
assert ligne_creuse('Y', 1) == "Y"
assert ligne_creuse('X', 5) == "X   X"