def calculerDizaines(z : int) -> tuple:
    c = z//10
    c1 = c *10
    c2 = c1+10
    return (c1,c2)
assert calculerDizaines(52)==(50,60)
assert calculerDizaines(10)==(10,20)
