from operator import mul, add
from math import prod
import functools

def head(seq):
    return seq[0] if seq else None

def reduce(op, sequence, default=None):
    if not sequence:
        raise TypeError("reduce() of empty iterable with no initial value")
    acc = default
    for x in sequence:
        if acc is None:
            acc = x
        else:
            acc = op(acc, x)
    return acc

def test_head():
    assert head([1]) == 1
    assert head([1,10]) == 1
    assert head(list(range(1, 10))) == 1
    assert head([]) is None
    print("all my head tests passed!")

def test_my_reduce():
    one_to_ten = list(range(1, 11))
    assert reduce(add, one_to_ten) == functools.reduce(add, one_to_ten)
    assert reduce(mul, one_to_ten) == functools.reduce(mul, one_to_ten)
    assert reduce(max, one_to_ten) == functools.reduce(max, one_to_ten)
    assert reduce(min, one_to_ten) == functools.reduce(min, one_to_ten)
    print("all my reduce tests passed!")

test_my_reduce()
test_head()
