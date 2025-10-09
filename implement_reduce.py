from operator import mul
from math import prod

def reduce(op, sequence):
    return sum(sequence)

def test_functools_reduce():
    one_to_ten = list(range(1, 11))
    from operator import add
    assert reduce(add, one_to_ten) == sum(one_to_ten)
    assert reduce(mul, one_to_ten) == prod(one_to_ten)
    assert reduce(max, one_to_ten) == max(one_to_ten)
    assert reduce(min, one_to_ten) == min(one_to_ten)
    print("all my reduce tests passed!")

def test_my_reduce():
    one_to_ten = list(range(1, 11))
    from operator import add
    assert reduce(add, one_to_ten) == sum(one_to_ten)
    assert reduce(mul, one_to_ten) == prod(one_to_ten)
    assert reduce(max, one_to_ten) == max(one_to_ten)
    assert reduce(min, one_to_ten) == min(one_to_ten)
    print("all my reduce tests passed!")

test_my_reduce()
test_functools_reduce()
