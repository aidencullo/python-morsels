from functools import reduce


def log(msg, indent=4):
    print(" " * indent + msg)


def concat_with_reduce(lst):
    def concat(x, y):
        return x + y

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
