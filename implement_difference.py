# set1 - set2 → O(len(set1)))

# difference
def difference(A, B):
    return A - B

A = set(range(10))
B = set(range(5))
assert A - B == difference(A, B)

A = set()
B = set(range(5))
assert A - B == difference(A, B)

A = set(range(5, 10))
B = set(range(10))
assert A - B == difference(A, B)
