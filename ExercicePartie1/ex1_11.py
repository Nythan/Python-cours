mot1 = input("Entrez un mot")
mot2 = input("Entrez un mot")
count = 0
if len(mot1) == len(mot2):
    for i in range(len(mot1)):
        if mot1[i]!=mot2[i]:
            count=count+1
else:
    count = -1

print(count)