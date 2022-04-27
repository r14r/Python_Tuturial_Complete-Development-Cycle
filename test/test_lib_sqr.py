import pytest

from CalculatorLib import calculator


def test_sqr():
    assert calculator.sqr(0) == 0
    assert calculator.sqr(1) == 1
    assert calculator.sqr(2) == 4

    assert calculator.sqr(-1) == 1
    assert calculator.sqr(-2) == 4
