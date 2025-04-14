import pytest
from main import Calculator

def test_add():
    calc = Calculator(4, 5)
    assert calc.add() == 9

def test_subtract():
    calc = Calculator(10, 3)
    assert calc.subtract() == 7

def test_multiply():
    calc = Calculator(3, 4)
    assert calc.multiply() == 12

def test_divide():
    calc = Calculator(20, 4)
    assert calc.divide() == 5.0

def test_divide_by_zero():
    calc = Calculator(5, 0)
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        calc.divide()

