def reduce():
    pass

def add(x, y):
    return x + y

def oneToTen():
    return list(range(1, 10))

assert(reduce(add, oneToTen) == 1)
