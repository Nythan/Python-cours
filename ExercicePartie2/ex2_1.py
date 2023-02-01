x = int(input("saississez un chiffre : "))
def mult(x : int) -> int:
    for i in range(1,11):
        y = i * x
        if y < 10:
            print(y, end='   ')
        else:
            print(y, end='  ')
    print()

mult(x)