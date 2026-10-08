import pytest

from gitignore_guard_demo import add, divide


def test_add() -> None:
    assert add(2, 3) == 5


def test_divide() -> None:
    assert divide(9, 3) == 3


def test_divide_by_zero() -> None:
    with pytest.raises(ValueError, match="must not be zero"):
        divide(1, 0)
