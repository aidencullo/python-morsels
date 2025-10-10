# set1 ^ set2 → O(len(set1) + len(set2)))

# symmetric difference
def symmetric_difference(A, B):
    return A ^ B

A = set(range(10))
B = set(range(5))
assert A ^ B == symmetric_difference(A, B)

A = set()
B = set(range(5))
assert A ^ B == symmetric_difference(A, B)

A = set(range(5, 10))
B = set(range(10))
assert A ^ B == symmetric_difference(A, B)
