from typing import Union


def _optional_int(value: float) -> Union[float, int]:
    """Converts a ``float`` to an ``int`` if they're the same value

    Args:
        value (float)

    Returns:
        Either the original input or the input as an ``int``

    Example:
        >>> _optional_int(3.0)
        3

        >>> _optional_int(1.2)
        1.2
    """
    if value == int(value):
        return int(value)

    return value
