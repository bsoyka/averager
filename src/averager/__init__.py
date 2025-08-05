"""A simple Python library to calculate averages of values."""

from typing import Union,Iterable
from averager._utils import _optional_int
import importlib.metadata

__version__ = importlib.metadata.version('averager')

def average(*values: Union[float, int]) -> Union[float, int]:
    """Calculates an unweighted average

    Args:
        values: The values to find the average of

    Returns:
        The average of the inputs

    Example:
        >>> average(1, 2, 3)
        2
    """

    res = sum(values) / len(values)

    return _optional_int(res)


def weighted_average(
    *values: Iterable[Union[float, int]]
) -> Union[float, int]:
    """Calculates an weighted average

    Args:
        values: The values to find the average as an iterable of
            ``(value, weight)`` pairs

    Returns:
        The weighted average of the inputs

    Example:
        >>> weighted_average((1, 2), (2, 3))
        1.6
    """

    dividend, divisor = 0, 0

    for value, weight in values:
        if weight < 0:
            raise ValueError('Weights cannot be less than zero')

        dividend += value * weight
        divisor += weight

    res = dividend / divisor

    return _optional_int(res)


def median(*values: Union[float, int]) -> Union[float, int]:
    """Calculates the median, or middle number

    Args:
        values: The values to find the median of

    Returns:
        The median of the inputs

    Examples:
        >>> median(1, 2, 3)
        2

        >>> median(1, 2, 3, 4)
        2.5
    """

    values = sorted(values)
    middle = len(values) // 2

    if len(values) % 2 == 0:
        return average(values[middle], values[middle - 1])

    return _optional_int(values[middle])


def mode(*values: Union[float, int]) -> Union[float, int]:
    """Calculates the mode, or most common value

    Args:
        values: The values to find the mode of

    Returns:
        The mode(s) of the inputs (returned as a set if more than one)

    Examples:
        >>> mode(1, 2, 2, 3)
        2

        >>> mode(1, 1, 2, 2)
        {1, 2}
    """

    counts = {}

    for value in values:
        counts[value] = counts.get(value, 0) + 1

    result = {k for k, v in counts.items() if v == max(counts.values())}

    if len(result) == 1:
        return result.pop()

    return result
