"""Tests for the calculator module.

Covers basic integer behaviour plus decimal and negative inputs, using
parametrized cases to avoid repeated setup across similar assertions.
"""

import pytest

from gitignore_guard_demo import add, divide


@pytest.mark.parametrize(
    ("left", "right", "expected"),
    [
        (2, 3, 5),                # basic integers
        (0.1, 0.2, 0.3),          # decimals (float precision via approx)
        (2.5, 0.5, 3.0),          # decimals summing to a whole number
        (-2, -3, -5),             # both negative
        (-5, 3, -2),              # mixed signs
        (-2.5, 2.5, 0.0),         # negatives cancelling to zero
    ],
)
def test_add(left: float, right: float, expected: float) -> None:
    assert add(left, right) == pytest.approx(expected)


@pytest.mark.parametrize(
    ("dividend", "divisor", "expected"),
    [
        (9, 3, 3),                # basic integers
        (10, 4, 2.5),             # non-whole quotient
        (7.5, 2.5, 3.0),          # decimals
        (0.5, 0.25, 2.0),         # decimals
        (-10, -4, 2.5),           # both negative
        (-10, 4, -2.5),           # dividend negative
        (-7.5, 2.5, -3.0),        # decimals with negative result
    ],
)
def test_divide(dividend: float, divisor: float, expected: float) -> None:
    assert divide(dividend, divisor) == pytest.approx(expected)


@pytest.mark.parametrize(("dividend", "divisor"), [(1, 0), (-7, 0), (0.5, 0.0)])
def test_divide_by_zero_raises_value_error(dividend: float, divisor: float) -> None:
    with pytest.raises(ValueError, match="must not be zero"):
        divide(dividend, divisor)
