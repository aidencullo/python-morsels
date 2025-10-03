from functools import reduce


def concat_with_reduce(lst):
    def concat(x, y):
        return x + y

    return reduce(concat, lst, "")


def test_concat_with_reduce():
    s = "hello world"
    lst = list(s)
    assert concat_with_reduce(lst) == s
    print("concat tests passed!")


def flatten_with_reduce(lst):
    def concat(x, y):
        return x + y

    return reduce(concat, lst, [])
    


def test_flatten_with_reduce():
    nested = [[0] * 2] * 2
    expected = [0] * 4
    assert flatten_with_reduce(nested) == expected
    print("flatten tests passed!")

def product_with_reduce():
    pass


def max_with_reduce():
    pass


def min_with_reduce():
    pass


def main():
    test_concat_with_reduce()
    test_flatten_with_reduce()


main()
