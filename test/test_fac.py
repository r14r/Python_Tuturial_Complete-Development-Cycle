import pytest

from CalculatorLib import calculator


def test_fac():
    assert calculator.fac(0) == 0
    assert calculator.fac(1) == 1
    assert calculator.fac(4) == 4*3*2


def test_fac_negativ_numbers():
    with pytest.raises(Exception) as e_info:
        assert calculator.fac(-1) == 0


def test_fac_negativ_numbers_should_fail():
    with pytest.raises(Exception) as e_info:
        assert calculator.fac(1) == 0
