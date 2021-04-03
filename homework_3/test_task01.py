from python_homework.homework_3.task01 import is_armstrong


def test_nine():
    assert is_armstrong(9) is True


def test_ten():
    assert is_armstrong(10) is False


def test_one_hundred_fifty_tree():
    assert is_armstrong(153) is True


def test_eight_two_zero_eight():
    assert is_armstrong(8208) is True


