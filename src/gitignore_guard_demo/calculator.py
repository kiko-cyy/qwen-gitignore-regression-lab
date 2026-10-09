"""Deliberately small code that an online coding agent can safely edit."""

from __future__ import annotations

Number = float


def add(left: Number, right: Number) -> Number:
    """Return the sum of two numbers."""
    return left + right


def subtract(left: Number, right: Number) -> Number:
    """Return the difference when ``right`` is subtracted from ``left``."""
    return left - right


def divide(dividend: Number, divisor: Number) -> Number:
    """Return a quotient and reject division by zero."""
    if divisor == 0:
        raise ValueError("divisor must not be zero")
    return dividend / divisor
