from functools import reduce

def concat_with_reduce(lst):
    concat = lambda x, y: x + y
    return reduce(concat, lst, "")

def test_concat_with_reduce():
    s = "hello world"
    lst = list(s)
    assert concat_with_reduce(lst) == s
    print("concat tests passed!")



def flatten_with_reduce():
    pass

def product_with_reduce():
    pass

def max_with_reduce():
    pass

def min_with_reduce():
    pass

def main():
    test_concat_with_reduce()

main()
