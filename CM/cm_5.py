#CM 5
def test_add(a:int,b:int) -> bool:
    return (a+b)>10

#return boolean en faisant type(test_add(5,2))
#connaitre l'ensemble des données en faisant help(test_add(5,2))

def test_add2(a:int,b:int) -> bool:
    """fonction qui renvoie vrai si a+b > 10"""
    return (a+b)>10

type(test_add)
type(test_add2(2,5))
help(test_add)
help(test_add2)

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

#typage des données
from typing import *
#list
l1: List = [1,"a",2]
l2: List[Any] = [1,"a",2]
l3: List[int] = [1,"a",2] #pas d'erreur de typage
l4: List[int] = [1,2,3]
l5: List[int] = ["A","B","C"] # erreur de typage

#tuples

t1 : Tuple = (1,"a",2)
t2: Tuple[int,str,int] = (1,"A",2)
t3: Tuple[Any,Any,Any] = (1,"A",2)
t4: Tuple[int,str,int] = (1,"A","B")
t5: Tuple[int,str,int] = (1,"A")

# les dictionnaire

d1: Dict[str,int] = {"A":1,"b":2,"C":3}
d2: Dict = {"A":1,True:"Z"}
d3: Dict[str, int] = {"A":1,"B":"err","C":3} # pas d'erreur de typage
d4: Dict[str,int] = {"A":1,35:2,"C":3} # pas d'erreur de typage
d5: Dict[str,int] = {"A":1,35:"err","C":3} # pas d'erreur de typage
d6: Dict[str,int] = {1:"A",2:"B",3:"C"} # erreur de typage

# les ensembles

e1: Set[int] = {1,2,3}
e2: Set = {1,2,3}
e3: Set[int] =  {1,2,"c"} # pas d'erreur de typage
e4: Set[int] = {"A","B",[]} # erreur de typage
e5: Set[int] = {"A","B",True} # pas d'erreur de typage
e6: Set[Any] = {"A",1,[]}


