"""Deliberately small code that an online coding agent can safely edit."""


from numbers import Real
from typing import TypeVar

T = TypeVar("T", bound=Real)


def add(left: T, right: T) -> T:
    """Return the sum of two numbers."""
    result: T = left + right  # type: ignore[operator, assignment]
    return result


def divide(dividend: float, divisor: float) -> float:
    """Return a quotient and reject division by zero."""
    if divisor == 0:
        raise ValueError("divisor must not be zero")
    result: float = dividend / divisor
    return result
