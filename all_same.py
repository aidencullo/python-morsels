def all_same(lst):
    return all(x == lst[0] for x in lst) if lst else True


# O(n) time and space
def all_same_operator(lst):
    return len(set(lst)) < 2


def test():
    def tens():
        return [10] * 10

    def one_to_ten():
        return list(range(1, 10))

    def test_all_same():
        assert all_same(tens())
        assert not all_same(one_to_ten())

    def test_all_same_operator():
        assert all_same_operator(tens())
        assert not all_same_operator(one_to_ten())

    test_all_same()
    test_all_same_operator()
    print("tests passed!")


test()
