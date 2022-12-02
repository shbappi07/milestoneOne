def add(x,y):
    z=x+y
    return z

def sub(x,y):
    z=x-y
    return z

def multiply(x,y):
    z=x*y
    return z

def multiAgr(*args):
    total = 0
    for item in args:
        total = item+total
    return total
# print(multiAgr(1,2,3,4,5,6,7,8,9,10))

def multiReturn(x,y):
    add = x+y
    sub =x-y
    mult = x*y
    return add,sub,mult

# print(multiReturn(1,2))
toup = multiReturn(1,2)
print(toup)
# tup = toup[0]
tupList = list(toup)
tupList[0]=9
print(tupList)

cngToTpl = tuple(tupList)
print(cngToTpl)
