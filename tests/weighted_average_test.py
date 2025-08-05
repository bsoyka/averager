"""Test the weighted_average function."""

from random import random

import pytest

from averager import weighted_average


@pytest.mark.parametrize(
    ('test_input', 'expected'),
    [
        ([(50, 15), (76, 20), (80, 20), (98, 45)], 82.8),
        ([(20, 7), (45, 3), (15, 4), (0, 2)], 20.9375),
    ],
)
def test_weighted_average(test_input: list[tuple[int, int]], expected: float) -> None:
    """Test the weighted average of a list of (value, weight) tuples."""
    result = weighted_average(*test_input)

    assert result == pytest.approx(expected)
    assert type(result) is type(expected)


def test_weighted_average_no_values() -> None:
    """Test that calling weighted_average with no values raises a ZeroDivisionError."""
    with pytest.raises(ZeroDivisionError):
        weighted_average()


def test_weighted_average_negative_weights() -> None:
    """Test that negative weights raise a ValueError."""
    with pytest.raises(ValueError, match='Weights cannot be less than zero'):
        weighted_average((1, -1), (0, -2))


@pytest.mark.parametrize('value', [1, 53, -4, 6.2, 2.4738])
def test_weighted_average_one_value(value: float) -> None:
    """Test the weighted average of a single value with a random weight."""
    result = weighted_average((value, random() * 100))

    assert result == pytest.approx(value)
    # Not asserting type because the result is sometimes a float
