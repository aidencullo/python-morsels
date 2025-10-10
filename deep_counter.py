from collections import Counter

# Initial Counters
c = Counter(a=4, b=2, c=0, d=-2)
d = Counter(a=1, b=2, c=3, d=4)

print("Original Counters:")
print("c:", c)
print("d:", d)

# subtract
c.subtract(d)
print("\nc.subtract(d):", c)  # a:3, b:0, c:-3, d:-6

# total of all counts
print("\nc.total():", c.total())  # sum of all counts

# clear
c.clear()
print("\nc.clear():", c)  # Counter()

# recreate c for further examples
c = Counter(a=3, b=1, c=0, d=-2)

# list unique elements
print("\nlist(c):", list(c))  # ['a', 'b', 'c', 'd']

# set conversion
print("set(c):", set(c))  # {'a', 'b', 'c', 'd'}

# dict conversion
print("dict(c):", dict(c))  # {'a':3, 'b':1, 'c':0, 'd':-2}

# items
print("c.items():", list(c.items()))  # [('a',3), ('b',1), ('c',0), ('d',-2)]

# convert from list of pairs
list_of_pairs = [('a', 5), ('b', 2)]
print("Counter(list_of_pairs):", Counter(list_of_pairs))

# most_common / least common
print("Most common 2:", c.most_common(2))
print("Least common 2:", c.most_common()[:-2-1:-1])

# remove zero and negative counts
print("Unary +c:", +c)  # only positive counts

# Mathematical operations
c1 = Counter(a=3, b=1)
c2 = Counter(a=1, b=2)

print("\nc1 + c2:", c1 + c2)  # add counts
print("c1 - c2:", c1 - c2)    # subtract positive counts only
print("c1 & c2:", c1 & c2)    # intersection (min)
print("c1 | c2:", c1 | c2)    # union (max)
print("c1 == c2:", c1 == c2)
print("c1 <= c2:", c1 <= c2)

# unary + and -
c3 = Counter(a=2, b=-4)
print("\n+c3:", +c3)  # remove non-positive
print("-c3:", -c3)     # remove non-positive, invert negatives to positive
