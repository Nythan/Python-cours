def top_likes(like : dict) -> tuple:
    listLike = []
    for i in like.items():
        listLike.append(i)

    if len(listLike) != 0 :
        result = listLike[0]
        for i in range(len(listLike)):
            if result[1] < listLike[i][1]:
                result = listLike[i]
            if result[1] == listLike[i][1]:
                tempres = result[0]
                temptest = listLike[i][0]
                if tempres[0] > temptest[0]:
                    result = listLike[i]
    else:
        result = ('', 0)
    return result


like = {'Bob': 102, 'Ada': 201, 'Alice': 103, 'Tim': 50}
print(top_likes(like))

dic = {'Bob': 102, 'Ada': 201, 'Alice': 103, 'Tim': 50}
assert top_likes(dic) == ('Ada', 201)

dic = {'Bob': 102, 'Marc': 201, 'Alice': 103, 'Ada': 201}
assert top_likes(dic) == ('Ada',201)

dic = {'Bob':102}
assert top_likes(dic) == ('Bob',102)

dic = {}
assert top_likes(dic) == ('',0)