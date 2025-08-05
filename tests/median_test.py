"""Test the median function."""

from __future__ import annotations

import pytest

from averager import median


@pytest.mark.parametrize(
    ('values', 'expected'),
    [
        ([1, 2, 3, 4, 5], 3),
        ([1, 2, 3], 2),
        ([1.5, 1.5, 1.5], 1.5),
        ([3.21, 4.56, 12.34], 4.56),
    ],
)
def test_median_odd_values_len(values: list[int | float], expected: float) -> None:
    """Test the median of a list of values with an odd length."""
    result = median(*values)

    assert result == expected
    assert type(result) is type(expected)


@pytest.mark.parametrize(
    ('values', 'expected'),
    [([1, 2, 3, 4, 5, 6], 3.5), ([1, 2], 1.5), ([5, 1, 3], 3)],
)
def test_median_even_values_len(values: list[int], expected: float) -> None:
    """Test the median of a list of values with an even length."""
    result = median(*values)

    assert result == expected
    assert type(result) is type(expected)


def test_median_empty_list() -> None:
    """Test that calling median with no values raises an IndexError."""
    with pytest.raises(IndexError):
        median()


def test_median_one_value() -> None:
    """Test the median of a single value."""
    assert median(1) == 1
