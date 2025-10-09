from operator import mul
from math import prod
import functools

def head(seq):
    return seq[0] if seq else None

def reduce(op, sequence):
    if not sequence:
        raise TypeError("reduce() of empty iterable with no initial value")
    initial = sequence[0]
    return sum(sequence)

def test_head():
    assert head([1]) == 1
    assert head([1,10]) == 1
    assert head(list(range(1, 10))) == 1
    assert head([]) is None
    print("all my head tests passed!")

def test_functools_reduce():
    one_to_ten = list(range(1, 11))
    from operator import add
    assert functools.reduce(add, one_to_ten) == sum(one_to_ten)
    assert functools.reduce(mul, one_to_ten) == prod(one_to_ten)
    assert functools.reduce(max, one_to_ten) == max(one_to_ten)
    assert functools.reduce(min, one_to_ten) == min(one_to_ten)
    print("all my functools.reduce tests passed!")

def test_my_reduce():
    one_to_ten = list(range(1, 11))
    from operator import add
    assert reduce(add, one_to_ten) == sum(one_to_ten)
    assert reduce(mul, one_to_ten) == prod(one_to_ten)
    assert reduce(max, one_to_ten) == max(one_to_ten)
    assert reduce(min, one_to_ten) == min(one_to_ten)
    print("all my reduce tests passed!")

# test_my_reduce()
test_functools_reduce()
test_head()
