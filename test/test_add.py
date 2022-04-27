from CalculatorLib import calculator


def test_add():
    assert calculator.add(0,0) == 0
    assert calculator.add(1,2) == 3
    assert calculator.add(-1,2) == 1
    assert calculator.add(-1,-1) == -2
