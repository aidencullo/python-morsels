


# intersection
def intersect(A, B):
    return A & B

A = set(range(10))
B = set(range(5))
assert A & B == intersect(A, B)

A = set()
B = set(range(5))
assert A & B == intersect(A, B)

A = set(range(5, 10))
B = set(range(10))
assert A & B == intersect(A, B)
