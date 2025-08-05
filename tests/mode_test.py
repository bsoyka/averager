"""Test the mode function."""

from __future__ import annotations

import pytest

from averager import mode


@pytest.mark.parametrize(
    ('values', 'expected'),
    [
        ((1, 2, 3), {1, 2, 3}),
        ((1, 1, 1, 1), 1),
        ((1, 2, 2, 3), 2),
        ((1, 2, 1, 2), {1, 2}),
    ],
)
def test_mode(values: tuple[int], expected: int | set[int]) -> None:
    """Test the mode of a list of values."""
    result = mode(*values)

    assert result == expected
    assert type(result) is type(expected)
