##cours sur les assertion
from typing import Dict


def div(a: int, b: int) -> int:
    assert b!=0, "le diviseur ne doit pas être nul"
    return a/b
def somme(a : int ,b : int) -> int:
    """Fonction renvoyant la somme de ses 2 arguments."""
    return a+b #erreur

assert somme(2,0)==2
assert somme(5,3)==8,"pb avec la somme de 5 et 3"
assert somme(0,2)==2,"pb avec une somme dont le premier élément est nul"

print(div(5,2))
#print(div(6,0))

def resteDiv(a: int, b:int) -> int:
    quaotient=a//b
    reste = a - quaotient * b
    assert reste < b, "Le reste doit être plus petit que le diviseur"
    assert int(reste) == reste
    assert int(quaotient) == quaotient
    return reste

print(resteDiv(50, 8))

#types de données
#introduction aux types de colections de données
#les listes sont en réalité des tableaux dynamiques
#plutôt pour des éléments de même type
print("----- Les listes -----")
l1 = [1,2,3,4]
l2=[]
l3 = [(2*x) for x in range(5)]
print(l1)
print(l1[-1])#print la dernière valeur
print(l2)
print(l3)

print("------")
for v in l3:
    print(v)
print("------")

for i in range(len(l1)):
    print("l1[",i,"]=",l1[i], sep='')
print(l1[1])

# les tuples : ressemble au struct de C
# plutôt des éléments hétérogénes

print("---- Les tuples ----")
t1 = (1,'a', True)
t2 = (2,) # un singleton
t3 = ()

print(t1)
print(t2)
print(t3)

print("------")
for v in t1:
    print(v)

print("------")
print(t1[1])

#les ensemble modifiables
print("----- Les ensembles -----")
s1 = {1,2,3}

print(s1)
for v in s1:
    print(v)

#les tables associatives ou dictionnaires
#les clefs doivent être d'un type disposant d'une fonction de hashage

print("----- Les dictionnaires -----")
d1 = {"A":3,"B":4,"C":2}
print(d1)
print(d1["C"])

def divDic(a: int, b: int) -> Dict:
    return {"quotien":a//b,"reste":a%b}

print(divDic(22,3))