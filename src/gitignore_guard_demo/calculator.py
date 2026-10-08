"""Deliberately small code that an online coding agent can safely edit."""


def add(left: float, right: float) -> float:
    """Return the sum of two numbers."""
    return left + right


def divide(dividend: float, divisor: float) -> float:
    """Return a quotient and reject division by zero."""
    if divisor == 0:
        raise ValueError("divisor must not be zero")
    return dividend / divisor
