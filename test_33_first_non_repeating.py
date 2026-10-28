import importlib

module = importlib.import_module("33_first_non_repeating")


def test_first_character_is_non_repeating():
    assert module.first_non_repeating("abcdabc") == "d"


def test_no_non_repeating_character():
    assert module.first_non_repeating("aabbcc") is None


def test_single_character():
    assert module.first_non_repeating("x") == "x"


def test_empty_string():
    assert module.first_non_repeating("") is None
