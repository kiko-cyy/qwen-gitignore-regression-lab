import pytest

from gitignore_guard_demo import add, divide, subtract


def test_add() -> None:
    assert add(2, 3) == 5


def test_subtract() -> None:
    assert subtract(5, 3) == 2


def test_subtract_negative_result() -> None:
    assert subtract(3, 5) == -2


def test_subtract_floats() -> None:
    assert subtract(2.5, 1.5) == 1.0


def test_divide() -> None:
    assert divide(9, 3) == 3


def test_divide_by_zero() -> None:
    with pytest.raises(ValueError, match="must not be zero"):
        divide(1, 0)
