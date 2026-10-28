import importlib

module = importlib.import_module("37_rotate_string")


def test_rotate_by_two():
    assert module.rotate_string("abcdef", 2) == "efabcd"


def test_rotate_by_one():
    assert module.rotate_string("hello", 1) == "ohell"


def test_rotate_by_string_length():
    assert module.rotate_string("hello", 5) == "hello"


def test_rotate_by_more_than_length():
    assert module.rotate_string("abc", 4) == "cab"


def test_empty_string():
    assert module.rotate_string("", 3) == ""
