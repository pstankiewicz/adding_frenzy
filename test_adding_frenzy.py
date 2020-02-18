from adding_frenzy import add


def test_adding_positive_numbers():
    assert add(5, 10) == 15


def test_adding_negative_numbers():
    assert add(-3, -1) == -4


def test_adding_zeroes():
    assert add(0, 0) == 0


def test_adding_negative_and_positive_result_negative():
    assert add(-8, 2) == -6


def test_adding_negative_and_positive_result_positive():
    assert add(-8, 12) == 4
