l = [0,0,0,0]
nbCas = 0
for i in range(0,10000):
    l[0] = int(i/1000)
    l[1] = int(i%1000/100)
    l[2] = int(i%100/10)
    l[3] = int(i%10)
    if l[0]*10+l[1]+l[2]*10+l[3] == l[1]*10+l[2]:
        nbCas = nbCas+1
        print(l)
print(nbCas)
