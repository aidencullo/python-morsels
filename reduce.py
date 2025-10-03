from functools import reduce
from math import prod
from operator import concat, mul


def log(msg, indent=4):
    print(" " * indent + msg)


def concat_with_reduce(lst):
    return reduce(concat, lst, "")


def test_concat_with_reduce():
    def test_blank():
        empty_str = ""
        no_chars = list(empty_str)
        input = no_chars
        expected = empty_str

        result = concat_with_reduce(input)

        assert result == expected, f"Expected {expected!r}, got {result!r}"
        log("blank test passed!", 8)

    def test_hello_world():
        message = "hello world"
        chars = list(message)
        input = chars
        expected = message

        result = concat_with_reduce(input)

        assert result == expected, f"Expected {expected!r}, got {result!r}"
        log("hello world test passed!", 8)

    test_blank()
    test_hello_world()
    log("concat tests passed!")


def flatten_with_reduce(lst):
    def concat(x, y):
        return x + y

    return reduce(concat, lst, [])


def test_flatten_with_reduce():
    def test_2_by_2():
        nested = [[0] * 2] * 2
        flat = [0] * 4
        input = nested
        expected = flat

        result = flatten_with_reduce(input)

        assert result == expected, f"Expected {expected!r}, got {result!r}"
        log("2x2 tests passed!", 8)

    test_2_by_2()
    log("flatten tests passed!")


def product_with_reduce(lst):
    return reduce(mul, lst)


def test_product_with_reduce():
    def test_2_by_2():
        nested = [2] * 2
        input = nested
        expected = 4

        result = product_with_reduce(input)

        assert result == expected, f"Expected {expected!r}, got {result!r}"
        log("2x2 tests passed!", 8)

    def test_one_to_ten():
        one_to_ten = list(range(1, 11))
        input = one_to_ten

        product_of_one_to_ten = prod(one_to_ten)
        expected = product_of_one_to_ten

        result = product_with_reduce(input)

        assert result == expected, f"Expected {expected!r}, got {result!r}"
        log("1..10 tests passed!", 8)

    test_2_by_2()
    test_one_to_ten()
    log("product tests passed!")


def test_max_with_reduce():
    def test_all_zeros():
        zeros = [0] * 10
        input = zeros
        expected = 0

        result = max_with_reduce(input)

        assert result == expected, f"Expected {expected!r}, got {result!r}"
        log("all tens tests passed!", 8)

    def test_one_to_ten():
        one_to_ten = list(range(1, 11))
        input = one_to_ten
        expected = 10

        result = max_with_reduce(input)

        assert result == expected, f"Expected {expected!r}, got {result!r}"
        log("1..10 tests passed!", 8)

    test_all_zeros()
    test_one_to_ten()
    log("max tests passed!")


def max_with_reduce(lst):
    return reduce(lambda x, y: x if x > y else y, lst)


def test_min_with_reduce():
    def test_all_zeros():
        zeros = [0] * 10
        input = zeros
        expected = 0

        result = min_with_reduce(input)

        assert result == expected, f"Expected {expected!r}, got {result!r}"
        log("all tens tests passed!", 8)

    def test_one_to_ten():
        one_to_ten = list(range(1, 11))
        input = one_to_ten
        expected = 1

        result = min_with_reduce(input)

        assert result == expected, f"Expected {expected!r}, got {result!r}"
        log("1..10 tests passed!", 8)

    test_all_zeros()
    test_one_to_ten()
    log("min tests passed!")


def min_with_reduce(lst):
    return reduce(lambda x, y: x if y > x else y, lst)


def main():
    test_concat_with_reduce()
    test_flatten_with_reduce()
    test_product_with_reduce()
    test_max_with_reduce()
    test_min_with_reduce()


main()
