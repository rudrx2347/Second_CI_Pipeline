import importlib

module = importlib.import_module("40_gcd")


def test_gcd_common_numbers():
    assert module.gcd(12, 18) == 6


def test_gcd_coprime_numbers():
    assert module.gcd(7, 9) == 1


def test_gcd_with_zero():
    assert module.gcd(10, 0) == 10


def test_gcd_equal_numbers():
    assert module.gcd(8, 8) == 8


def test_gcd_negative_numbers():
    assert module.gcd(-12, 18) == 6
