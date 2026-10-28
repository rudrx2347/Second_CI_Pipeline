import importlib

module = importlib.import_module("38_missing_number_xor")


def test_missing_middle_number():
    assert module.missing_number([0, 1, 3, 4]) == 2


def test_missing_zero():
    assert module.missing_number([1, 2, 3]) == 0


def test_missing_last_number():
    assert module.missing_number([0, 1, 2]) == 3


def test_empty_list():
    assert module.missing_number([]) == 0


def test_unsorted_numbers():
    assert module.missing_number([4, 0, 3, 1]) == 2
