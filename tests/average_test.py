"""Test the average function."""

import pytest

from averager import average


@pytest.mark.parametrize(
    ('values', 'expected'),
    [([1, 2], 1.5), ([2, 2, 2, 2, 2], 2), ([1, 2, 3, 4, 5], 3)],
)
def test_average(values: list[int], expected: float) -> None:
    """Test the average of a list of values."""
    result = average(*values)

    assert result == pytest.approx(expected)
    assert type(result) is type(expected)


def test_average_no_values() -> None:
    """Test that calling average with no values raises a ZeroDivisionError."""
    with pytest.raises(ZeroDivisionError):
        average()


@pytest.mark.parametrize('value', [-5, -2.5, -1, 0, 1, 2.5, 5])
def test_average_one_value(value: float) -> None:
    """Test the average of a single value."""
    result = average(value)

    assert result == pytest.approx(value)
    assert type(result) is type(value)
