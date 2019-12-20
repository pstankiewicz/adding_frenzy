from adding_frenzy import add


def test_adding_positive_numbers():
    assert add(5, 10) == 15


def test_adding_negative_numbers():
    assert add(-3, -1) == -4


def test_adding_zeroes():
    assert add(0, 0) == 0
