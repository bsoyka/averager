"""Test the _optional_int utility function."""

import pytest

from averager._utils import _optional_int


@pytest.mark.parametrize('test_input', [1, 2, 3, 4, 5])
def test_int_to_int(test_input: int) -> None:
    """Test that integers remain unchanged and are returned as integers."""
    assert _optional_int(test_input) == test_input
    assert type(_optional_int(test_input)) is int


@pytest.mark.parametrize(
    ('test_input', 'expected'), [(1.0, 1), (2.0, 2), (3.0, 3), (4.0, 4), (5.0, 5)]
)
def test_float_to_int(test_input: float, expected: int) -> None:
    """Test that floats with no decimal part are converted to integers."""
    assert _optional_int(test_input) == expected
    assert type(_optional_int(test_input)) is int


@pytest.mark.parametrize('test_input', [1.2, 2.3, 3.4, 4.5])
def test_float_to_float(test_input: float) -> None:
    """Test that floats with a decimal part are returned as floats."""
    assert _optional_int(test_input) == test_input
    assert type(_optional_int(test_input)) is float
